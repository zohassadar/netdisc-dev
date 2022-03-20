import dataclasses
import logging
import pprint

from netdisc.base import abstract, device
from netdisc.snmp import easyeng, engine, helper, pyeng, snmpbase
from netdisc.tools import log_setup

log_setup.set_logger(verbose=4)

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


pp = lambda *a, **kw: pprint.pprint(*a, width=200, **kw)


def unfiltered(value):
    return value


def remove_fqdn(value):
    assert isinstance(value, str)
    return value.split(".")[0]


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
class Generic(abstract.Accumulator):
    engine: engine.SNMPEngine

    def __post_init__(self):
        self.device_ip = self.engine.host
        self._object_cache = {}

    def object_cache_get(self, binding: snmpbase.VarBindBase):
        return self._object_cache.setdefault(binding, self.engine.object_get(binding))

    def device(self) -> device.Device:
        result = device.Device(device_ip=self.device_ip, **self.base_info())
        logger.info(
            "The length of devices interfaces and neighbors are: %s and %s",
            len(result.interfaces),
            len(result.neighbors),
        )
        result.interfaces.extend(
            [
                device.Interface(device_ip=self.device_ip, **result)
                for result in self.interfaces()
            ]
        )

        processed = []
        for neighbor in self.neighbors():
            neighbor = device.Neighbor(device_ip=self.device_ip, **neighbor)
            processed.append(neighbor)
        result.neighbors.extend(processed)
        return result

    def base_info(self):
        snmpv2_result = self.object_cache_get(snmpbase.SNMPv2)
        return apply_mapping(snmpv2_result, SNMPv2_MAP, {})

    def interfaces(self):
        results = []
        ifmib_results = self.object_cache_get(snmpbase.IFMIB)
        for ifmib_result in ifmib_results.values():
            results.append(apply_mapping(ifmib_result, IFMIB_MAP, {}))
        return results

    def neighbors(self):
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
        pp(lldp_mgmt_ips)
        results = []
        for idx, neighbor in neighbors.items():
            logger.debug("Processing neighbor index: %s", idx)
            intf_idx = idx.lldp_if
            lldp_port: snmpbase.LLDPInterface = neighbor_ports.interfaces_by_lldp_if[
                intf_idx
            ]
            interface = interfaces.interfaces_by_if_descr[lldp_port.lldpLocPortDesc]
            result = {}
            result = apply_mapping(interface, LLDP_IF_MAP, result)
            result = apply_mapping(neighbor, LLDP_NEIGHBOR_MAP, result)
            if mgmt_ip := lldp_mgmt_ips.ip_by_neigh_idx.get(idx):
                result["ip"] = mgmt_ip
            results.append(result)
        return results

    def routes(self):
        pass

    def vlans(self):
        pass

    def vrfs(self):
        pass

    def macs(self):
        pass

    def arps(self):
        pass


class UnknownDevice(abstract.Accumulator):
    ...


eh = helper.MIBHelper(flags=snmpbase.MIBXlate.NONE)

easy = easyeng.EasySNMPEngine(
    mib_helper=eh,
    host="192.168.42.254",
    community="wordup",
)

ph = helper.MIBHelper(flags=snmpbase.MIBXlate.NONE)

py2 = pyeng.PySNMPEngine(
    mib_helper=ph,
    host="192.168.42.254",
    community="wordup",
)

g = Generic(py2)
d = g.device()

print(len(d.neighbors))
