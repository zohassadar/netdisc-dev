#
# PySNMP MIB module CISCO-CDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///mibs.thola.io/asn1/CISCO-CDP-MIB
# Produced by pysmi-0.3.4 at Tue Mar 29 10:05:54 2022
# On host dump platform Linux version 5.4.0-100-generic by user rwd
# Using Python version 3.10.4 (main, Mar 24 2022, 16:12:56) [GCC 9.4.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols(
    "ASN1", "ObjectIdentifier", "OctetString", "Integer"
)
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(
    ConstraintsUnion,
    ValueSizeConstraint,
    SingleValueConstraint,
    ValueRangeConstraint,
    ConstraintsIntersection,
) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsUnion",
    "ValueSizeConstraint",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ConstraintsIntersection",
)
(ciscoMgmt,) = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
CiscoNetworkAddress, CiscoNetworkProtocol = mibBuilder.importSymbols(
    "CISCO-TC", "CiscoNetworkAddress", "CiscoNetworkProtocol"
)
(VlanIndex,) = mibBuilder.importSymbols("CISCO-VTP-MIB", "VlanIndex")
(ifIndex,) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols(
    "SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup"
)
(
    Counter32,
    MibIdentifier,
    IpAddress,
    Counter64,
    Gauge32,
    TimeTicks,
    ModuleIdentity,
    NotificationType,
    Bits,
    ObjectIdentity,
    MibScalar,
    MibTable,
    MibTableRow,
    MibTableColumn,
    Integer32,
    iso,
    Unsigned32,
) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Counter32",
    "MibIdentifier",
    "IpAddress",
    "Counter64",
    "Gauge32",
    "TimeTicks",
    "ModuleIdentity",
    "NotificationType",
    "Bits",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Integer32",
    "iso",
    "Unsigned32",
)
TruthValue, DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols(
    "SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "TimeStamp"
)
ciscoCdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 23))
ciscoCdpMIB.setRevisions(
    (
        "2005-03-21 00:00",
        "2005-03-14 00:00",
        "2001-11-23 00:00",
        "2001-04-23 00:00",
        "2000-11-22 00:00",
        "1998-12-10 00:00",
        "1998-09-16 00:00",
        "1996-07-08 00:00",
        "1995-08-15 00:00",
        "1995-07-27 00:00",
        "1995-01-25 00:00",
    )
)
if mibBuilder.loadTexts:
    ciscoCdpMIB.setLastUpdated("200503210000Z")
if mibBuilder.loadTexts:
    ciscoCdpMIB.setOrganization("Cisco System Inc.")
ciscoCdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 1))
cdpInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1))
cdpCache = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2))
cdpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3))
cdpInterfaceTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1),
)
if mibBuilder.loadTexts:
    cdpInterfaceTable.setStatus("current")
cdpInterfaceEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1),
).setIndexNames((0, "CISCO-CDP-MIB", "cdpInterfaceIfIndex"))
if mibBuilder.loadTexts:
    cdpInterfaceEntry.setStatus("current")
cdpInterfaceIfIndex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)),
)
if mibBuilder.loadTexts:
    cdpInterfaceIfIndex.setStatus("current")
cdpInterfaceEnable = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 2), TruthValue()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    cdpInterfaceEnable.setStatus("current")
cdpInterfaceMessageInterval = (
    MibTableColumn(
        (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 3),
        Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254)),
    )
    .setUnits("seconds")
    .setMaxAccess("readwrite")
)
if mibBuilder.loadTexts:
    cdpInterfaceMessageInterval.setStatus("obsolete")
cdpInterfaceGroup = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 4), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpInterfaceGroup.setStatus("current")
cdpInterfacePort = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 5), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpInterfacePort.setStatus("current")
cdpInterfaceName = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 1, 1, 6), DisplayString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpInterfaceName.setStatus("current")
cdpInterfaceExtTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2),
)
if mibBuilder.loadTexts:
    cdpInterfaceExtTable.setStatus("current")
cdpInterfaceExtEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2, 1),
).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts:
    cdpInterfaceExtEntry.setStatus("current")
