from unittest.mock import patch

import pytest
from netdisc.base.device import IP, Interface, Neighbor, Route

from tests.device_fixtures import (
    device_1_interface_2,
    device_1_interface_3_updated,
    device_1_loaded,
    device_1_loaded_with_update,
    device_1_neighbor_3,
    device_2_loaded,
    device_3_loaded,
)


def filter_nones(kvpairs):
    return {k: v for k, v in kvpairs.items() if v is not None}


@pytest.fixture
def Device():
    from netdisc.base.device import Device

    return Device


def test_loading_devices(device_1_loaded, device_2_loaded, device_3_loaded):
    assert device_1_loaded and device_2_loaded and device_3_loaded


def test_new_device(Device):
    print(repr(Device))
    assert Device()


def test_new_interface():
    assert Interface()


def test_new_neighbor():
    assert Neighbor()


def test_new_ip():
    assert IP()


def test_new_route():
    assert Route()


def test_loading_device(Device, device_1_loaded):
    Device().load(device_1_loaded)


def explore_dict(this_dict, that_dict):
    for key in list(this_dict):
        d = this_dict.get(key)
        e = that_dict.get(key)
        if isinstance(d, list):
            for f, g in zip(d, e):
                explore_dict(f, g)
                continue
        if d != e:
            print(f"{d=} {e=}")


def list_dict_compare(list1, list2):
    for e1, e2 in zip(list1, list2):
        if not filter_nones(dict(e1)) == filter_nones(dict(e2)):
            return False
    return True


@pytest.mark.parametrize(
    ("device_data"),
    (
        pytest.param("device_1_loaded"),
        pytest.param("device_2_loaded"),
        pytest.param("device_3_loaded"),
        pytest.param("device_1_loaded_with_update"),
    ),
)
def test_dumping_device(device_data, request, Device):
    device_data = request.getfixturevalue(device_data)
    first_device = Device()
    first_device.load(device_data)
    dumped = first_device.dump()
    second_device = Device()
    second_device.load(dumped)
    assert list_dict_compare(first_device.arps, second_device.arps)
    assert list_dict_compare(first_device.macs, second_device.macs)
    assert list_dict_compare(first_device.routes, second_device.routes)
    assert list_dict_compare(first_device.vrfs, second_device.vrfs)
    assert list_dict_compare(first_device.vlans, second_device.vlans)
    assert list_dict_compare(first_device.ip_addresses, second_device.ip_addresses)
    assert list_dict_compare(first_device.ipv6_addresses, second_device.ipv6_addresses)
    assert list_dict_compare(first_device.interfaces, second_device.interfaces)
    assert list_dict_compare(first_device.neighbors, second_device.neighbors)


def test_device_interface(Device, device_1_loaded, device_1_interface_2):
    device = Device()
    device.load(device_1_loaded)
    result = device.get_interface("Fa1/2")
    assert dict(result) == filter_nones(device_1_interface_2)


def test_device_neighbor(Device, device_1_loaded, device_1_neighbor_3):
    device = Device()
    device.load(device_1_loaded)
    result = device.get_neighbor("Fa1/3", "TEST_DEVICE_3", "Fa3/1")
    assert dict(result) == filter_nones(device_1_neighbor_3)


def test_invalid_container(Device):
    device = Device()
    setup = (
        "invalid_container",
        "get_interface",
        ("interface_name",),
        Interface,
    )
    with pytest.raises(ValueError):
        device.load_list({}, *setup)


def test_container_specified_not_list(Device):
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


def test_update_device_interface(Device, device_1_loaded, device_1_interface_3_updated):
    device = Device(hostname="asdf")
    device.load(device_1_loaded)
    interface = device.get_interface("Fa1/3")
    interface.update({"media": "aidem"})
    assert dict(interface) == device_1_interface_3_updated


def test_update_device(
    Device, device_1_loaded, device_1_loaded_with_update, device_1_interface_3_updated
):
    device = Device(hostname="asdf")
    device.load(device_1_loaded)
    before_interface = device.get_interface("Fa1/3")
    device.load(device_1_loaded_with_update)
    after_interface = device.get_interface("Fa1/3")
    assert dict(after_interface) == device_1_interface_3_updated
    assert before_interface is after_interface


def test_get_vrf_none(Device):
    device = Device()
    result = device.get_vrf("asdf")
    assert result is None


def test_get_vlan_none(Device):
    device = Device()
    result = device.get_vlan("asdf")
    assert result is None


def test_get_route_none(Device):
    device = Device()
    result = device.get_route("asdf", "asdf", "asdf")
    assert result is None


def test_get_neighbor_none(Device):
    device = Device()
    result = device.get_neighbor("asdf", "asdf", "asdf")
    assert result is None


def test_get_mac_none(Device):
    device = Device()
    result = device.get_mac("asdf", "asdf")
    assert result is None


def test_get_ipv6_address_none(Device):
    device = Device()
    result = device.get_ipv6_address("asdf", "asdf")
    assert result is None


def test_get_ip_address_none(Device):
    device = Device()
    result = device.get_ip_address("asdf", "asdf")
    assert result is None


def test_get_interface_none(Device):
    device = Device()
    result = device.get_interface("asdf")
    assert result is None


def test_get_arp_none(Device):
    device = Device()
    result = device.get_arp("asdf", "asdf")
    assert result is None
