import dataclasses
from xml.dom.minidom import Attr
from netdisc.snmp import engine, snmpbase
from netdisc.base import abstract
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def unfiltered(value):
    return value


def remove_fqdn(value):
    try:
        return value.split(".")[0]
    except AttributeError:
        return value


SNMPv2_MAP = {
    "hostname": ("sysName", remove_fqdn),
    "full_hostname": ("sysName", unfiltered),
    "sysinfo": ("sysDescr", unfiltered),
    "location": ("sysLocation", unfiltered),
    "contact": ("sysContact", unfiltered),
    "version": ("sysDescr", unfiltered),
}


IFMIB_MAP = {
    "interface_name": ("ifDescr", unfiltered),
    "description": ("ifAlias", unfiltered),
    "speed": ("ifSpeed", unfiltered),
}


LLDP_IF_MAP = {
    "interface_name": ("ifDescr", unfiltered),
}


LLDP_NEIGHBOR_MAP = {
    "interface": ("lldpRemPortId", unfiltered),
    "hostname": ("lldpRemSysName", unfiltered),
    "sysinfo": ("lldpRemSysDesc", unfiltered),
}


def apply_mapping(binding: snmpbase.VarBindBase, mapping: dict, result: dict) -> dict:
    for key, (snmp_key, filter_) in mapping.items():
        result[key] = filter_(getattr(binding, snmp_key))
    return result


@dataclasses.dataclass
class SNMPGeneric(abstract.Gatherer):
    engine: engine.SNMPEngine

    def __post_init__(self):
        self.device_ip = self.engine.host
        self._object_cache = {}

    def object_cache_get(self, binding: snmpbase.VarBindBase):
        return self._object_cache.setdefault(binding, self.engine.object_get(binding))

    def get_device(self):
        snmpv2_result = self.object_cache_get(snmpbase.SNMPv2)
        return apply_mapping(snmpv2_result, SNMPv2_MAP, {})

    def get_interfaces(self):
        results = []
        ifmib_results = self.object_cache_get(snmpbase.IFMIB)
        for ifmib_result in ifmib_results.values():
            results.append(apply_mapping(ifmib_result, IFMIB_MAP, {}))
        return results

    def get_neighbors(self):
        neighbor_ports: snmpbase.LLDPInterfacesDict = self.object_cache_get(
            snmpbase.LLDPInterface
        )
        neighbors: snmpbase.LLDPNeighborDict[
            snmpbase.LLDPNeighIdx, snmpbase.LLDPNeighbor
        ] = self.object_cache_get(snmpbase.LLDPNeighbor)
        interfaces: snmpbase.InterfaceDict = self.object_cache_get(snmpbase.IFMIB)
        lldp_mgmt_ips: snmpbase.LLDPRemMgmtDict = self.object_cache_get(
            snmpbase.LLDPRemMgmtIntf
        )
        results = []
        for idx, neighbor in neighbors.items():
            logger.debug("Processing neighbor index: %s", idx)
            intf_idx = idx.lldp_if
            if not (lldp_port := neighbor_ports.interfaces_by_lldp_if.get(intf_idx)):
                logger.warning("%s not found in interfaces_by_lldp_if", intf_idx)
                continue
            result = {}
            if interface := interfaces.interfaces_by_if_descr.get(
                lldp_port.lldpLocPortDesc
            ):
                result = apply_mapping(interface, LLDP_IF_MAP, result)
            else:
                logger.warning(
                    "%s not found in interfaces_by_if_descr", lldp_port.lldpLocPortDesc
                )
            result = apply_mapping(neighbor, LLDP_NEIGHBOR_MAP, result)
            if mgmt_ip := lldp_mgmt_ips.ip_by_neigh_idx.get(idx):
                result["ip"] = mgmt_ip
            results.append(result)
        return results

    def get_routes(self):
        pass

    def get_vlans(self):
        pass

    def get_vrfs(self):
        pass

    def get_macs(self):
        pass

    def get_arps(self):
        pass

    def get_ip_addresses(self) -> list[dict[str, str | int | bool]]:
        return super().get_ip_addresses()

    def get_ipv6_addresses(self) -> list[dict[str, str | int | bool]]:
        return super().get_ipv6_addresses()
