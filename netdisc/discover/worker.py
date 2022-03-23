import json
import logging
import collections
import netdisc.snmp.discover
from netdisc.base import constant, device, abstract
from netdisc.tools import helpers

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


DISCOVERY_MAP = dict()
# DISCOVERY_MAP[constant.Proto.API] = apidisc.api_discover
# DISCOVERY_MAP[constant.Proto.TELNET] = sshdisc.telnet_discover
# DISCOVERY_MAP[constant.Proto.SSH] = sshdisc.ssh_discover
DISCOVERY_MAP[constant.Proto.SNMPv3] = netdisc.snmp.discover.discover


class TaskRequest(
    collections.namedtuple("TaskRequest", "ip, proto, kwargs, hostname, sysinfo, extra")
):
    def __new__(
        cls,
        ip: str,
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

        return super().__new__(cls, ip, proto, kwargs, hostname, sysinfo, extra)


class TaskResponse(collections.namedtuple("TaskResponse", "ip, dumped")):
    def __new__(
        cls,
        ip: str,
        dumped: dict,
    ):
        if not isinstance(dumped, dict):
            raise ValueError("TaskResponse requires dict as second argument")
        try:
            json.dumps(dumped)
        except TypeError:
            raise ValueError("dumped_device must be JSON serializable")
        return super().__new__(cls, ip, dumped)


def get_device_dump(gatherer: abstract.Gatherer) -> device.Device:
    result = device.Device()
    result.update(gatherer.get_device())
    result.interfaces.extend(gatherer.get_interfaces())
    result.neighbors.extend(gatherer.get_neighbors())
    result.ip_addresses.extend(gatherer.get_ip_addresses())
    result.ipv6_addresses.extend(gatherer.get_ipv6_addresses())
    result.routes.extend(gatherer.get_routes())
    result.macs.extend(gatherer.get_macs())
    result.arps.extend(gatherer.get_arps())
    result.vlans.extend(gatherer.get_vlans())
    result.vrfs.extend(gatherer.get_vrfs())
    return result.dump()


@helpers.debugger(logging.CRITICAL)
def do_task(task: TaskRequest) -> TaskResponse:
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
