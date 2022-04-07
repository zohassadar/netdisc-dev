import unittest.mock as mock
import pytest
from netdisc.tools import interactive
from netdisc.base import device_base
import os
from tests.device_fixtures import (
    device_1_loaded,
    device_1_neighbor_2,
    device_1_neighbor_3,
)
import contextlib


def setup_module():
    contextlib.redirect_stdout(open(os.devnull, "w"))

    """ setup any state specific to the execution of the given module."""


def teardown_module():

    """teardown any state that was previously setup with a setup_module
    method.
    """


@pytest.fixture
def device_1_neighbor_2_obj(device_1_neighbor_2, capsys):
    neighbor = device_base.Neighbor(**device_1_neighbor_2)
    return neighbor


@pytest.fixture
def device_1_neighbor_3_obj(device_1_neighbor_3, capsys):
    neighbor = device_base.Neighbor(**device_1_neighbor_3)
    return neighbor


@pytest.fixture
def device_1_loaded_obj(
    device_1_loaded,
    device_1_neighbor_2_obj,
    device_1_neighbor_3_obj,
):
    device = device_base.Device()
    device.load(device_1_loaded)
    device.neighbors = [device_1_neighbor_2_obj, device_1_neighbor_3_obj]
    return device


def test_interactive_neighbor_filter_basic(device_1_loaded_obj, capsys):
    capsys
    i = interactive.InteractiveNeighborFilter()
    with mock.patch("builtins.input", lambda *args: "!"):
        i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)


def test_interactive_all_neighbors(device_1_loaded_obj, capsys):
    capsys
    i = interactive.InteractiveNeighborFilter()
    with mock.patch("builtins.input", lambda *args: "a"):
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert not i._discover_all
    assert sorted(results, key=lambda n: n.hostname) == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname
    )


def test_interactive_all_neighbors_going_forward(device_1_loaded_obj, capsys):
    capsys
    i = interactive.InteractiveNeighborFilter()
    with mock.patch("builtins.input", lambda *args: "A"):
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert i._discover_all
    assert sorted(results, key=lambda n: n.hostname) == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname
    )


def test_interactive_all_neighbors_going_forward_set(device_1_loaded_obj, capsys):
    capsys
    i = interactive.InteractiveNeighborFilter()
    i._discover_all = True
    results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert sorted(results, key=lambda n: n.hostname) == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname
    )


def test_interactive_no_neighbors(device_1_loaded_obj, capsys):
    capsys
    i = interactive.InteractiveNeighborFilter()
    with mock.patch("builtins.input", lambda *args: "n"):
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert not i._skip_all
    assert results == []


def test_interactive_no_neighbors_going_forward(device_1_loaded_obj, capsys):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch("builtins.input", lambda *args: "N"):
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert i._skip_all
    assert results == []


def test_interactive_no_neighbors_going_forward_set(device_1_loaded_obj, capsys):
    i = interactive.InteractiveNeighborFilter()
    i._skip_all = True
    results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert results == []


def test_interactive_empty_list(device_1_loaded_obj, capsys):
    i = interactive.InteractiveNeighborFilter()
    results = i.filter(device_1_loaded_obj, [])
    assert results == []


def test_interactive_reset(device_1_loaded_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["r", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert builtins_input.call_count == 2


def test_interactive_filter(device_1_loaded_obj, device_1_neighbor_2_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["f ip in 192.168.42.102/32", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert results == [device_1_neighbor_2_obj]


def test_interactive_invalid_filter(device_1_loaded_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["f ip in 192.168.42.10sdf2/32", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert builtins_input.call_count == 2


def test_interactive_include_range(device_1_loaded_obj, device_1_neighbor_2_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["i 2-5,100", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert results == [device_1_neighbor_2_obj]


def test_interactive_include_range_invalid(
    device_1_loaded_obj, device_1_neighbor_2_obj
):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["i whatever", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert sorted(results, key=lambda n: n.hostname) == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname
    )


def test_interactive_exclude_range(device_1_loaded_obj, device_1_neighbor_2_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["e 0-1,", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert results == [device_1_neighbor_2_obj]


def test_interactive_exclude_range_invalid(
    device_1_loaded_obj, device_1_neighbor_2_obj
):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["e whatever", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert sorted(results, key=lambda n: n.hostname) == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname
    )


def test_interactive_sorted(device_1_loaded_obj, device_1_neighbor_2_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["s hostname", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert results == sorted(device_1_loaded_obj.neighbors, key=lambda n: n.hostname)


def test_interactive_sorted_invalid(device_1_loaded_obj, device_1_neighbor_2_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["s whatever", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert sorted(results, key=lambda n: n.hostname) == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname
    )


def test_interactive_reverse_sorted(device_1_loaded_obj, device_1_neighbor_2_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["rs hostname", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert results == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname, reverse=True
    )


def test_interactive_reverse_sorted_invalid(
    device_1_loaded_obj, device_1_neighbor_2_obj
):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["rs whatever", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert sorted(results, key=lambda n: n.hostname) == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname
    )


def test_interactive_long_help(device_1_loaded_obj, device_1_neighbor_2_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["h", "", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert sorted(results, key=lambda n: n.hostname) == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname
    )


def test_interactive_no_input(device_1_loaded_obj, device_1_neighbor_2_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert sorted(results, key=lambda n: n.hostname) == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname
    )


def test_interactive_invalid_input(device_1_loaded_obj, device_1_neighbor_2_obj):
    i = interactive.InteractiveNeighborFilter()
    with mock.patch(
        "builtins.input", mock.Mock(side_effect=["whatever", "!"])
    ) as builtins_input:
        results = i.filter(device_1_loaded_obj, device_1_loaded_obj.neighbors)
    assert sorted(results, key=lambda n: n.hostname) == sorted(
        device_1_loaded_obj.neighbors, key=lambda n: n.hostname
    )
