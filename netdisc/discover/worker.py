import collections
import json
import logging
import typing
import netdisc.snmp.discover
from netdisc.base import abstract, constant, device_base
from netdisc.tools import helpers

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def get_discovery(proto: constant.Proto) -> typing.Callable:
    def unsupported(**kwargs):
        ip = kwargs.get("ip")
        return device_base.Device(
            device_ip=ip,
            failed=True,
            failure_reason=f"{proto} unsupported",
        )

    match proto:
        case constant.Proto.SNMPv3:
            return netdisc.snmp.discover.snmp_discover
        case constant.Proto.SNMPv2c:
            return netdisc.snmp.discover.snmp_discover
        case _:
            return unsupported


class TaskRequest(
    collections.namedtuple(
        "TaskRequest", "host, proto, kwargs, hostname, sysinfo, extra"
    )
):
    def __new__(
        cls,
        host: str,
        proto: str | constant.Proto,
        kwargs: dict,
        hostname: str | None,
        sysinfo: str | None,
        extra: str | None = None,
    ):

        if isinstance(proto, str):
            try:
                proto = constant.Proto(proto)
            except ValueError as exc:
                raise ValueError("Not a valid Protocol") from exc
        elif not isinstance(proto, constant.Proto):
            raise ValueError("Protocol must be Protocol enum object")

        if extra is not None and not isinstance(extra, dict):
            raise ValueError("extra argument must be a dict")
        elif extra is None:
            extra = {}

        if not isinstance(kwargs, dict):
            raise ValueError("kwargs argument must be a dict")

        try:
            json.dumps(kwargs)
        except TypeError:
            raise ValueError(
                "Protocol keyword arguments dict must be json serializable"
            )

        try:
            json.dumps(extra)
        except TypeError:
            raise ValueError("extra dict must be json serializable")

        return super().__new__(cls, host, proto, kwargs, hostname, sysinfo, extra)


class TaskResponse(collections.namedtuple("TaskResponse", "host, dumped")):
    def __new__(
        cls,
        host: str,
        dumped: dict,
    ):
        if not isinstance(dumped, dict):
            raise ValueError("TaskResponse requires dict as second argument")
        try:
            json.dumps(dumped)
        except TypeError:
            raise ValueError("dumped_device must be JSON serializable")
        return super().__new__(cls, host, dumped)


def discovery_dispatch(task: TaskRequest) -> TaskResponse:
    task = TaskRequest(*task)
    logging.debug("Received request: host=%s, hostname=%s", task.host, task.hostname)
    proto = constant.Proto(task.proto)
    discoverer = get_discovery(proto)
    device = discoverer(
        host=task.host,
        hostname=task.hostname,
        sysinfo=task.sysinfo,
        extra=task.extra,
        **task.kwargs,
    )
    if hasattr(device, "dump"):
        device = device.dump()
    return TaskResponse(task.host, device)
