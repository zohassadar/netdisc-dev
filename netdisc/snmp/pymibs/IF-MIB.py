#
# PySNMP MIB module IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///mibs.thola.io/asn1/IF-MIB
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
(IANAifType,) = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols(
    "SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup"
)
(snmpTraps,) = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
(
    MibIdentifier,
    IpAddress,
    Counter64,
    MibScalar,
    MibTable,
    MibTableRow,
    MibTableColumn,
    Gauge32,
    mib_2,
    TimeTicks,
    ModuleIdentity,
    NotificationType,
    Bits,
    ObjectIdentity,
    Counter32,
    Integer32,
    iso,
    Unsigned32,
) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "MibIdentifier",
    "IpAddress",
    "Counter64",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Gauge32",
    "mib-2",
    "TimeTicks",
    "ModuleIdentity",
    "NotificationType",
    "Bits",
    "ObjectIdentity",
    "Counter32",
    "Integer32",
    "iso",
    "Unsigned32",
)
(
    TestAndIncr,
    DisplayString,
    TextualConvention,
    TimeStamp,
    PhysAddress,
    TruthValue,
    AutonomousType,
    RowStatus,
) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TestAndIncr",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "PhysAddress",
    "TruthValue",
    "AutonomousType",
    "RowStatus",
)
ifMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 31))
ifMIB.setRevisions(
    (
        "2000-06-14 00:00",
        "1996-02-28 21:55",
        "1993-11-08 21:55",
    )
)
if mibBuilder.loadTexts:
    ifMIB.setLastUpdated("200006140000Z")
if mibBuilder.loadTexts:
    ifMIB.setOrganization("IETF Interfaces MIB Working Group")
ifMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 31, 1))
interfaces = MibIdentifier((1, 3, 6, 1, 2, 1, 2))


class OwnerString(TextualConvention, OctetString):
    status = "deprecated"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)


class InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)


class InterfaceIndexOrZero(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)


ifNumber = MibScalar((1, 3, 6, 1, 2, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifNumber.setStatus("current")
ifTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 31, 1, 5), TimeTicks()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifTableLastChange.setStatus("current")
ifTable = MibTable(
    (1, 3, 6, 1, 2, 1, 2, 2),
)
if mibBuilder.loadTexts:
    ifTable.setStatus("current")
ifEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 2, 2, 1),
).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts:
    ifEntry.setStatus("current")
ifIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 1), InterfaceIndex()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifIndex.setStatus("current")
ifDescr = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 2),
    DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifDescr.setStatus("current")
ifType = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 3), IANAifType()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifType.setStatus("current")
ifMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 4), Integer32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifMtu.setStatus("current")
ifSpeed = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 5), Gauge32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifSpeed.setStatus("current")
ifPhysAddress = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 6), PhysAddress()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifPhysAddress.setStatus("current")
ifAdminStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 7),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    ifAdminStatus.setStatus("current")
ifOperStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 8),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7)))
    .clone(
        namedValues=NamedValues(
            ("up", 1),
            ("down", 2),
            ("testing", 3),
            ("unknown", 4),
            ("dormant", 5),
            ("notPresent", 6),
            ("lowerLayerDown", 7),
        )
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifOperStatus.setStatus("current")
ifLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 9), TimeTicks()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifLastChange.setStatus("current")
ifInOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 10), Counter32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifInOctets.setStatus("current")
ifInUcastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 11), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifInUcastPkts.setStatus("current")
ifInNUcastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 12), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifInNUcastPkts.setStatus("deprecated")
ifInDiscards = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 13), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifInDiscards.setStatus("current")
ifInErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 14), Counter32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifInErrors.setStatus("current")
ifInUnknownProtos = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 15), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifInUnknownProtos.setStatus("current")
ifOutOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 16), Counter32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifOutOctets.setStatus("current")
ifOutUcastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 17), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifOutUcastPkts.setStatus("current")
ifOutNUcastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 18), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifOutNUcastPkts.setStatus("deprecated")
ifOutDiscards = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 19), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifOutDiscards.setStatus("current")
ifOutErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 20), Counter32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifOutErrors.setStatus("current")
ifOutQLen = MibTableColumn((1, 3, 6, 1, 2, 1, 2, 2, 1, 21), Gauge32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifOutQLen.setStatus("deprecated")
ifSpecific = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 22), ObjectIdentifier()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifSpecific.setStatus("deprecated")
ifXTable = MibTable(
    (1, 3, 6, 1, 2, 1, 31, 1, 1),
)
if mibBuilder.loadTexts:
    ifXTable.setStatus("current")
ifXEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1),
)
ifEntry.registerAugmentions(("IF-MIB", "ifXEntry"))
ifXEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts:
    ifXEntry.setStatus("current")
ifName = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 1), DisplayString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifName.setStatus("current")
ifInMulticastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 2), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifInMulticastPkts.setStatus("current")
ifInBroadcastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 3), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifInBroadcastPkts.setStatus("current")
ifOutMulticastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 4), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifOutMulticastPkts.setStatus("current")
ifOutBroadcastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 5), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifOutBroadcastPkts.setStatus("current")
ifHCInOctets = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 6), Counter64()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifHCInOctets.setStatus("current")
ifHCInUcastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 7), Counter64()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifHCInUcastPkts.setStatus("current")
ifHCInMulticastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 8), Counter64()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifHCInMulticastPkts.setStatus("current")
ifHCInBroadcastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 9), Counter64()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifHCInBroadcastPkts.setStatus("current")
ifHCOutOctets = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 10), Counter64()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifHCOutOctets.setStatus("current")
ifHCOutUcastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 11), Counter64()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifHCOutUcastPkts.setStatus("current")
ifHCOutMulticastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 12), Counter64()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifHCOutMulticastPkts.setStatus("current")
ifHCOutBroadcastPkts = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 13), Counter64()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifHCOutBroadcastPkts.setStatus("current")
ifLinkUpDownTrapEnable = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 14),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    ifLinkUpDownTrapEnable.setStatus("current")
ifHighSpeed = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 15), Gauge32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifHighSpeed.setStatus("current")
ifPromiscuousMode = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 16), TruthValue()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    ifPromiscuousMode.setStatus("current")
ifConnectorPresent = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 17), TruthValue()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifConnectorPresent.setStatus("current")
ifAlias = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 18),
    DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    ifAlias.setStatus("current")
ifCounterDiscontinuityTime = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 1, 1, 19), TimeStamp()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifCounterDiscontinuityTime.setStatus("current")
ifStackTable = MibTable(
    (1, 3, 6, 1, 2, 1, 31, 1, 2),
)
if mibBuilder.loadTexts:
    ifStackTable.setStatus("current")
ifStackEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1),
).setIndexNames((0, "IF-MIB", "ifStackHigherLayer"), (0, "IF-MIB", "ifStackLowerLayer"))
if mibBuilder.loadTexts:
    ifStackEntry.setStatus("current")
ifStackHigherLayer = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1, 1), InterfaceIndexOrZero()
)
if mibBuilder.loadTexts:
    ifStackHigherLayer.setStatus("current")
ifStackLowerLayer = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1, 2), InterfaceIndexOrZero()
)
if mibBuilder.loadTexts:
    ifStackLowerLayer.setStatus("current")
ifStackStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 2, 1, 3), RowStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    ifStackStatus.setStatus("current")
ifStackLastChange = MibScalar((1, 3, 6, 1, 2, 1, 31, 1, 6), TimeTicks()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    ifStackLastChange.setStatus("current")
ifRcvAddressTable = MibTable(
    (1, 3, 6, 1, 2, 1, 31, 1, 4),
)
if mibBuilder.loadTexts:
    ifRcvAddressTable.setStatus("current")
ifRcvAddressEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1),
).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "IF-MIB", "ifRcvAddressAddress"))
if mibBuilder.loadTexts:
    ifRcvAddressEntry.setStatus("current")
ifRcvAddressAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 31, 1, 4, 1, 1), PhysAddress())
if mibBuilder.loadTexts:
    ifRcvAddressAddress.setStatus("current")
ifRcvAddressStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1, 2), RowStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    ifRcvAddressStatus.setStatus("current")
ifRcvAddressType = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 4, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(namedValues=NamedValues(("other", 1), ("volatile", 2), ("nonVolatile", 3)))
    .clone("volatile"),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    ifRcvAddressType.setStatus("current")
