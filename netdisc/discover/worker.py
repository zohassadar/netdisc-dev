import json
import typing
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

from netdisc.base import constant
from netdisc.discover import apidisc, snmpdisc, sshdisc
from netdisc.tools import helpers

DISCOVERY_MAP = dict()
DISCOVERY_MAP[constant.Proto.API] = apidisc.api_discover
DISCOVERY_MAP[constant.Proto.TELNET] = sshdisc.telnet_discover
DISCOVERY_MAP[constant.Proto.SSH] = sshdisc.ssh_discover
DISCOVERY_MAP[constant.Proto.SNMPv3] = snmpdisc.snmp_discover


class TaskRequestT(typing.NamedTuple):
    ip: str
    proto: str
    kwargs: dict
    hostname: str
    sysinfo: str
    extra: dict


@helpers.debugger(logging.CRITICAL)
def TaskRequest(
    ip: str,
    proto: str,
    kwargs: dict,
    hostname: str = "",
    sysinfo: str = "",
    extra: dict = None,
) -> TaskRequestT:
    if not isinstance(proto, constant.Proto):
        raise ValueError("Protocol must be Protocol enum object")
    proto = str(proto)
    if extra is None:
        extra = {}

    try:
        json.dumps(kwargs)
    except TypeError:
        raise ValueError("Protocol keyword arguments dict must be json serializable")

    try:
        json.dumps(extra)
    except TypeError:
        raise ValueError("extra dict must be json serializable")

    return TaskRequestT(
        ip,
        proto,
        kwargs,
        hostname,
        sysinfo,
        extra,
    )


class TaskResponseT(typing.NamedTuple):
    ip: str
    dumped_device: dict


@helpers.debugger(logging.CRITICAL)
def TaskResponse(ip: str, dumped_device: dict):
    try:
        json.dumps(dumped_device)
    except TypeError:
        raise ValueError("dumped_device must be JSON serializable")
    return TaskResponseT(ip, dumped_device)


@helpers.debugger(logging.CRITICAL)
def do_task(task: TaskRequestT) -> TaskResponseT:
    proto = constant.Proto(task.proto)
    discoverer = DISCOVERY_MAP[proto]
    device = discoverer(
        ip=task.ip,
        hostname=task.hostname,
        sysinfo=task.sysinfo,
        kwargs=task.kwargs,
        extra=task.extra,
    )
    return TaskResponse(task.ip, device)
