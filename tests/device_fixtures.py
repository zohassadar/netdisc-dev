import yaml
import pytest

import pathlib

DEVICES_PATH = pathlib.Path.joinpath(pathlib.Path(__file__).parent, "devices")

# Build a small fake topology of three devices connected to each other


# d1 Fa1/2  <->  d2 Fa2/1
# d1 Fa1/3  <->  d3 Fa3/1

# d2 Fa2/1  <->  d1 Fa1/2
# d2 Fa2/3  <->  d3 Fa3/2

# d3 Fa3/1  <->  d1 Fa1/3
# d3 Fa3/2  <->  d2 Fa2/3


def open_n_yaml_safe_load(filename):
    with open(filename) as f:
        return yaml.safe_load(f)


DEVICE_1 = pathlib.Path.joinpath(DEVICES_PATH, "device_1.yaml")
DEVICE_2 = pathlib.Path.joinpath(DEVICES_PATH, "device_2.yaml")
DEVICE_3 = pathlib.Path.joinpath(DEVICES_PATH, "device_3.yaml")


@pytest.fixture
def device_1_partial():
    return open_n_yaml_safe_load(DEVICE_1)["device_1"]


@pytest.fixture
def device_2_partial():
    return open_n_yaml_safe_load(DEVICE_2)["device_2"]


@pytest.fixture
def device_3_partial():
    return open_n_yaml_safe_load(DEVICE_3)["device_3"]


@pytest.fixture
def device_1_interface_2():
    return open_n_yaml_safe_load(DEVICE_1)["device_1_interface_2"]


@pytest.fixture
def device_1_interface_3():
    return open_n_yaml_safe_load(DEVICE_1)["device_1_interface_3"]


@pytest.fixture
def device_2_interface_1():
    return open_n_yaml_safe_load(DEVICE_2)["device_2_interface_1"]


@pytest.fixture
def device_2_interface_3():
    return open_n_yaml_safe_load(DEVICE_2)["device_2_interface_3"]


@pytest.fixture
def device_3_interface_1():
    return open_n_yaml_safe_load(DEVICE_3)["device_3_interface_1"]


@pytest.fixture
def device_3_interface_2():
    return open_n_yaml_safe_load(DEVICE_3)["device_3_interface_2"]


@pytest.fixture
def device_1_neighbor_2():
    return open_n_yaml_safe_load(DEVICE_1)["device_1_neighbor_2"]


@pytest.fixture
def device_1_neighbor_3():
    return open_n_yaml_safe_load(DEVICE_1)["device_1_neighbor_3"]


@pytest.fixture
def device_2_neighbor_1():
    return open_n_yaml_safe_load(DEVICE_2)["device_2_neighbor_1"]


@pytest.fixture
def device_2_neighbor_3():
    return open_n_yaml_safe_load(DEVICE_2)["device_2_neighbor_3"]


@pytest.fixture
def device_3_neighbor_1():
    return open_n_yaml_safe_load(DEVICE_3)["device_3_neighbor_1"]


@pytest.fixture
def device_3_neighbor_2():
    return open_n_yaml_safe_load(DEVICE_3)["device_3_neighbor_2"]


@pytest.fixture
def device_1_interfaces():
    return [
        open_n_yaml_safe_load(DEVICE_1)["device_1_interface_2"],
        open_n_yaml_safe_load(DEVICE_1)["device_1_interface_3"],
    ]


@pytest.fixture
def device_2_interfaces():
    return [
        open_n_yaml_safe_load(DEVICE_2)["device_2_interface_1"],
        open_n_yaml_safe_load(DEVICE_2)["device_2_interface_3"],
    ]


@pytest.fixture
def device_3_interfaces():
    return [
        open_n_yaml_safe_load(DEVICE_3)["device_3_interface_2"],
        open_n_yaml_safe_load(DEVICE_3)["device_3_interface_3"],
    ]


@pytest.fixture
def device_1_neighbors():
    return [
        open_n_yaml_safe_load(DEVICE_1)["device_1_neighbor_2"],
        open_n_yaml_safe_load(DEVICE_1)["device_1_neighbor_3"],
    ]


@pytest.fixture
def device_2_neighbors():
    return [
        open_n_yaml_safe_load(DEVICE_2)["device_2_neighbor_1"],
        open_n_yaml_safe_load(DEVICE_2)["device_2_neighbor_3"],
    ]


@pytest.fixture
def device_3_neighbors():
    return [
        open_n_yaml_safe_load(DEVICE_3)["device_3_neighbor_2"],
        open_n_yaml_safe_load(DEVICE_3)["device_3_neighbor_3"],
    ]


@pytest.fixture
def device_1_loaded():
    device = open_n_yaml_safe_load(DEVICE_1)["device_1"]

    interfaces = [
        open_n_yaml_safe_load(DEVICE_1)["device_1_interface_2"],
        open_n_yaml_safe_load(DEVICE_1)["device_1_interface_3"],
    ]
    neighbors = [
        open_n_yaml_safe_load(DEVICE_1)["device_1_neighbor_2"],
        open_n_yaml_safe_load(DEVICE_1)["device_1_neighbor_3"],
    ]

    device["interfaces"].extend(interfaces)
    device["neighbors"].extend(neighbors)
    return device


@pytest.fixture
def device_2_loaded():
    device = open_n_yaml_safe_load(DEVICE_2)["device_2"]

    interfaces = [
        open_n_yaml_safe_load(DEVICE_2)["device_2_interface_1"],
        open_n_yaml_safe_load(DEVICE_2)["device_2_interface_3"],
    ]
    neighbors = [
        open_n_yaml_safe_load(DEVICE_2)["device_2_neighbor_1"],
        open_n_yaml_safe_load(DEVICE_2)["device_2_neighbor_3"],
    ]

    device["interfaces"].extend(interfaces)
    device["neighbors"].extend(neighbors)
    return device


@pytest.fixture
def device_3_loaded():
    device = open_n_yaml_safe_load(DEVICE_3)["device_3"]

    interfaces = [
        open_n_yaml_safe_load(DEVICE_3)["device_3_interface_1"],
        open_n_yaml_safe_load(DEVICE_3)["device_3_interface_2"],
    ]
    neighbors = [
        open_n_yaml_safe_load(DEVICE_3)["device_3_neighbor_1"],
        open_n_yaml_safe_load(DEVICE_3)["device_3_neighbor_2"],
    ]

    device["interfaces"].extend(interfaces)
    device["neighbors"].extend(neighbors)
    return device
