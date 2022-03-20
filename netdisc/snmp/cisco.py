import dataclasses
from netdisc.snmp import snmpbase


@dataclasses.dataclass
class CiscoSNMPv2(snmpbase.SNMPv2):
    sysObjectID: str = dataclasses.field(
        metadata=snmpbase.xlate(
            snmpbase.MIBXlate.OID,
            extras=("CISCO-PRODUCTS-MIB",),
        ),
        default=None,
    )


@dataclasses.dataclass
class CDPGlobal(snmpbase.ZeroIndex):
    MIB = "CISCO-CDP-MIB"
    cdpGlobalRun: str = dataclasses.field(
        metadata=snmpbase.xlate(
            key=snmpbase.MIBXlate.NAMED_VALUE,
        ),
        default=None,
    )
    cdpGlobalMessageInterval: str = None
    cdpGlobalHoldTime: str = None
    cdpGlobalDeviceId: str = None
    cdpGlobalLastChange: str = dataclasses.field(
        metadata=snmpbase.xlate(
            key=snmpbase.MIBXlate.TIMESTAMP,
        ),
        default=None,
    )


@dataclasses.dataclass(frozen=True)
class CDPIntIdx:
    if_idx: int = None


@dataclasses.dataclass
class CDPInterface(snmpbase.WalkRequired):
    INDEX = CDPIntIdx
    MIB = "CISCO-CDP-MIB"
    cdpInterfaceEnable: str = dataclasses.field(
        metadata=snmpbase.xlate(
            key=snmpbase.MIBXlate.NAMED_VALUE,
        ),
        default=None,
    )
    cdpInterfaceGroup: str = None
    cdpInterfaceName: str = None
    cdpInterfacePort: str = None


@dataclasses.dataclass
class CDPNeighbor(snmpbase.WalkRequired):
    MIB = "CISCO-CDP-MIB"
    cdpCacheAddress: str = None
    cdpCacheAddressType: str = None
    cdpCacheCapabilities: str = None
    cdpCacheDeviceId: str = None
    cdpCacheDevicePort: str = None
    cdpCacheDuplex: str = None
    cdpCacheLastChange: str = None
    cdpCacheNativeVLAN: str = None
    cdpCachePlatform: str = None
    cdpCacheVTPMgmtDomain: str = None
    cdpCacheVersion: str = None
    cdpCachePrimaryMgmtAddrType: str = None
    cdpCachePrimaryMgmtAddr: str = None
    cdpCacheSecondaryMgmtAddrType: str = None
    cdpCacheSecondaryMgmtAddr: str = None


@dataclasses.dataclass
class CiscoVTPInfo(snmpbase.WalkRequired):
    MIB = "CISCO-VTP-MIB"
    vtpVlanState: str = None
    vtpVlanType: str = None
    vtpVlanName: str = None
    vtpVlanMtu: str = None
    vtpVlanIfIndex: str = None


@dataclasses.dataclass
class CiscoMACTableEntry(
    snmpbase.MACTableEntry,
    snmpbase.CiscoVLANFuckery,
):
    ...
