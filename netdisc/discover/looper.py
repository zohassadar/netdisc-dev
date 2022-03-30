""" 
S = Starting Host
N = Neighbor (discovered host

[S1, S2, S3] 
  ->  _hopper



"""

import logging

logging.basicConfig(level=logging.DEBUG)
import collections
import dataclasses
import logging
import queue
import pprint
from netdisc.base import abstract, device
from netdisc.discover import authen, worker

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


@dataclasses.dataclass
class PendingDevice:
    ip: str
    hostname: str = None
    sysinfo: str = None
    auth_methods: authen.AuthMethodList = None
    extra: dict = dataclasses.field(default_factory=dict)

    def __post_init__(self):
        self.failure_reasons: list[str] = []
        self.device: device.Device = device.Device()
        self.dumped_device: dict[str, str | int | bool | list] = {}


@dataclasses.dataclass
class DiscoveryRunner:
    topology: abstract.TopologyBase = None
    hostlist: list = dataclasses.field(
        default_factory=list,
    )
    auth_methods: authen.AuthMethodList = dataclasses.field(
        default_factory=authen.AuthMethodList,
    )
    discovery_q: queue.Queue = dataclasses.field(
        default_factory=queue.Queue,
    )
    discovered_q: queue.Queue = dataclasses.field(
        default_factory=queue.Queue,
    )
    # filters: list[abstract.FilterBase]
    # outputs: list[abstract.OutputBase]
    loop_forever: bool = False
    max_loops: int = 10
    loop_sleep: int = 1

    def loop(self):
        while self._running():
            self._check_new()
            self._check_finished()
        print("complete")

    def __post_init__(self):
        logger.debug("Initializing looper")
        # Devices awaiting discovery
        self._pending: dict[str, PendingDevice] = {}

        # Container of IP addresses confirmed to have been visited.
        self._known_ips: set[str] = set()

        # Devices waiting to be discovered
        self._hopper: collections.deque[PendingDevice] = collections.deque()

        # Start counter for idle cycles
        self._idle_count = 0

        # Run reset to populate self._hopper with self.hostlist
        self._reset()

    def _not_dead(self):
        """Reset the dead timer"""
        logger.debug("we're still alive")
        self._idle_count = 0

    def _reset(self):
        """Reset the state of the loop

        Used at the beginning to fill _hopper

        Used at the end of the loop to fill _hopper with
        the same list as the starting list when loop_forever
        is used
        """
        _starting_hosts = []
        for host in self.hostlist:
            logger.debug("Adding start host: %s", host)
            _pending = PendingDevice(ip=host, auth_methods=self.auth_methods.copy())
            _starting_hosts.append(_pending)
        logger.debug("Resetting looper with %s starting hosts", len(_starting_hosts))
        self._hopper.extend(_starting_hosts)
        self._known_ips = set()

    def _running(self) -> bool:
        """Check both queue lengths and the _hopper length

        Reset if all are empty and loop_forever is enabled
        """

        pprint.pprint(self._pending)
        pprint.pprint(self._known_ips)
        if self._idle_count > self.max_loops:
            logger.error("Exceeded max loops %s", self.max_loops)
            return False
        self._idle_count += 1
        _discovery_l = self.discovery_q.qsize()
        _discovered_l = self.discovered_q.qsize()
        _hopper_l = len(self._hopper)
        _result = bool(_discovery_l + _discovered_l + _hopper_l)
        logger.debug(
            "Q Stats: Idle: %s Pre: %s Post: %s Hopper: %s",
            self._idle_count,
            _discovery_l,
            _discovered_l,
            _hopper_l,
        )
        if not _result and self.loop_forever:
            logger.info("Discovery complete.  Starting over.")
            _result = True
            self._reset()
        elif not _result:
            logger.warning("Discovery complete")
        return _result

    def _add_task_request(self, pending: PendingDevice):
        """If an authentication method is available, put in the queue

        If not, _send_to_topology
        """
        logger.debug(
            "authentication_failure = %s", pending.device.authentication_failure
        )
        auth = pending.auth_methods.next(pending.device.authentication_failure)
        if not auth:
            logger.error("exhausted authentication %s %s", pending.ip, pending.hostname)
            self._send_to_topology(pending)
            return
        logger.info("submitting task for %s %s", pending.ip, pending.hostname)
        logger.debug("auth repr: %s", auth)
        logger.debug("kwargs provided: %s", auth.kwargs)
        task = worker.TaskRequest(
            ip=pending.ip,
            proto=str(auth.proto),
            kwargs=auth.kwargs,
            hostname=pending.hostname,
            sysinfo=pending.sysinfo,
            extra=pending.extra,
        )
        self.discovery_q.put(tuple(task))

    def _check_new(self):
        """Empty _hopper and send to _add_task_request

        ignore IPs that have been seen
        """
        while self._hopper:
            self._not_dead()
            _pending = self._hopper.popleft()
            _ip = _pending.ip
            if _ip in self._known_ips:
                logger.info(f"Skipping %s.  Already visited", _ip)
                continue
            self._known_ips.add(_ip)
            self._pending[_ip] = _pending
            logger.debug(
                "Adding to discovery queue: %s %s",
                _pending.ip,
                _pending.hostname,
            )
            self._add_task_request(_pending)

    def _check_finished(self):
        """Check and see if anything has come back.

        Send to _add_task_request if it failed

        _send_to_topology if it succeeded
        """
        try:
            response = self.discovered_q.get(timeout=self.loop_sleep)
        except queue.Empty:
            logger.info("Nothing complete in the discovered queue")
            return
        self._not_dead()
        _response = worker.TaskResponse(*response)
        _pending = self._pending[_response.ip]
        logger.debug("Popped from the queue %s: %s", _response.ip, _response.dumped)
        _pending.dumped_device = _response.dumped
        _pending.device.load_partial(_pending.dumped_device)
        if _pending.device.failed:
            logger.error(
                "Device failed.  Sending back through: %s %s",
                _pending.ip,
                _pending.hostname,
            )
            self._add_task_request(_pending)
        else:
            logger.info(
                "Device succeeded.  Adding to topology: %s %s",
                _pending.ip,
                _pending.hostname,
            )
            self._send_to_topology(_pending)

    def _send_to_topology(self, pending: PendingDevice):
        """Extract neighbors and send device to topology
        Pop from _pending dictionary
        """
        pending.device.load(pending.dumped_device)
        self._extract_neighbors(pending)
        self._extract_ip_addresses(pending)
        self._pending.pop(pending.ip)
        self.topology.update_device(pending.device)

    def _extract_neighbors(self, pending):
        for neighbor in pending.device.neighbors:
            _pending = PendingDevice(
                auth_methods=self.auth_methods.copy(),
                ip=neighbor.ip,
                hostname=neighbor.hostname,
                sysinfo=neighbor.sysinfo,
            )
            self._hopper.append(_pending)

    def _extract_ip_addresses(self, pending):
        for ip_address in pending.device.ip_addresses:
            self._known_ips.add(ip_address.address)
