import dataclasses
import logging
import sys
import time

from netdisc.base import abstract, device, topology
from netdisc.discover import authen, worker


@dataclasses.dataclass
class PendingDevice:
    ip: str
    hostname: str = None
    sysinfo: str = None
    extra: dict = dataclasses.field(default_factory=dict)

    def __post_init__(self):
        self.auth_methods: authen.AuthMethodList = None
        self.failure_reasons = []
        self.device: device.Device = None
        self.dumped_device: dict = None


@dataclasses.dataclass
class DiscoveryRunner:
    topology: abstract.TopologyBase
    hopper: list[PendingDevice]
    queue: abstract.QueueBase
    auth_methods: authen.AuthMethodList
    # filters: list[abstract.FilterBase]
    outputs: list[abstract.OutputBase]
    server_mode: bool = False
    dead_timer: int = 100
    loop_sleep: int = 1

    def __post_init__(self):
        self._entered = False
        self._pending_devices = {}
        self._on_deck = None
        self._existing_device = None
        self._dead_timer = self.dead_timer
        self._killed = False
        self._reset_hopper()

    def __enter__(self):
        self._entered = True
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.queue.close()

    def run(self):
        if not self._entered:
            raise RuntimeError(
                f"Cannot call {self.__class__.__name__}.run() without using context manager"
            )
        while self._not_dead():
            if self._check_hopper():
                continue
            if self._check_result_queue():
                continue
            logging.info(
                "Sleeping for %s seconds",
                self.loop_sleep,
            )
            time.sleep(self.loop_sleep)

    def _not_dead(self):

        self._dead_timer -= 1
        if self._killed:
            return False
        if self._dead_timer >= 0:
            return True
        if self._pending_devices:
            return False
        if self.server_mode:
            self._reset_hopper()
            return True

    def _reset_hopper(self):
        self._hopper = self.hopper.copy()

    def _reset_on_deck(self):
        self._dead_timer = self.dead_timer
        self._on_deck = None

    def _check_hopper(self):
        if self._on_deck:
            raise RuntimeError(
                "Unexpected.  _check_result_queue called when _on_deck populated"
            )
        if not self._hopper:
            return
        # Pop first element
        pending, self._hopper = self._hopper[0], self._hopper[1:]
        logging.info(
            "Pulled %s %s from the hopper",
            pending.ip,
            pending.hostname,
        )
        self._on_deck = pending
        self._on_deck.auth_methods = self.auth_methods.copy()
        self._submit_new_task()
        return True

    def _check_result_queue(self):
        if self._on_deck:
            raise RuntimeError(
                "Unexpected.  _check_result_queue called when _on_deck populated"
            )
        if self.queue.empty():
            return

        response = self.queue.get(timeout=self.loop_sleep)
        if not response:
            return

        result = worker.TaskResponse(*response)
        logging.debug(self._pending_devices)
        self._on_deck = self._pending_devices.pop(result.ip, None)
        if not self._on_deck:
            raise RuntimeError(f"Pending devices has no entry for {result.ip}")

        self._on_deck.device = device.Device()
        self._on_deck.device.load_partial(result.dumped_device)
        logging.info(
            "Pulled %s %s from the result_queue",
            self._on_deck.device.device_ip,
            self._on_deck.device.hostname,
        )
        self._on_deck.dumped_device = result.dumped_device
        if self._on_deck.device.failed:
            self._on_deck.failure_reasons.append(self._on_deck.device.failure_reason)
        self._submit_new_task()
        return True

    def _submit_new_task(self):
        if not self._on_deck:
            raise RuntimeError(
                "Unexpected. _submit_new_task called when _on_deck not populated"
            )
        if self._on_deck.device and not self._on_deck.device.failed:
            self._update_device()
            return

        if not self._on_deck.device or self._on_deck.device.authentication_failure:
            authmethod = self._on_deck.auth_methods.next()
        else:
            authmethod = self._on_deck.auth_methods.next_protocol()

        if not authmethod:
            self._update_device()
            return

        self._pending_devices[self._on_deck.ip] = self._on_deck
        task = worker.TaskRequest(
            self._on_deck.ip,
            authmethod.proto,
            authmethod.kwargs(),
            self._on_deck.hostname,
            self._on_deck.sysinfo,
            self._on_deck.extra,
        )

        logging.info(
            "Submitting %s %s %s into the task queue",
            self._on_deck.ip,
            self._on_deck.hostname,
            authmethod,
        )
        self.queue.put(task)
        self._reset_on_deck()

    def _add_device(self):
        if not self._on_deck:
            raise RuntimeError(
                "Unexpected. add_device called when _on_deck not populated"
            )
        self._on_deck.device.load(self._on_deck.dumped_device)
        self.topology.add_device(self._on_deck.device)
        self._reset_on_deck()

    def _update_device(self):
        if not self._on_deck:
            raise RuntimeError(
                "Unexpected. _update_device called when _on_deck not populated"
            )
        existing = self.topology.get_device(self._on_deck.ip)
        if not existing:
            self._add_device()
            return
        existing.update(self._on_deck.device)
        topology.update(existing)
        # self._hopper.extend(self.filters(self._on_deck.existing))
        self._reset_on_deck()
