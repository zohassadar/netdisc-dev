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
    """Validated namedtuple

    Args:

        host (str): IP address being discovered
        proto (str | Proto): protocol
        kwargs (dict[str, str]): passed as **kwargs to function
        hostname (str | None): hostname (if known)
        sysinfo (str | None): sysinfo or version info (if known)
        extra (dict): Additional options to pass to the engine
    """

    def __new__(
        cls,
        host: str,
        proto: str,
        kwargs: dict,
        hostname: str | None,
        sysinfo: str | None,
        extra: str | None = None,
    ):
        try:
            proto = str(constant.Proto(proto))
        except ValueError as exc:
            raise ValueError("Not a valid Protocol") from exc

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


class TaskResponse(collections.namedtuple("TaskResponse", "host dumped")):
    """validated named tuple

    Args:
        host (str): IP address of device being discovered
        dumped (dict[str, str|int|bool|list]): result of discovery
    """

    def __new__(cls, host: str, dumped: dict):
        if not isinstance(dumped, dict):
            raise ValueError("TaskResponse requires dict as second argument")
        try:
            json.dumps(dumped)
        except TypeError:
            raise ValueError("dumped_device must be JSON serializable")
        return super().__new__(cls, host, dumped)


def discovery_dispatch(task: TaskRequest) -> TaskResponse:
    """Runs appropriate discovery function based on protocol

    Args:
       task (TaskRequest): namedtuple

    Returns:
       TaskResponse[str, dict[str, str|int|bool|list]]

    """
    task = TaskRequest(*task)
    proto = constant.Proto(task.proto)
    logging.info(
        "Dispatching: host=%s, hostname=%s, proto=%s",
        task.host,
        task.hostname,
        proto,
    )
    discoverer = get_discovery(proto)
    device = discoverer(
        host=task.host,
        hostname=task.hostname,
        sysinfo=task.sysinfo,
        extra=task.extra,
        **task.kwargs,
    )
    logging.info("Dispatch received response from %s", task.host)
    return TaskResponse(task.host, device.dump())
