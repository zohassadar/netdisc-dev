from __future__ import annotations
import dataclasses
import logging
import enum
import collections
import typing
import functools
import re

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class SNMPV2_MIB_SYS_SERVICES(enum.Flag):
    PHYSICAL = 1
    DATALINK = 2
    NETWORK = 4
    TRANSPORT = 8
    SESSION = 16
    PRESENTATION = 32
    APPLICATION = 64


class MIBXlate(enum.IntFlag):
    NONE = 0
    OID = enum.auto()
    BITS = enum.auto()
    NAMED_VALUE = enum.auto()
    MAC = enum.auto()
    IP = enum.auto()
    LOCAL_ENUM = enum.auto()
    TIMETICKS = enum.auto()
    TIMESTAMP = enum.auto()
    PYSNMP = OID | LOCAL_ENUM | MAC | TIMETICKS | TIMESTAMP
    EASYSNMP = -1


METADATA_FLAG_KEY = "_mib_value_xlate_"
METADATA_LOOKUP_INFO = "_lookup_info_"


def xlate(key: MIBXlate, extras: typing.Any = None):
    return {
        METADATA_FLAG_KEY: key,
        METADATA_LOOKUP_INFO: extras,
    }


@dataclasses.dataclass
class VarBindBase:
    _converted = False
    _MIB_NOT_SET = object()
    CONTAINER = dict()
    MIB = _MIB_NOT_SET
    LOOKUP_MIBS = ()

    def __post_init__(self):
        if self.MIB is self._MIB_NOT_SET:
            raise ValueError(f"Attribute MIB is not defined for {type(self).__name__}")


@dataclasses.dataclass
class ZeroIndex(VarBindBase):
    ...


@dataclasses.dataclass
class WalkRequired(VarBindBase):
    INDEX = lambda *args: args
    ...


@dataclasses.dataclass
class CiscoVLANFuckery(VarBindBase):
    ...


@dataclasses.dataclass
class SNMPv2(ZeroIndex):
    MIB = "SNMPv2-MIB"
    sysName: str = None
    sysDescr: str = None
    sysContact: str = None
    sysLocation: str = None
    sysObjectID: str = None
    sysUpTime: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.TIMETICKS,
        ),
        default=None,
    )
    sysServices: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.LOCAL_ENUM,
            extras=SNMPV2_MIB_SYS_SERVICES,
        ),
        default=None,
    )


@dataclasses.dataclass(frozen=True)
class IFIndex:
    if_idx: int


class InterfaceDict(dict):
    @functools.cached_property
    def interfaces_by_if_index(self) -> dict[int, IFMIB]:
        return {idx.if_idx: if_info for idx, if_info in self.items()}

    @functools.cached_property
    def interfaces_by_if_name(self) -> dict[str, IFMIB]:
        return {if_info.ifName: if_info for if_info in self.values()}

    @functools.cached_property
    def interfaces_by_if_descr(self) -> dict[str, IFMIB]:
        return {if_info.ifDescr: if_info for if_info in self.values()}


@dataclasses.dataclass
class IFMIB(WalkRequired):
    CONTAINER = InterfaceDict
    INDEX = IFIndex
    MIB = "IF-MIB"
    ifIndex: str = None
    ifAlias: str = None
    ifName: str = None
    ifDescr: str = None
    ifMtu: str = None
    ifSpeed: str = None
    ifPhysAddress: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.MAC,
        ),
        default=None,
    )
    ifType: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.NAMED_VALUE,
        ),
        default=None,
    )
    ifAdminStatus: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.NAMED_VALUE,
        ),
        default=None,
    )
    ifOperStatus: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.NAMED_VALUE,
        ),
        default=None,
    )


@dataclasses.dataclass
class LLDPGlobal(ZeroIndex):
    MIB = "LLDP-MIB"
    lldpLocSysName: str = None
    lldpLocSysDesc: str = None
    lldpLocSysCapEnabled: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.BITS,
        ),
        default=None,
    )


@dataclasses.dataclass(frozen=True)
class LLDPMgmtIndex:
    af: str = None
    ip: str = None

    def __post_init__(self):
        IPV4_PREFIX = "1.4."  # (Type, Length)
        IPV4_TAG = "ipV4"
        if str(self.af).startswith(IPV4_PREFIX):
            logger.debug("Index delivered as OID beginning with %s", IPV4_PREFIX)
            ip = self.af.replace(IPV4_PREFIX, "")
            af = IPV4_TAG
            object.__setattr__(self, "af", af)
            object.__setattr__(self, "ip", ip)


class LLDPManagementDict(dict):
    @functools.cached_property
    def info_by_ip_address(self) -> dict[str, LLDPMgmtInterface]:
        return {idx.ip: info for idx, info in self.items()}


