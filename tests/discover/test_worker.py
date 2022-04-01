from netdisc.discover import worker

from netdisc.base import constant, device_base
import pytest


def test_task_request_valid_proto():
    args = ["1.1.1.1", constant.Proto.API, {}, 4, 5, {}]
    result = worker.TaskRequest(*args)
    aslist = list(result)
    aslist[1] = constant.Proto(aslist[1])
    assert aslist == args


def test_task_request_valid_proto_str():
    args = ["1.1.1.1", "api", {}, 4, 5, {}]
    result = worker.TaskRequest(*args)
    resultlist = list(result)
    assert resultlist[0] == args[0]
    assert resultlist[2:] == args[2:]
    assert constant.Proto(resultlist[1]) is constant.Proto.API


def test_task_request_invalid_proto_int():
    args = ["1.1.1.1", 999, {}, 4, 5, {}]
    with pytest.raises(ValueError):
        worker.TaskRequest(*args)


def test_task_request_invalid_proto_str():
    args = ["1.1.1.1", "invalid", {}, 4, 5, {}]
    with pytest.raises(ValueError):
        worker.TaskRequest(*args)


def test_task_request_no_extra():
    args = ["1.1.1.1", "api", {}, 4, 5]
    result = worker.TaskRequest(*args)
    assert isinstance(result.extra, dict)


def test_task_request_invalid_extra():
    args = ["1.1.1.1", "api", {}, 4, 5, int]
    with pytest.raises(ValueError):
        worker.TaskRequest(*args)


def test_task_request_invalid_extra_json():
    args = ["1.1.1.1", "api", {}, 4, 5, {1: int}]
    with pytest.raises(ValueError):
        worker.TaskRequest(*args)


def test_task_request_invalid_kwargs_json():
    args = ["1.1.1.1", "api", {2: int}, 4, 5, {}]
    with pytest.raises(ValueError):
        worker.TaskRequest(*args)


def test_task_request_invalid_kwargs():
    args = ["1.1.1.1", "api", int, 4, 5, {}]
    with pytest.raises(ValueError):
        worker.TaskRequest(*args)


def test_task_response_valid():
    args = ["1.1.1.1", {}]
    assert list(worker.TaskResponse(*args)) == args


def test_task_response_invalid():
    args = ["1.1.1.1", 1]
    with pytest.raises(ValueError):
        worker.TaskResponse(*args)


def test_task_response_invalid_json():
    args = ["1.1.1.1", {1: int}]
    with pytest.raises(ValueError):
        worker.TaskResponse(*args)


def test_worker_loading_device():
    pass
