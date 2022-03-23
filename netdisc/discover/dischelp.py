from netdisc.base import device, abstract


def gather_and_test(
    gatherer: abstract.Gatherer,
    disabled=False,
) -> tuple[None | Exception, dict]:
    """This is a pass thru to make sure that data returned by the gatherer
    is valid to the Device class.  Errors can be raised on the worker end before
    the data is sent back to the queue
    """
    result = gatherer.get_device()
    result["interfaces"] = gatherer.get_interfaces()
    result["neighbors"] = gatherer.get_neighbors()
    result["ip_addresses"] = gatherer.get_ip_addresses()
    result["ipv6_addresses"] = gatherer.get_ipv6_addresses()
    result["routes"] = gatherer.get_routes()
    result["macs"] = gatherer.get_macs()
    result["arps"] = gatherer.get_arps()
    result["vlans"] = gatherer.get_vlans()
    result["vrfs"] = gatherer.get_vrfs()

    exception = None

    try:
        device.Device().load(result) if not disabled else None
    except ValueError as exc:
        exception = exc
    return exception, result
