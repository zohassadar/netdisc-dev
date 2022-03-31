import logging
import pprint
import queue
import threading
import contextlib
import collections
import pytest
from netdisc.base import constant, device_base, topology
from netdisc.discover import authen, looper, worker

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


@pytest.fixture
def ip_address_set_1():
    return [
        {
            "address": "192.168.11.1",
        },
        {
            "address": "192.168.11.2",
        },
    ]


@pytest.fixture
def ip_address_set_2():
    return [
        {
            "address": "192.168.22.1",
        },
        {
            "address": "192.168.22.2",
        },
    ]


@pytest.fixture
def ip_address_set_3():
    return [
        {
            "address": "192.168.33.1",
        },
        {
            "address": "192.168.33.2",
        },
    ]


@pytest.fixture
def neighbor_set_1():
    return [
        {
            "hostname": "TEST_DEVICE_2",
            "ip": "192.168.22.22",
        },
        {
            "hostname": "TEST_DEVICE_3",
            "ip": "192.168.33.33",
        },
    ]


@pytest.fixture
def neighbor_set_2():
    return [
        {
            "hostname": "TEST_DEVICE_1",
            "ip": "192.168.11.11",
        },
        {
            "hostname": "TEST_DEVICE_3",
            "ip": "192.168.33.33",
        },
    ]


@pytest.fixture
def neighbor_set_3():
    return [
        {
            "hostname": "TEST_DEVICE_1",
            "ip": "192.168.11.11",
        },
        {
            "hostname": "TEST_DEVICE_2",
            "ip": "192.168.22.22",
        },
    ]


@pytest.fixture
def device_authentication_failure():
    return device_base.Device(authentication_failure=True)


@pytest.fixture
def device_failure():
    return device_base.Device(failed=True)


@pytest.fixture
def device_1(ip_address_set_1, neighbor_set_1):
    _device = device_base.Device(device_ip="192.168.11.11")
    _device["interfaces"] = ip_address_set_1
    _device["neighbors"] = neighbor_set_1
    return _device


@pytest.fixture
def device_2(ip_address_set_2, neighbor_set_2):
    _device = device_base.Device()
    _device["interfaces"] = ip_address_set_2
    _device["neighbors"] = neighbor_set_2
    return _device


@pytest.fixture
def device_3(ip_address_set_3, neighbor_set_3):
    _device = device_base.Device()
    _device["interfaces"] = ip_address_set_3
    _device["neighbors"] = neighbor_set_3
    return _device


@pytest.fixture
def devices_dict(device_1, device_2, device_3):
    return {
        "192.168.11.11": device_1,
        "192.168.22.22": device_2,
        "192.168.33.33": device_3,
    }


def get_fake_worker():
    class FakeWorker(threading.Thread):
        def __init__(self, discovery_q, discovered_q):
            super().__init__()
            self.discovery_q = discovery_q
            self.discovered_q = discovered_q
            self.stopped = False
            self.lookup_dict = collections.defaultdict(device_base.Device)

        def run(self):
            while not self.stopped:
                try:
                    _pre = self.discovery_q.get(timeout=1)
                except queue.Empty:
                    if not self.stopped:
                        continue
                    else:
                        break
                _request = worker.TaskRequest(*_pre)
                _response = worker.TaskResponse(
                    _request.ip,
                    self.lookup_dict[_request.ip].dump(),
                )
                self.discovered_q.put(_response)

    discovery_q = queue.Queue()
    discovered_q = queue.Queue()
    fake_worker = FakeWorker(discovery_q, discovered_q)
    return fake_worker


@contextlib.contextmanager
def fake_queueset_returns_auth_failure():
    fake_worker = get_fake_worker()
    fake_worker.lookup_dict = collections.defaultdict(
        lambda _: device_failure,
    )
    yield fake_worker.discovery_q, fake_worker.discovered_q
    fake_worker.stopped = True


@pytest.fixture
def auths():
    auths = authen.AuthMethodList()
    auths.load_authentication_methods(
        {
            "userpass": {
                "username": "asdf",
                "password": "asdf",
            },
            "userpasssecret": {
                "username": "fdsa",
                "password": "fdsa",
                "secret": "secret",
            },
            "version3": {
                "snmpuser": "fdsa",
                "authtype": "fdsa",
                "auth": "secret",
            },
            "version2": {
                "community": "fdsa",
            },
        }
    )
    return auths


@pytest.fixture
def topology():
    class FakeTopology:
        def __init__(self):
            self.results = []

        def update_device(self, device):
            self.results.append(device.dump())

    return FakeTopology()


@pytest.fixture
def starting_hostlist():
    return ["192.168.11.11"]


def test_loading():
    looper.DiscoveryRunner()


def test_loading_with_fixtures(starting_hostlist, auths, topology):
    with fake_queueset_returns_auth_failure() as (
        discovery_q,
        discovered_q,
    ):
        looper.DiscoveryRunner(
            topology=topology,
            hostlist=starting_hostlist,
            auth_methods=auths,
            discovery_q=discovery_q,
            discovered_q=discovered_q,
        )


def test_running_with_fixtures(starting_hostlist, auths, topology):
    with fake_queueset_returns_auth_failure() as (
        discovery_q,
        discovered_q,
    ):
        loop = looper.DiscoveryRunner(
            topology=topology,
            hostlist=starting_hostlist,
            auth_methods=auths,
            discovery_q=discovery_q,
            discovered_q=discovered_q,
            max_loops=2,
            loop_sleep=0.5,
        )
        loop.loop()


class Ignored:
    def __init__(self):

        d = looper.DiscoveryRunner(
            hostlist=["192.168.42.42"],
            loop_forever=False,
            # topology=topo,
            # auth_methods=auths,
        )

        thread = self.ThreadRunner(d.discovery_q, d.discovered_q)
        thread.start()
        d.loop()
        thread.stopped = True
        # what_we_found