linkDown = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 3)).setObjects(
    ("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus")
)
if mibBuilder.loadTexts:
    linkDown.setStatus("current")
linkUp = NotificationType((1, 3, 6, 1, 6, 3, 1, 1, 5, 4)).setObjects(
    ("IF-MIB", "ifIndex"), ("IF-MIB", "ifAdminStatus"), ("IF-MIB", "ifOperStatus")
)
if mibBuilder.loadTexts:
    linkUp.setStatus("current")
ifConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 31, 2))
ifGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 31, 2, 1))
ifCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 31, 2, 2))
ifCompliance3 = ModuleCompliance((1, 3, 6, 1, 2, 1, 31, 2, 2, 3)).setObjects(
    ("IF-MIB", "ifGeneralInformationGroup"),
    ("IF-MIB", "linkUpDownNotificationsGroup"),
    ("IF-MIB", "ifFixedLengthGroup"),
    ("IF-MIB", "ifHCFixedLengthGroup"),
    ("IF-MIB", "ifPacketGroup"),
    ("IF-MIB", "ifHCPacketGroup"),
    ("IF-MIB", "ifVHCPacketGroup"),
    ("IF-MIB", "ifCounterDiscontinuityGroup"),
    ("IF-MIB", "ifRcvAddressGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifCompliance3 = ifCompliance3.setStatus("current")
ifGeneralInformationGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 10)).setObjects(
    ("IF-MIB", "ifIndex"),
    ("IF-MIB", "ifDescr"),
    ("IF-MIB", "ifType"),
    ("IF-MIB", "ifSpeed"),
    ("IF-MIB", "ifPhysAddress"),
    ("IF-MIB", "ifAdminStatus"),
    ("IF-MIB", "ifOperStatus"),
    ("IF-MIB", "ifLastChange"),
    ("IF-MIB", "ifLinkUpDownTrapEnable"),
    ("IF-MIB", "ifConnectorPresent"),
    ("IF-MIB", "ifHighSpeed"),
    ("IF-MIB", "ifName"),
    ("IF-MIB", "ifNumber"),
    ("IF-MIB", "ifAlias"),
    ("IF-MIB", "ifTableLastChange"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifGeneralInformationGroup = ifGeneralInformationGroup.setStatus("current")
ifFixedLengthGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 2)).setObjects(
    ("IF-MIB", "ifInOctets"),
    ("IF-MIB", "ifOutOctets"),
    ("IF-MIB", "ifInUnknownProtos"),
    ("IF-MIB", "ifInErrors"),
    ("IF-MIB", "ifOutErrors"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifFixedLengthGroup = ifFixedLengthGroup.setStatus("current")
ifHCFixedLengthGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 3)).setObjects(
    ("IF-MIB", "ifHCInOctets"),
    ("IF-MIB", "ifHCOutOctets"),
    ("IF-MIB", "ifInOctets"),
    ("IF-MIB", "ifOutOctets"),
    ("IF-MIB", "ifInUnknownProtos"),
    ("IF-MIB", "ifInErrors"),
    ("IF-MIB", "ifOutErrors"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifHCFixedLengthGroup = ifHCFixedLengthGroup.setStatus("current")
ifPacketGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 4)).setObjects(
    ("IF-MIB", "ifInOctets"),
    ("IF-MIB", "ifOutOctets"),
    ("IF-MIB", "ifInUnknownProtos"),
    ("IF-MIB", "ifInErrors"),
    ("IF-MIB", "ifOutErrors"),
    ("IF-MIB", "ifMtu"),
    ("IF-MIB", "ifInUcastPkts"),
    ("IF-MIB", "ifInMulticastPkts"),
    ("IF-MIB", "ifInBroadcastPkts"),
    ("IF-MIB", "ifInDiscards"),
    ("IF-MIB", "ifOutUcastPkts"),
    ("IF-MIB", "ifOutMulticastPkts"),
    ("IF-MIB", "ifOutBroadcastPkts"),
    ("IF-MIB", "ifOutDiscards"),
    ("IF-MIB", "ifPromiscuousMode"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifPacketGroup = ifPacketGroup.setStatus("current")
ifHCPacketGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 5)).setObjects(
    ("IF-MIB", "ifHCInOctets"),
    ("IF-MIB", "ifHCOutOctets"),
    ("IF-MIB", "ifInOctets"),
    ("IF-MIB", "ifOutOctets"),
    ("IF-MIB", "ifInUnknownProtos"),
    ("IF-MIB", "ifInErrors"),
    ("IF-MIB", "ifOutErrors"),
    ("IF-MIB", "ifMtu"),
    ("IF-MIB", "ifInUcastPkts"),
    ("IF-MIB", "ifInMulticastPkts"),
    ("IF-MIB", "ifInBroadcastPkts"),
    ("IF-MIB", "ifInDiscards"),
    ("IF-MIB", "ifOutUcastPkts"),
    ("IF-MIB", "ifOutMulticastPkts"),
    ("IF-MIB", "ifOutBroadcastPkts"),
    ("IF-MIB", "ifOutDiscards"),
    ("IF-MIB", "ifPromiscuousMode"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifHCPacketGroup = ifHCPacketGroup.setStatus("current")
ifVHCPacketGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 6)).setObjects(
    ("IF-MIB", "ifHCInUcastPkts"),
    ("IF-MIB", "ifHCInMulticastPkts"),
    ("IF-MIB", "ifHCInBroadcastPkts"),
    ("IF-MIB", "ifHCOutUcastPkts"),
    ("IF-MIB", "ifHCOutMulticastPkts"),
    ("IF-MIB", "ifHCOutBroadcastPkts"),
    ("IF-MIB", "ifHCInOctets"),
    ("IF-MIB", "ifHCOutOctets"),
    ("IF-MIB", "ifInOctets"),
    ("IF-MIB", "ifOutOctets"),
    ("IF-MIB", "ifInUnknownProtos"),
    ("IF-MIB", "ifInErrors"),
    ("IF-MIB", "ifOutErrors"),
    ("IF-MIB", "ifMtu"),
    ("IF-MIB", "ifInUcastPkts"),
    ("IF-MIB", "ifInMulticastPkts"),
    ("IF-MIB", "ifInBroadcastPkts"),
    ("IF-MIB", "ifInDiscards"),
    ("IF-MIB", "ifOutUcastPkts"),
    ("IF-MIB", "ifOutMulticastPkts"),
    ("IF-MIB", "ifOutBroadcastPkts"),
    ("IF-MIB", "ifOutDiscards"),
    ("IF-MIB", "ifPromiscuousMode"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifVHCPacketGroup = ifVHCPacketGroup.setStatus("current")
ifRcvAddressGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 7)).setObjects(
    ("IF-MIB", "ifRcvAddressStatus"), ("IF-MIB", "ifRcvAddressType")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifRcvAddressGroup = ifRcvAddressGroup.setStatus("current")
ifStackGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 11)).setObjects(
    ("IF-MIB", "ifStackStatus"), ("IF-MIB", "ifStackLastChange")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifStackGroup2 = ifStackGroup2.setStatus("current")
ifCounterDiscontinuityGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 13)).setObjects(
    ("IF-MIB", "ifCounterDiscontinuityTime")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifCounterDiscontinuityGroup = ifCounterDiscontinuityGroup.setStatus("current")
linkUpDownNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 31, 2, 1, 14)
).setObjects(("IF-MIB", "linkUp"), ("IF-MIB", "linkDown"))
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    linkUpDownNotificationsGroup = linkUpDownNotificationsGroup.setStatus("current")
ifTestTable = MibTable(
    (1, 3, 6, 1, 2, 1, 31, 1, 3),
)
if mibBuilder.loadTexts:
    ifTestTable.setStatus("deprecated")
ifTestEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1),
)
ifEntry.registerAugmentions(("IF-MIB", "ifTestEntry"))
ifTestEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts:
    ifTestEntry.setStatus("deprecated")
ifTestId = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 1), TestAndIncr()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    ifTestId.setStatus("deprecated")
ifTestStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 2),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("notInUse", 1), ("inUse", 2))),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    ifTestStatus.setStatus("deprecated")
ifTestType = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 3), AutonomousType()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    ifTestType.setStatus("deprecated")
ifTestResult = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 4),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7)))
    .clone(
        namedValues=NamedValues(
            ("none", 1),
            ("success", 2),
            ("inProgress", 3),
            ("notSupported", 4),
            ("unAbleToRun", 5),
            ("aborted", 6),
            ("failed", 7),
        )
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifTestResult.setStatus("deprecated")
ifTestCode = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 5), ObjectIdentifier()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    ifTestCode.setStatus("deprecated")
ifTestOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 31, 1, 3, 1, 6), OwnerString()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    ifTestOwner.setStatus("deprecated")
ifGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 1)).setObjects(
    ("IF-MIB", "ifDescr"),
    ("IF-MIB", "ifType"),
    ("IF-MIB", "ifSpeed"),
    ("IF-MIB", "ifPhysAddress"),
    ("IF-MIB", "ifAdminStatus"),
    ("IF-MIB", "ifOperStatus"),
    ("IF-MIB", "ifLastChange"),
    ("IF-MIB", "ifLinkUpDownTrapEnable"),
    ("IF-MIB", "ifConnectorPresent"),
    ("IF-MIB", "ifHighSpeed"),
    ("IF-MIB", "ifName"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifGeneralGroup = ifGeneralGroup.setStatus("deprecated")
ifTestGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 8)).setObjects(
    ("IF-MIB", "ifTestId"),
    ("IF-MIB", "ifTestStatus"),
    ("IF-MIB", "ifTestType"),
    ("IF-MIB", "ifTestResult"),
    ("IF-MIB", "ifTestCode"),
    ("IF-MIB", "ifTestOwner"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifTestGroup = ifTestGroup.setStatus("deprecated")
ifStackGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 9)).setObjects(
    ("IF-MIB", "ifStackStatus")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifStackGroup = ifStackGroup.setStatus("deprecated")
ifOldObjectsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 31, 2, 1, 12)).setObjects(
    ("IF-MIB", "ifInNUcastPkts"),
    ("IF-MIB", "ifOutNUcastPkts"),
    ("IF-MIB", "ifOutQLen"),
    ("IF-MIB", "ifSpecific"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifOldObjectsGroup = ifOldObjectsGroup.setStatus("deprecated")
ifCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 31, 2, 2, 1)).setObjects(
    ("IF-MIB", "ifGeneralGroup"),
    ("IF-MIB", "ifStackGroup"),
    ("IF-MIB", "ifFixedLengthGroup"),
    ("IF-MIB", "ifHCFixedLengthGroup"),
    ("IF-MIB", "ifPacketGroup"),
    ("IF-MIB", "ifHCPacketGroup"),
    ("IF-MIB", "ifTestGroup"),
    ("IF-MIB", "ifRcvAddressGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifCompliance = ifCompliance.setStatus("deprecated")
ifCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 31, 2, 2, 2)).setObjects(
    ("IF-MIB", "ifGeneralInformationGroup"),
    ("IF-MIB", "ifStackGroup2"),
    ("IF-MIB", "ifCounterDiscontinuityGroup"),
    ("IF-MIB", "ifFixedLengthGroup"),
    ("IF-MIB", "ifHCFixedLengthGroup"),
    ("IF-MIB", "ifPacketGroup"),
    ("IF-MIB", "ifHCPacketGroup"),
    ("IF-MIB", "ifRcvAddressGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    ifCompliance2 = ifCompliance2.setStatus("deprecated")
mibBuilder.exportSymbols(
    "IF-MIB",
    ifFixedLengthGroup=ifFixedLengthGroup,
    ifHCInOctets=ifHCInOctets,
    ifMtu=ifMtu,
    ifInOctets=ifInOctets,
    ifCompliances=ifCompliances,
    ifXTable=ifXTable,
    ifSpecific=ifSpecific,
    ifTestId=ifTestId,
    ifStackTable=ifStackTable,
    ifCounterDiscontinuityGroup=ifCounterDiscontinuityGroup,
    ifDescr=ifDescr,
    ifHCOutMulticastPkts=ifHCOutMulticastPkts,
    ifStackStatus=ifStackStatus,
    ifOutDiscards=ifOutDiscards,
    ifConformance=ifConformance,
    ifHCInMulticastPkts=ifHCInMulticastPkts,
    ifTestTable=ifTestTable,
    ifOutMulticastPkts=ifOutMulticastPkts,
    ifHighSpeed=ifHighSpeed,
    ifInBroadcastPkts=ifInBroadcastPkts,
    linkUpDownNotificationsGroup=linkUpDownNotificationsGroup,
    ifStackGroup=ifStackGroup,
    ifOutOctets=ifOutOctets,
    ifInMulticastPkts=ifInMulticastPkts,
    ifAlias=ifAlias,
    ifRcvAddressAddress=ifRcvAddressAddress,
    ifIndex=ifIndex,
    linkDown=linkDown,
    ifCompliance2=ifCompliance2,
    ifMIBObjects=ifMIBObjects,
    ifName=ifName,
    ifCompliance3=ifCompliance3,
    ifHCInUcastPkts=ifHCInUcastPkts,
    ifOutUcastPkts=ifOutUcastPkts,
    ifTestEntry=ifTestEntry,
    ifOldObjectsGroup=ifOldObjectsGroup,
    ifNumber=ifNumber,
    ifStackHigherLayer=ifStackHigherLayer,
    ifGroups=ifGroups,
    ifTableLastChange=ifTableLastChange,
    ifPhysAddress=ifPhysAddress,
    ifTable=ifTable,
    ifSpeed=ifSpeed,
    ifInUcastPkts=ifInUcastPkts,
    ifInErrors=ifInErrors,
    ifRcvAddressType=ifRcvAddressType,
    ifGeneralInformationGroup=ifGeneralInformationGroup,
    ifPacketGroup=ifPacketGroup,
    ifOutErrors=ifOutErrors,
    ifRcvAddressGroup=ifRcvAddressGroup,
    ifOutQLen=ifOutQLen,
    ifCompliance=ifCompliance,
    PYSNMP_MODULE_ID=ifMIB,
    ifVHCPacketGroup=ifVHCPacketGroup,
    ifHCOutBroadcastPkts=ifHCOutBroadcastPkts,
    ifGeneralGroup=ifGeneralGroup,
    ifInNUcastPkts=ifInNUcastPkts,
    interfaces=interfaces,
    ifOutBroadcastPkts=ifOutBroadcastPkts,
    ifTestStatus=ifTestStatus,
    ifHCInBroadcastPkts=ifHCInBroadcastPkts,
    ifEntry=ifEntry,
    ifLinkUpDownTrapEnable=ifLinkUpDownTrapEnable,
    OwnerString=OwnerString,
    ifRcvAddressTable=ifRcvAddressTable,
    ifType=ifType,
    ifTestResult=ifTestResult,
    ifTestType=ifTestType,
    ifOperStatus=ifOperStatus,
    ifStackLastChange=ifStackLastChange,
    ifInDiscards=ifInDiscards,
    ifHCOutUcastPkts=ifHCOutUcastPkts,
    ifRcvAddressEntry=ifRcvAddressEntry,
    InterfaceIndex=InterfaceIndex,
    ifOutNUcastPkts=ifOutNUcastPkts,
    ifStackLowerLayer=ifStackLowerLayer,
    ifCounterDiscontinuityTime=ifCounterDiscontinuityTime,
    ifHCFixedLengthGroup=ifHCFixedLengthGroup,
    ifAdminStatus=ifAdminStatus,
    ifPromiscuousMode=ifPromiscuousMode,
    ifStackEntry=ifStackEntry,
    InterfaceIndexOrZero=InterfaceIndexOrZero,
    ifHCPacketGroup=ifHCPacketGroup,
    ifStackGroup2=ifStackGroup2,
    ifLastChange=ifLastChange,
    ifInUnknownProtos=ifInUnknownProtos,
    ifMIB=ifMIB,
    ifHCOutOctets=ifHCOutOctets,
    ifConnectorPresent=ifConnectorPresent,
    ifRcvAddressStatus=ifRcvAddressStatus,
    ifTestOwner=ifTestOwner,
    linkUp=linkUp,
    ifXEntry=ifXEntry,
    ifTestGroup=ifTestGroup,
    ifTestCode=ifTestCode,
)
