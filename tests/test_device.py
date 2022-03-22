import pytest
from netdisc.base import device
from netdisc.base.device import IP, Device, Interface, Neighbor, Route

from device_fixtures import (
    device_1_interface_2,
    device_1_neighbor_3,
    device_1_loaded,
    device_2_loaded,
    device_3_loaded,
)


def test_loading_devices(device_1_loaded, device_2_loaded, device_3_loaded):
    assert device_1_loaded and device_2_loaded and device_3_loaded


def test_new_device():
    assert Device()


def test_new_interface():
    assert Interface()


def test_new_neighbor():
    assert Neighbor()


def test_new_ip():
    assert IP()


def test_new_route():
    assert Route()


def test_loading_device(device_1_loaded):
    Device().load(device_1_loaded)


def test_device_interface(device_1_loaded, device_1_interface_2):
    device = Device()
    device.load(device_1_loaded)
    result = device.get_interface("Fa1/2")
    assert dict(result) == device_1_interface_2


def test_device_neighbor(device_1_loaded, device_1_neighbor_3):
    device = Device()
    device.load(device_1_loaded)
    result = device.get_neighbor("Fa1/3", "TEST_DEVICE_3", "Fa3/1")
    assert dict(result) == device_1_neighbor_3


def test_invalid_container():
    device = Device()
    setup = (
        "invalid_container",
        "get_interface",
        ("interface_name",),
        Interface,
    )
    with pytest.raises(ValueError):
        device.load_list({}, *setup)


def test_container_specified_not_list():
    device = Device(hostname="asdf")
    setup = (
        "hostname",
        "get_interface",
        ("interface_name",),
        Interface,
    )
    with pytest.raises(ValueError) as raised:
        device.load_list({}, *setup)
    print(raised.value)