cdpInterfaceExtendedTrust = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2, 1, 1),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("trusted", 1), ("noTrust", 2))),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    cdpInterfaceExtendedTrust.setStatus("current")
cdpInterfaceCosForUntrustedPort = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 1, 2, 1, 2),
    Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    cdpInterfaceCosForUntrustedPort.setStatus("current")
cdpCacheTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1),
)
if mibBuilder.loadTexts:
    cdpCacheTable.setStatus("current")
cdpCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1),).setIndexNames(
    (0, "CISCO-CDP-MIB", "cdpCacheIfIndex"), (0, "CISCO-CDP-MIB", "cdpCacheDeviceIndex")
)
if mibBuilder.loadTexts:
    cdpCacheEntry.setStatus("current")
cdpCacheIfIndex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)),
)
if mibBuilder.loadTexts:
    cdpCacheIfIndex.setStatus("current")
cdpCacheDeviceIndex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)),
)
if mibBuilder.loadTexts:
    cdpCacheDeviceIndex.setStatus("current")
cdpCacheAddressType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 3), CiscoNetworkProtocol()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheAddressType.setStatus("current")
cdpCacheAddress = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 4), CiscoNetworkAddress()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheAddress.setStatus("current")
cdpCacheVersion = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 5), DisplayString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheVersion.setStatus("current")
cdpCacheDeviceId = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 6), DisplayString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheDeviceId.setStatus("current")
cdpCacheDevicePort = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 7), DisplayString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheDevicePort.setStatus("current")
cdpCachePlatform = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 8), DisplayString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCachePlatform.setStatus("current")
cdpCacheCapabilities = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 9),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheCapabilities.setStatus("current")
cdpCacheVTPMgmtDomain = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 10),
    DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheVTPMgmtDomain.setStatus("current")
cdpCacheNativeVLAN = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 11), VlanIndex()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheNativeVLAN.setStatus("current")
cdpCacheDuplex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 12),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(
        namedValues=NamedValues(("unknown", 1), ("halfduplex", 2), ("fullduplex", 3))
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheDuplex.setStatus("current")
cdpCacheApplianceID = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 13),
    Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheApplianceID.setStatus("current")
cdpCacheVlanID = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 14),
    Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheVlanID.setStatus("current")
cdpCachePowerConsumption = (
    MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 15), Unsigned32())
    .setUnits("milliwatts")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    cdpCachePowerConsumption.setStatus("current")
cdpCacheMTU = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 16), Unsigned32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheMTU.setStatus("current")
cdpCacheSysName = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 17),
    DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheSysName.setStatus("current")
cdpCacheSysObjectID = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 18), ObjectIdentifier()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheSysObjectID.setStatus("current")
cdpCachePrimaryMgmtAddrType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 19), CiscoNetworkProtocol()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCachePrimaryMgmtAddrType.setStatus("current")
cdpCachePrimaryMgmtAddr = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 20), CiscoNetworkAddress()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCachePrimaryMgmtAddr.setStatus("current")
cdpCacheSecondaryMgmtAddrType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 21), CiscoNetworkProtocol()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheSecondaryMgmtAddrType.setStatus("current")
cdpCacheSecondaryMgmtAddr = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 22), CiscoNetworkAddress()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheSecondaryMgmtAddr.setStatus("current")
cdpCachePhysLocation = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 23), DisplayString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCachePhysLocation.setStatus("current")
cdpCacheLastChange = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 1, 1, 24), TimeStamp()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCacheLastChange.setStatus("current")
cdpCtAddressTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2),
)
if mibBuilder.loadTexts:
    cdpCtAddressTable.setStatus("current")
cdpCtAddressEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1),
).setIndexNames(
    (0, "CISCO-CDP-MIB", "cdpCacheIfIndex"),
    (0, "CISCO-CDP-MIB", "cdpCacheDeviceIndex"),
    (0, "CISCO-CDP-MIB", "cdpCtAddressIndex"),
)
if mibBuilder.loadTexts:
    cdpCtAddressEntry.setStatus("current")
cdpCtAddressIndex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1, 3),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)),
)
if mibBuilder.loadTexts:
    cdpCtAddressIndex.setStatus("current")
