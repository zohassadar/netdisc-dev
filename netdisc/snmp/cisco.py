import dataclasses
from snmp import base


@dataclasses.dataclass
class CiscoSNMPv2(base.SNMPv2):
    sysObjectID: str = dataclasses.field(
        metadata=base.xlate(
            base.MIBXlate.OID,
            extras=("CISCO-PRODUCTS-MIB",),
        ),
        default=None,
    )


@dataclasses.dataclass
class CDPGlobal(base.ZeroIndex):
    MIB = "CISCO-CDP-MIB"
    cdpGlobalRun: str = dataclasses.field(
        metadata=base.xlate(
            key=base.MIBXlate.NAMED_VALUE,
        ),
        default=None,
    )
    cdpGlobalMessageInterval: str = None
    cdpGlobalHoldTime: str = None
    cdpGlobalDeviceId: str = None
    cdpGlobalLastChange: str = dataclasses.field(
        metadata=base.xlate(
            key=base.MIBXlate.TIMESTAMP,
        ),
        default=None,
    )


@dataclasses.dataclass(frozen=True)
class CDPIntIdx:
    if_idx: int = None


@dataclasses.dataclass
class CDPInterface(base.WalkRequired):
    INDEX = CDPIntIdx
    MIB = "CISCO-CDP-MIB"
    cdpInterfaceEnable: str = dataclasses.field(
        metadata=base.xlate(
            key=base.MIBXlate.NAMED_VALUE,
        ),
        default=None,
    )
    cdpInterfaceGroup: str = None
    cdpInterfaceName: str = None
    cdpInterfacePort: str = None


@dataclasses.dataclass
class CDPNeighbor(base.WalkRequired):
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
class CiscoVTPInfo(base.WalkRequired):
    MIB = "CISCO-VTP-MIB"
    vtpVlanState: str = None
    vtpVlanType: str = None
    vtpVlanName: str = None
    vtpVlanMtu: str = None
    vtpVlanIfIndex: str = None


@dataclasses.dataclass
class CiscoVTPInfo(base.WalkRequired):
    MIB = "CISCO-VTP-MIB"
    vtpVlanState: str = None
    vtpVlanType: str = None
    vtpVlanName: str = None
    vtpVlanMtu: str = None
    vtpVlanIfIndex: str = None


@dataclasses.dataclass
class CiscoMACTableEntry(
    base.MACTableEntry,
    base.CiscoVLANFuckery,
):
    ...