@dataclasses.dataclass
class LLDPMgmtInterface(WalkRequired):
    CONTAINER = LLDPManagementDict
    INDEX = LLDPMgmtIndex
    MIB = "LLDP-MIB"
    lldpLocManAddrSubtype: str = None
    lldpLocManAddrLen: str = None
    lldpLocManAddrIfSubtype: str = None
    lldpLocManAddrIfId: str = None


@dataclasses.dataclass(frozen=True)
class LLDPIfIndex:
    lldp_if: int = None


class LLDPInterfacesDict(dict):
    @functools.cached_property
    def interfaces_by_lldp_if(self) -> dict[int, LLDPInterface]:
        return {idx.lldp_if: ifinfo for idx, ifinfo in self.items()}

    @functools.cached_property
    def interfaces_by_lldp_port_desc(self) -> dict[str, LLDPInterface]:
        return {ifinfo.lldpLocPortDesc: ifinfo for ifinfo in self.values()}


@dataclasses.dataclass
class LLDPInterface(WalkRequired):
    CONTAINER = LLDPInterfacesDict
    INDEX = LLDPIfIndex
    MIB = "LLDP-MIB"
    lldpLocPortDesc: str = None
    lldpLocPortId: str = None
    lldpLocPortIdSubtype: str = None


@dataclasses.dataclass(frozen=True)
class LLDPNeighIdx:
    NEEDS_CONVERTED = re.compile(r"\d+\.\d+\.\d+").match
    number: int = None
    lldp_if: int = None
    neighbor: int = None

    def __post_init__(self):
        if self.NEEDS_CONVERTED(str(self.number)):
            number, lldp_if, neighbor = self.number.split(".")
            object.__setattr__(self, "number", number)
            object.__setattr__(self, "lldp_if", lldp_if)
            object.__setattr__(self, "neighbor", neighbor)


class LLDPNeighborDict(dict):
    @functools.cached_property
    def neighbor_by_lldp_if(self) -> dict[int, LLDPNeighbor]:
        return {idx.lldp_if: neigh for idx, neigh in self.items()}


@dataclasses.dataclass
class LLDPNeighbor(WalkRequired):
    CONTAINER = LLDPNeighborDict
    INDEX = LLDPNeighIdx
    MIB = "LLDP-MIB"
    lldpRemChassisIdSubtype: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.NAMED_VALUE,
        ),
        default=None,
    )
    lldpRemChassisId: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.MAC,
        ),
        default=None,
    )
    lldpRemPortIdSubtype: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.NAMED_VALUE,
        ),
        default=None,
    )
    lldpRemPortId: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.MAC,
        ),
        default=None,
    )
    lldpRemPortDesc: str = None
    lldpRemSysName: str = None
    lldpRemSysDesc: str = None
    lldpRemSysCapSupported: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.BITS,
        ),
        default=None,
    )
    lldpRemSysCapEnabled: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.BITS,
        ),
        default=None,
    )


@dataclasses.dataclass(frozen=True)
class MACPortIdx:
    mac_port: int = None


class MACPortsDict(dict):
    @functools.cached_property
    def mac_indexes_by_if_index(self) -> dict[int, MACTablePorts]:
        return {
            mac_port.dot1dBasePortIfIndex: idx.mac_port
            for idx, mac_port in self.items()
        }

    @functools.cached_property
    def if_indexes_by_mac_index(self) -> dict[int, MACTablePorts]:
        return {
            idx.mac_port: mac_port.dot1dBasePortIfIndex
            for idx, mac_port in self.items()
        }


@dataclasses.dataclass
class MACTablePorts(WalkRequired):
    CONTAINER = MACPortsDict
    INDEX = MACPortIdx
    MIB = "BRIDGE-MIB"
    dot1dBasePortIfIndex: str = None


@dataclasses.dataclass(frozen=True)
class MACEntryIdx:
    NEEDS_CONVERTED = re.compile(r"\d+\.\d+\.\d+\.\d+\.\d+\.\d+").match
    mac: str = None

    def __post_init__(self):
        if self.NEEDS_CONVERTED(str(self.mac)):
            mac = ":".join(f"{int(n):02x}" for n in self.mac.split("."))
            object.__setattr__(self, "mac", mac)


class MACEntryDict(dict):
    @functools.cached_property
    def mac_entries_by_mac_index(self) -> dict[int, list[MACTableEntry]]:
        result = {}
        for entry in self.values():
            result.setdefault(entry.dot1dTpFdbPort, list()).append(entry)
        return result


@dataclasses.dataclass
class MACTableEntry(WalkRequired):
    CONTAINER = MACEntryDict
    INDEX = MACEntryIdx
    MIB = "BRIDGE-MIB"
    dot1dTpFdbAddress: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.MAC,
        ),
        default=None,
    )
    dot1dTpFdbPort: str = None
    dot1dTpFdbStatus: str = dataclasses.field(
        metadata=xlate(
            key=MIBXlate.NAMED_VALUE,
        ),
        default=None,
    )