cdpCtAddressType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1, 4), CiscoNetworkProtocol()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCtAddressType.setStatus("current")
cdpCtAddress = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 2, 2, 1, 5), CiscoNetworkAddress()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpCtAddress.setStatus("current")
cdpGlobalRun = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 1), TruthValue().clone("true")
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    cdpGlobalRun.setStatus("current")
cdpGlobalMessageInterval = (
    MibScalar(
        (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 2),
        Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254)).clone(60),
    )
    .setUnits("seconds")
    .setMaxAccess("readwrite")
)
if mibBuilder.loadTexts:
    cdpGlobalMessageInterval.setStatus("current")
cdpGlobalHoldTime = (
    MibScalar(
        (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 3),
        Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(180),
    )
    .setUnits("seconds")
    .setMaxAccess("readwrite")
)
if mibBuilder.loadTexts:
    cdpGlobalHoldTime.setStatus("current")
cdpGlobalDeviceId = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 4), DisplayString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpGlobalDeviceId.setStatus("current")
cdpGlobalLastChange = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 5), TimeStamp()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpGlobalLastChange.setStatus("current")
cdpGlobalDeviceIdFormatCpb = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 6),
    Bits().clone(
        namedValues=NamedValues(("serialNumber", 0), ("macAddress", 1), ("other", 2))
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    cdpGlobalDeviceIdFormatCpb.setStatus("current")
cdpGlobalDeviceIdFormat = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 1, 3, 7),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(
        namedValues=NamedValues(("serialNumber", 1), ("macAddress", 2), ("other", 3))
    ),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    cdpGlobalDeviceIdFormat.setStatus("current")
ciscoCdpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 2))
ciscoCdpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1))
ciscoCdpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2))
ciscoCdpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 1)
).setObjects(("CISCO-CDP-MIB", "ciscoCdpMIBGroup"))

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBCompliance = ciscoCdpMIBCompliance.setStatus("obsolete")
ciscoCdpMIBComplianceV11R01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 2)
).setObjects(("CISCO-CDP-MIB", "ciscoCdpMIBGroupV11R01"))

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBComplianceV11R01 = ciscoCdpMIBComplianceV11R01.setStatus("obsolete")
ciscoCdpMIBComplianceV11R02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 3)
).setObjects(("CISCO-CDP-MIB", "ciscoCdpMIBGroupV11R02"))

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBComplianceV11R02 = ciscoCdpMIBComplianceV11R02.setStatus("obsolete")
ciscoCdpMIBComplianceV12R02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 4)
).setObjects(("CISCO-CDP-MIB", "ciscoCdpMIBGroupV12R02"))

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBComplianceV12R02 = ciscoCdpMIBComplianceV12R02.setStatus("obsolete")
ciscoCdpMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 5)
).setObjects(("CISCO-CDP-MIB", "ciscoCdpMIBGroupV12R02"))

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBCompliance5 = ciscoCdpMIBCompliance5.setStatus("deprecated")
ciscoCdpMIBComplianceV12R03 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 1, 6)
).setObjects(
    ("CISCO-CDP-MIB", "ciscoCdpMIBGroupV12R03"),
    ("CISCO-CDP-MIB", "ciscoCdpCtAddressGroup"),
    ("CISCO-CDP-MIB", "ciscoCdpV2MIBGroup"),
    ("CISCO-CDP-MIB", "ciscoCdpV2IfExtGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBComplianceV12R03 = ciscoCdpMIBComplianceV12R03.setStatus("current")
ciscoCdpMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 1)).setObjects(
    ("CISCO-CDP-MIB", "cdpInterfaceEnable"),
    ("CISCO-CDP-MIB", "cdpInterfaceMessageInterval"),
    ("CISCO-CDP-MIB", "cdpCacheAddressType"),
    ("CISCO-CDP-MIB", "cdpCacheAddress"),
    ("CISCO-CDP-MIB", "cdpCacheVersion"),
    ("CISCO-CDP-MIB", "cdpCacheDeviceId"),
    ("CISCO-CDP-MIB", "cdpCacheDevicePort"),
    ("CISCO-CDP-MIB", "cdpCacheCapabilities"),
    ("CISCO-CDP-MIB", "cdpCachePlatform"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBGroup = ciscoCdpMIBGroup.setStatus("obsolete")
ciscoCdpMIBGroupV11R01 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 2)).setObjects(
    ("CISCO-CDP-MIB", "cdpInterfaceEnable"),
    ("CISCO-CDP-MIB", "cdpInterfaceMessageInterval"),
    ("CISCO-CDP-MIB", "cdpInterfaceGroup"),
    ("CISCO-CDP-MIB", "cdpInterfacePort"),
    ("CISCO-CDP-MIB", "cdpCacheAddressType"),
    ("CISCO-CDP-MIB", "cdpCacheAddress"),
    ("CISCO-CDP-MIB", "cdpCacheVersion"),
    ("CISCO-CDP-MIB", "cdpCacheDeviceId"),
    ("CISCO-CDP-MIB", "cdpCacheDevicePort"),
    ("CISCO-CDP-MIB", "cdpCacheCapabilities"),
    ("CISCO-CDP-MIB", "cdpCachePlatform"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBGroupV11R01 = ciscoCdpMIBGroupV11R01.setStatus("obsolete")
ciscoCdpMIBGroupV11R02 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 3)).setObjects(
    ("CISCO-CDP-MIB", "cdpInterfaceEnable"),
    ("CISCO-CDP-MIB", "cdpInterfaceGroup"),
    ("CISCO-CDP-MIB", "cdpInterfacePort"),
    ("CISCO-CDP-MIB", "cdpCacheAddressType"),
    ("CISCO-CDP-MIB", "cdpCacheAddress"),
    ("CISCO-CDP-MIB", "cdpCacheVersion"),
    ("CISCO-CDP-MIB", "cdpCacheDeviceId"),
    ("CISCO-CDP-MIB", "cdpCacheDevicePort"),
    ("CISCO-CDP-MIB", "cdpCacheCapabilities"),
    ("CISCO-CDP-MIB", "cdpCachePlatform"),
    ("CISCO-CDP-MIB", "cdpGlobalRun"),
    ("CISCO-CDP-MIB", "cdpGlobalMessageInterval"),
    ("CISCO-CDP-MIB", "cdpGlobalHoldTime"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBGroupV11R02 = ciscoCdpMIBGroupV11R02.setStatus("obsolete")
ciscoCdpMIBGroupV12R02 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 5)).setObjects(
    ("CISCO-CDP-MIB", "cdpInterfaceEnable"),
    ("CISCO-CDP-MIB", "cdpInterfaceGroup"),
    ("CISCO-CDP-MIB", "cdpInterfacePort"),
    ("CISCO-CDP-MIB", "cdpCacheAddressType"),
    ("CISCO-CDP-MIB", "cdpCacheAddress"),
    ("CISCO-CDP-MIB", "cdpCacheVersion"),
    ("CISCO-CDP-MIB", "cdpCacheDeviceId"),
    ("CISCO-CDP-MIB", "cdpCacheDevicePort"),
    ("CISCO-CDP-MIB", "cdpCacheCapabilities"),
    ("CISCO-CDP-MIB", "cdpCachePlatform"),
    ("CISCO-CDP-MIB", "cdpCacheVTPMgmtDomain"),
    ("CISCO-CDP-MIB", "cdpCacheNativeVLAN"),
    ("CISCO-CDP-MIB", "cdpCacheDuplex"),
    ("CISCO-CDP-MIB", "cdpGlobalRun"),
    ("CISCO-CDP-MIB", "cdpGlobalMessageInterval"),
    ("CISCO-CDP-MIB", "cdpGlobalHoldTime"),
    ("CISCO-CDP-MIB", "cdpGlobalDeviceId"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBGroupV12R02 = ciscoCdpMIBGroupV12R02.setStatus("deprecated")
ciscoCdpV2MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 6)).setObjects(
    ("CISCO-CDP-MIB", "cdpCacheApplianceID"),
    ("CISCO-CDP-MIB", "cdpCacheVlanID"),
    ("CISCO-CDP-MIB", "cdpCachePowerConsumption"),
    ("CISCO-CDP-MIB", "cdpCacheMTU"),
    ("CISCO-CDP-MIB", "cdpCacheSysName"),
    ("CISCO-CDP-MIB", "cdpCacheSysObjectID"),
    ("CISCO-CDP-MIB", "cdpCacheLastChange"),
    ("CISCO-CDP-MIB", "cdpCachePhysLocation"),
    ("CISCO-CDP-MIB", "cdpCachePrimaryMgmtAddrType"),
    ("CISCO-CDP-MIB", "cdpCachePrimaryMgmtAddr"),
    ("CISCO-CDP-MIB", "cdpCacheSecondaryMgmtAddrType"),
    ("CISCO-CDP-MIB", "cdpCacheSecondaryMgmtAddr"),
    ("CISCO-CDP-MIB", "cdpGlobalLastChange"),
    ("CISCO-CDP-MIB", "cdpGlobalDeviceIdFormatCpb"),
    ("CISCO-CDP-MIB", "cdpGlobalDeviceIdFormat"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpV2MIBGroup = ciscoCdpV2MIBGroup.setStatus("current")
ciscoCdpV2IfExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 7)).setObjects(
    ("CISCO-CDP-MIB", "cdpInterfaceExtendedTrust"),
    ("CISCO-CDP-MIB", "cdpInterfaceCosForUntrustedPort"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpV2IfExtGroup = ciscoCdpV2IfExtGroup.setStatus("current")
ciscoCdpCtAddressGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 8)).setObjects(
    ("CISCO-CDP-MIB", "cdpCtAddressType"), ("CISCO-CDP-MIB", "cdpCtAddress")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpCtAddressGroup = ciscoCdpCtAddressGroup.setStatus("current")
ciscoCdpMIBGroupV12R03 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 23, 2, 2, 9)).setObjects(
    ("CISCO-CDP-MIB", "cdpInterfaceEnable"),
    ("CISCO-CDP-MIB", "cdpInterfaceGroup"),
    ("CISCO-CDP-MIB", "cdpInterfacePort"),
    ("CISCO-CDP-MIB", "cdpInterfaceName"),
    ("CISCO-CDP-MIB", "cdpCacheAddressType"),
    ("CISCO-CDP-MIB", "cdpCacheAddress"),
    ("CISCO-CDP-MIB", "cdpCacheVersion"),
    ("CISCO-CDP-MIB", "cdpCacheDeviceId"),
    ("CISCO-CDP-MIB", "cdpCacheDevicePort"),
    ("CISCO-CDP-MIB", "cdpCacheCapabilities"),
    ("CISCO-CDP-MIB", "cdpCachePlatform"),
    ("CISCO-CDP-MIB", "cdpCacheVTPMgmtDomain"),
    ("CISCO-CDP-MIB", "cdpCacheNativeVLAN"),
    ("CISCO-CDP-MIB", "cdpCacheDuplex"),
    ("CISCO-CDP-MIB", "cdpGlobalRun"),
    ("CISCO-CDP-MIB", "cdpGlobalMessageInterval"),
    ("CISCO-CDP-MIB", "cdpGlobalHoldTime"),
    ("CISCO-CDP-MIB", "cdpGlobalDeviceId"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ciscoCdpMIBGroupV12R03 = ciscoCdpMIBGroupV12R03.setStatus("current")
mibBuilder.exportSymbols(
    "CISCO-CDP-MIB",
    cdpCacheNativeVLAN=cdpCacheNativeVLAN,
    ciscoCdpMIBObjects=ciscoCdpMIBObjects,
    cdpCachePrimaryMgmtAddrType=cdpCachePrimaryMgmtAddrType,
    ciscoCdpMIBComplianceV12R02=ciscoCdpMIBComplianceV12R02,
    ciscoCdpMIBGroupV11R01=ciscoCdpMIBGroupV11R01,
    cdpInterfaceEnable=cdpInterfaceEnable,
    cdpCtAddressTable=cdpCtAddressTable,
    cdpGlobalDeviceIdFormatCpb=cdpGlobalDeviceIdFormatCpb,
    cdpInterfacePort=cdpInterfacePort,
    cdpCacheSecondaryMgmtAddr=cdpCacheSecondaryMgmtAddr,
    ciscoCdpMIBGroupV11R02=ciscoCdpMIBGroupV11R02,
    cdpGlobalDeviceIdFormat=cdpGlobalDeviceIdFormat,
    cdpGlobalMessageInterval=cdpGlobalMessageInterval,
    ciscoCdpMIBCompliance=ciscoCdpMIBCompliance,
    cdpCacheLastChange=cdpCacheLastChange,
    ciscoCdpMIBComplianceV11R01=ciscoCdpMIBComplianceV11R01,
    cdpCacheIfIndex=cdpCacheIfIndex,
    cdpInterfaceIfIndex=cdpInterfaceIfIndex,
    cdpInterfaceTable=cdpInterfaceTable,
    cdpCacheDevicePort=cdpCacheDevicePort,
    PYSNMP_MODULE_ID=ciscoCdpMIB,
    cdpCachePrimaryMgmtAddr=cdpCachePrimaryMgmtAddr,
    cdpCachePhysLocation=cdpCachePhysLocation,
    cdpGlobalRun=cdpGlobalRun,
    ciscoCdpMIBGroupV12R03=ciscoCdpMIBGroupV12R03,
    cdpCtAddressEntry=cdpCtAddressEntry,
    cdpCacheSysName=cdpCacheSysName,
    cdpInterfaceCosForUntrustedPort=cdpInterfaceCosForUntrustedPort,
    cdpCacheMTU=cdpCacheMTU,
    cdpCtAddressIndex=cdpCtAddressIndex,
    cdpInterfaceGroup=cdpInterfaceGroup,
    cdpCacheDuplex=cdpCacheDuplex,
    ciscoCdpMIBGroups=ciscoCdpMIBGroups,
    ciscoCdpMIB=ciscoCdpMIB,
    ciscoCdpMIBCompliance5=ciscoCdpMIBCompliance5,
    ciscoCdpCtAddressGroup=ciscoCdpCtAddressGroup,
    cdpCacheSecondaryMgmtAddrType=cdpCacheSecondaryMgmtAddrType,
    cdpInterfaceEntry=cdpInterfaceEntry,
    ciscoCdpMIBComplianceV12R03=ciscoCdpMIBComplianceV12R03,
    cdpInterfaceExtTable=cdpInterfaceExtTable,
    cdpCtAddress=cdpCtAddress,
    ciscoCdpMIBComplianceV11R02=ciscoCdpMIBComplianceV11R02,
    cdpInterfaceMessageInterval=cdpInterfaceMessageInterval,
    cdpCachePlatform=cdpCachePlatform,
    cdpGlobalDeviceId=cdpGlobalDeviceId,
    ciscoCdpMIBCompliances=ciscoCdpMIBCompliances,
    ciscoCdpMIBGroupV12R02=ciscoCdpMIBGroupV12R02,
    cdpCacheVersion=cdpCacheVersion,
    cdpCacheTable=cdpCacheTable,
    cdpInterface=cdpInterface,
    cdpGlobalLastChange=cdpGlobalLastChange,
    ciscoCdpV2MIBGroup=ciscoCdpV2MIBGroup,
    ciscoCdpMIBConformance=ciscoCdpMIBConformance,
    cdpCacheAddressType=cdpCacheAddressType,
    cdpCacheApplianceID=cdpCacheApplianceID,
    cdpCacheVTPMgmtDomain=cdpCacheVTPMgmtDomain,
    cdpGlobalHoldTime=cdpGlobalHoldTime,
    cdpInterfaceExtEntry=cdpInterfaceExtEntry,
    cdpCacheCapabilities=cdpCacheCapabilities,
    cdpCacheDeviceId=cdpCacheDeviceId,
    cdpCacheAddress=cdpCacheAddress,
    cdpCacheEntry=cdpCacheEntry,
    cdpCacheDeviceIndex=cdpCacheDeviceIndex,
    cdpCacheVlanID=cdpCacheVlanID,
    cdpInterfaceName=cdpInterfaceName,
    cdpCachePowerConsumption=cdpCachePowerConsumption,
    cdpCacheSysObjectID=cdpCacheSysObjectID,
    ciscoCdpMIBGroup=ciscoCdpMIBGroup,
    cdpCache=cdpCache,
    cdpInterfaceExtendedTrust=cdpInterfaceExtendedTrust,
    cdpCtAddressType=cdpCtAddressType,
    ciscoCdpV2IfExtGroup=ciscoCdpV2IfExtGroup,
    cdpGlobal=cdpGlobal,
)
