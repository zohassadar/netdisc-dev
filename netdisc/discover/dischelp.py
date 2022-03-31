import enum
from netdisc.base import abstract, device_base


class DiscoveryOptions(enum.IntFlag):
    INTERFACES = enum.auto()
    NEIGHBORS = enum.auto()
    IP_ADDRESSES = enum.auto()
    IPv6_ADDRESSES = enum.auto()
    ROUTES = enum.auto()
    MACS = enum.auto()
    ARPS = enum.auto()
    VLANS = enum.auto()
    VRFS = enum.auto()
    STP = enum.auto()
    DNS = enum.auto()


def gather_and_test(
    gatherer: abstract.Gatherer,
    flags: DiscoveryOptions = DiscoveryOptions(-1),
) -> device_base.Device:
    """This is a pass thru to make sure that data returned by the gatherer
    is valid to the Device class.  Errors can be raised on the worker end before
    the data is sent back to the queue
    """
    result = {}
    partial = gatherer.get_device()
    result.update(partial)
    if DiscoveryOptions.INTERFACES in flags:
        result["interfaces"] = gatherer.get_interfaces()
    if DiscoveryOptions.NEIGHBORS in flags:
        result["neighbors"] = gatherer.get_neighbors()
    if DiscoveryOptions.IP_ADDRESSES in flags:
        result["ip_addresses"] = gatherer.get_ip_addresses()
    if DiscoveryOptions.IPv6_ADDRESSES in flags:
        result["ipv6_addresses"] = gatherer.get_ipv6_addresses()
    if DiscoveryOptions.ROUTES in flags:
        result["routes"] = gatherer.get_routes()
    if DiscoveryOptions.MACS in flags:
        result["macs"] = gatherer.get_macs()
    if DiscoveryOptions.ARPS in flags:
        result["arps"] = gatherer.get_arps()
    if DiscoveryOptions.VLANS in flags:
        result["vlans"] = gatherer.get_vlans()
    if DiscoveryOptions.VRFS in flags:
        result["vrfs"] = gatherer.get_vrfs()

    try:
        device = device_base.Device()
        device.load(result)
        return device
    except ValueError as exc:
        full_load_error = exc

    try:
        device = device_base.Device()
        device.load(partial)
        sep = ", "
        device.failure_history = sep.join(
            (
                device.failure_history,
                full_load_error,
            )
        ).strip(sep)
        return device
    except ValueError as exc:
        partial_load_error = exc

    return device_base.Device(
        failed=True,
        device_ip=partial.get("device_ip"),
        failure_reason=partial_load_error,
        failure_history=full_load_error,
    )
