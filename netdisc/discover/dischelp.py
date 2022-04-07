import enum
from netdisc.base import abstract, device_base
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


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


class GatherBase(abstract.Gatherer):
    def get_device(self):
        logger.error("Not Implemented")
        return {}

    def get_interfaces(self):
        logger.error("Not Implemented")
        return []

    def get_neighbors(self):
        logger.error("Not Implemented")
        return []

    def get_routes(self):
        logger.error("Not Implemented")
        return []

    def get_vlans(self):
        logger.error("Not Implemented")
        return []

    def get_vrfs(self):
        logger.error("Not Implemented")
        return []

    def get_macs(self):
        logger.error("Not Implemented")
        return []

    def get_arps(self):
        logger.error("Not Implemented")
        return []

    def get_ip_addresses(self):
        logger.error("Not Implemented")
        return []

    def get_ipv6_addresses(self):
        logger.error("Not Implemented")
        return []

    def get_device_object(
        self,
        flags: DiscoveryOptions = DiscoveryOptions(-1),
    ) -> device_base.Device:
        """This is a pass thru to make sure that data returned by the gatherer
        is valid to the Device class.  Errors can be raised on the worker end before
        the data is sent back to the queue
        """
        result = {}
        partial = self.get_device()
        result.update(partial)
        if DiscoveryOptions.INTERFACES in flags:
            result["interfaces"] = self.get_interfaces()
        if DiscoveryOptions.NEIGHBORS in flags:
            result["neighbors"] = self.get_neighbors()
        if DiscoveryOptions.IP_ADDRESSES in flags:
            result["ip_addresses"] = self.get_ip_addresses()
        if DiscoveryOptions.IPv6_ADDRESSES in flags:
            result["ipv6_addresses"] = self.get_ipv6_addresses()
        if DiscoveryOptions.ROUTES in flags:
            result["routes"] = self.get_routes()
        if DiscoveryOptions.MACS in flags:
            result["macs"] = self.get_macs()
        if DiscoveryOptions.ARPS in flags:
            result["arps"] = self.get_arps()
        if DiscoveryOptions.VLANS in flags:
            result["vlans"] = self.get_vlans()
        if DiscoveryOptions.VRFS in flags:
            result["vrfs"] = self.get_vrfs()

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
                    device.failure_history if device.failure_history else "",
                    str(full_load_error),
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
