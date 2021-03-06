#
# PySNMP MIB module CISCO-VTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///mibs.thola.io/asn1/CISCO-VTP-MIB
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
(Cisco2KVlanList,) = mibBuilder.importSymbols("CISCO-TC", "Cisco2KVlanList")
InterfaceIndexOrZero, ifIndex, InterfaceIndex = mibBuilder.importSymbols(
    "IF-MIB", "InterfaceIndexOrZero", "ifIndex", "InterfaceIndex"
)
InetAddressType, InetAddress = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB", "InetAddressType", "InetAddress"
)
(OwnerString,) = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
(SnmpAdminString,) = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols(
    "SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup"
)
(
    MibIdentifier,
    IpAddress,
    Gauge32,
    MibScalar,
    MibTable,
    MibTableRow,
    MibTableColumn,
    Counter64,
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
    "Gauge32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Counter64",
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
    TruthValue,
    DateAndTime,
    RowStatus,
) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TestAndIncr",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "DateAndTime",
    "RowStatus",
)
ciscoVtpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 46))
ciscoVtpMIB.setRevisions(
    (
        "2013-10-14 00:00",
        "2010-05-12 00:00",
        "2009-12-03 00:00",
        "2008-03-07 00:00",
        "2007-10-04 00:00",
        "2006-02-17 00:00",
        "2004-02-11 00:00",
        "2003-11-21 00:00",
        "2003-08-08 00:00",
        "2003-07-11 00:00",
        "2003-04-16 00:00",
        "2002-04-10 00:00",
        "2002-02-28 00:00",
        "2001-08-03 00:00",
        "2001-02-26 00:00",
        "2001-02-12 00:00",
        "2000-09-19 00:00",
        "2000-04-10 00:00",
        "2000-01-06 00:00",
        "1999-02-25 11:30",
        "1999-01-05 11:30",
        "1998-05-19 11:30",
        "1997-08-08 11:38",
        "1997-05-09 11:30",
        "1997-02-24 11:15",
        "1997-01-27 17:30",
        "1996-09-16 12:30",
        "1996-07-17 12:30",
        "1996-01-18 18:20",
    )
)
if mibBuilder.loadTexts:
    ciscoVtpMIB.setLastUpdated("201310140000Z")
if mibBuilder.loadTexts:
    ciscoVtpMIB.setOrganization("Cisco Systems, Inc.")
vtpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1))


class VlanIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)


class ManagementDomainIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)


class VlanType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(
        SingleValueConstraint(1, 2, 3, 4, 5, 6)
    )
    namedValues = NamedValues(
        ("ethernet", 1),
        ("fddi", 2),
        ("tokenRing", 3),
        ("fddiNet", 4),
        ("trNet", 5),
        ("deprecated", 6),
    )


class VlanTypeExt(TextualConvention, Bits):
    reference = "RFC2674."
    status = "current"
    namedValues = NamedValues(
        ("vtpmanageable", 0),
        ("internal", 1),
        ("reserved", 2),
        ("rspan", 3),
        ("dynamicGvrp", 4),
    )


vtpStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1))
vtpVersion = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1, 1),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4)))
    .clone(namedValues=NamedValues(("one", 1), ("two", 2), ("none", 3), ("three", 4))),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVersion.setStatus("current")
vtpMaxVlanStorage = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 1023)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpMaxVlanStorage.setStatus("current")
vtpNotificationsEnabled = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1, 3), TruthValue()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpNotificationsEnabled.setStatus("current")
vtpVlanCreatedNotifEnabled = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1, 4), TruthValue()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpVlanCreatedNotifEnabled.setStatus("current")
vtpVlanDeletedNotifEnabled = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1, 5), TruthValue()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpVlanDeletedNotifEnabled.setStatus("current")
vlanManagementDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2))
managementDomainTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1),
)
if mibBuilder.loadTexts:
    managementDomainTable.setStatus("current")
managementDomainEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1),
).setIndexNames((0, "CISCO-VTP-MIB", "managementDomainIndex"))
if mibBuilder.loadTexts:
    managementDomainEntry.setStatus("current")
managementDomainIndex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 1), ManagementDomainIndex()
)
if mibBuilder.loadTexts:
    managementDomainIndex.setStatus("current")
managementDomainName = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 2),
    DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    managementDomainName.setStatus("current")
managementDomainLocalMode = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4)))
    .clone(
        namedValues=NamedValues(
            ("client", 1), ("server", 2), ("transparent", 3), ("off", 4)
        )
    ),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    managementDomainLocalMode.setStatus("current")
managementDomainConfigRevNumber = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 4), Gauge32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    managementDomainConfigRevNumber.setStatus("current")
managementDomainLastUpdater = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 5), IpAddress()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    managementDomainLastUpdater.setStatus("current")
managementDomainLastChange = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 6), DateAndTime()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    managementDomainLastChange.setStatus("current")
managementDomainRowStatus = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 7), RowStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    managementDomainRowStatus.setStatus("current")
managementDomainTftpServer = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 8), IpAddress()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    managementDomainTftpServer.setStatus("current")
managementDomainTftpPathname = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 9), DisplayString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    managementDomainTftpPathname.setStatus("current")
managementDomainPruningState = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 10),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    managementDomainPruningState.setStatus("current")
managementDomainVersionInUse = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 11),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4)))
    .clone(
        namedValues=NamedValues(
            ("version1", 1), ("version2", 2), ("none", 3), ("version3", 4)
        )
    ),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    managementDomainVersionInUse.setStatus("current")
managementDomainPruningStateOper = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 12),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    managementDomainPruningStateOper.setStatus("current")
managementDomainAdminSrcIf = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 13), SnmpAdminString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    managementDomainAdminSrcIf.setStatus("current")
managementDomainSourceOnlyMode = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 14), TruthValue().clone("false")
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    managementDomainSourceOnlyMode.setStatus("current")
managementDomainOperSrcIf = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 15), SnmpAdminString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    managementDomainOperSrcIf.setStatus("current")
managementDomainConfigFile = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 16), SnmpAdminString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    managementDomainConfigFile.setStatus("current")
managementDomainLocalUpdaterType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 17), InetAddressType()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    managementDomainLocalUpdaterType.setStatus("current")
managementDomainLocalUpdater = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 18), InetAddress()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    managementDomainLocalUpdater.setStatus("current")
managementDomainDeviceID = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 19), SnmpAdminString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    managementDomainDeviceID.setStatus("current")
vlanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3))
vtpVlanTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1),
)
if mibBuilder.loadTexts:
    vtpVlanTable.setStatus("current")
vtpVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1),).setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"), (0, "CISCO-VTP-MIB", "vtpVlanIndex")
)
if mibBuilder.loadTexts:
    vtpVlanEntry.setStatus("current")
vtpVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 1), VlanIndex())
if mibBuilder.loadTexts:
    vtpVlanIndex.setStatus("current")
vtpVlanState = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 2),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4)))
    .clone(
        namedValues=NamedValues(
            ("operational", 1),
            ("suspended", 2),
            ("mtuTooBigForDevice", 3),
            ("mtuTooBigForTrunk", 4),
        )
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanState.setStatus("current")
vtpVlanType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 3), VlanType()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanType.setStatus("current")
vtpVlanName = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 4),
    DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanName.setStatus("current")
vtpVlanMtu = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 5),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1500, 18190)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanMtu.setStatus("current")
vtpVlanDot10Said = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 6),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanDot10Said.setStatus("current")
vtpVlanRingNumber = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 7),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanRingNumber.setStatus("current")
vtpVlanBridgeNumber = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 8),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanBridgeNumber.setStatus("current")
vtpVlanStpType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 9),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(namedValues=NamedValues(("ieee", 1), ("ibm", 2), ("hybrid", 3))),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanStpType.setStatus("current")
vtpVlanParentVlan = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 10), VlanIndex()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanParentVlan.setStatus("current")
vtpVlanTranslationalVlan1 = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 11), VlanIndex()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanTranslationalVlan1.setStatus("current")
vtpVlanTranslationalVlan2 = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 12), VlanIndex()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanTranslationalVlan2.setStatus("current")
vtpVlanBridgeType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 13),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("srt", 1), ("srb", 2))),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanBridgeType.setStatus("current")
vtpVlanAreHopCount = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 14),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanAreHopCount.setStatus("current")
vtpVlanSteHopCount = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 15),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanSteHopCount.setStatus("current")
vtpVlanIsCRFBackup = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 16), TruthValue()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanIsCRFBackup.setStatus("current")
vtpVlanTypeExt = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 17), VlanTypeExt()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanTypeExt.setStatus("current")
vtpVlanIfIndex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 18), InterfaceIndexOrZero()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanIfIndex.setStatus("current")
internalVlanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 2))
vtpInternalVlanAllocPolicy = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 2, 1),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("ascending", 1), ("descending", 2))),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpInternalVlanAllocPolicy.setStatus("current")
vtpInternalVlanTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 2, 2),
)
if mibBuilder.loadTexts:
    vtpInternalVlanTable.setStatus("current")
vtpInternalVlanEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 2, 2, 1),
).setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"), (0, "CISCO-VTP-MIB", "vtpVlanIndex")
)
if mibBuilder.loadTexts:
    vtpInternalVlanEntry.setStatus("current")
vtpInternalVlanOwner = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 2, 2, 1, 1), SnmpAdminString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpInternalVlanOwner.setStatus("current")
vlanEdit = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4))
vtpEditControlTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1),
)
if mibBuilder.loadTexts:
    vtpEditControlTable.setStatus("current")
vtpEditControlEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1),
)
managementDomainEntry.registerAugmentions(("CISCO-VTP-MIB", "vtpEditControlEntry"))
vtpEditControlEntry.setIndexNames(*managementDomainEntry.getIndexNames())
if mibBuilder.loadTexts:
    vtpEditControlEntry.setStatus("current")
vtpVlanEditOperation = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1, 1),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5)))
    .clone(
        namedValues=NamedValues(
            ("none", 1), ("copy", 2), ("apply", 3), ("release", 4), ("restartTimer", 5)
        )
    ),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditOperation.setStatus("current")
vtpVlanApplyStatus = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1, 2),
    Integer32()
    .subtype(
        subtypeSpec=ConstraintsUnion(
            SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        )
    )
    .clone(
        namedValues=NamedValues(
            ("inProgress", 1),
            ("succeeded", 2),
            ("configNumberError", 3),
            ("inconsistentEdit", 4),
            ("tooBig", 5),
            ("localNVStoreFail", 6),
            ("remoteNVStoreFail", 7),
            ("editBufferEmpty", 8),
            ("someOtherError", 9),
            ("notPrimaryServer", 10),
        )
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanApplyStatus.setStatus("current")
vtpVlanEditBufferOwner = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1, 3), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditBufferOwner.setStatus("current")
vtpVlanEditConfigRevNumber = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1, 4), Gauge32()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditConfigRevNumber.setStatus("current")
vtpVlanEditModifiedVlan = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1, 5), VlanIndex()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanEditModifiedVlan.setStatus("current")
vtpVlanEditTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2),
)
if mibBuilder.loadTexts:
    vtpVlanEditTable.setStatus("current")
vtpVlanEditEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1),).setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
    (0, "CISCO-VTP-MIB", "vtpVlanEditIndex"),
)
if mibBuilder.loadTexts:
    vtpVlanEditEntry.setStatus("current")
vtpVlanEditIndex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 1), VlanIndex()
)
if mibBuilder.loadTexts:
    vtpVlanEditIndex.setStatus("current")
vtpVlanEditState = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 2),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("operational", 1), ("suspended", 2)))
    .clone("operational"),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditState.setStatus("current")
vtpVlanEditType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 3), VlanType().clone("ethernet")
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditType.setStatus("current")
vtpVlanEditName = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 4),
    DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditName.setStatus("current")
vtpVlanEditMtu = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 5),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1500, 18190)).clone(1500),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditMtu.setStatus("current")
vtpVlanEditDot10Said = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 6),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditDot10Said.setStatus("current")
vtpVlanEditRingNumber = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 7),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditRingNumber.setStatus("current")
vtpVlanEditBridgeNumber = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 8),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditBridgeNumber.setStatus("current")
vtpVlanEditStpType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 9),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(namedValues=NamedValues(("ieee", 1), ("ibm", 2), ("auto", 3))),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditStpType.setStatus("current")
vtpVlanEditParentVlan = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 10), VlanIndex()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditParentVlan.setStatus("current")
vtpVlanEditRowStatus = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 11), RowStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditRowStatus.setStatus("current")
vtpVlanEditTranslationalVlan1 = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 12), VlanIndex()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditTranslationalVlan1.setStatus("current")
vtpVlanEditTranslationalVlan2 = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 13), VlanIndex()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditTranslationalVlan2.setStatus("current")
vtpVlanEditBridgeType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 14),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("srt", 1), ("srb", 2))),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditBridgeType.setStatus("current")
vtpVlanEditAreHopCount = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 15),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditAreHopCount.setStatus("current")
vtpVlanEditSteHopCount = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 16),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 13)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditSteHopCount.setStatus("current")
vtpVlanEditIsCRFBackup = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 17), TruthValue()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditIsCRFBackup.setStatus("current")
vtpVlanEditTypeExt = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 18), VlanTypeExt()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpVlanEditTypeExt.setStatus("deprecated")
vtpVlanEditTypeExt2 = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 19), VlanTypeExt()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlanEditTypeExt2.setStatus("current")
vtpVlanLocalShutdownTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 3),
)
if mibBuilder.loadTexts:
    vtpVlanLocalShutdownTable.setStatus("current")
vtpVlanLocalShutdownEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 3, 1),
).setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"), (0, "CISCO-VTP-MIB", "vtpVlanIndex")
)
if mibBuilder.loadTexts:
    vtpVlanLocalShutdownEntry.setStatus("current")
vtpVlanLocalShutdown = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 3, 1, 1),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("up", 1), ("down", 2))),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpVlanLocalShutdown.setStatus("current")
vtpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5))
vtpStatsTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1),
)
if mibBuilder.loadTexts:
    vtpStatsTable.setStatus("current")
vtpStatsEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1),
)
managementDomainEntry.registerAugmentions(("CISCO-VTP-MIB", "vtpStatsEntry"))
vtpStatsEntry.setIndexNames(*managementDomainEntry.getIndexNames())
if mibBuilder.loadTexts:
    vtpStatsEntry.setStatus("current")
vtpInSummaryAdverts = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 1), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpInSummaryAdverts.setStatus("current")
vtpInSubsetAdverts = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 2), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpInSubsetAdverts.setStatus("current")
vtpInAdvertRequests = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 3), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpInAdvertRequests.setStatus("current")
vtpOutSummaryAdverts = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 4), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpOutSummaryAdverts.setStatus("current")
vtpOutSubsetAdverts = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 5), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpOutSubsetAdverts.setStatus("current")
vtpOutAdvertRequests = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 6), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpOutAdvertRequests.setStatus("current")
vtpConfigRevNumberErrors = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 7), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpConfigRevNumberErrors.setStatus("current")
vtpConfigDigestErrors = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 8), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpConfigDigestErrors.setStatus("current")
vlanTrunkPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6))
vlanTrunkPortTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1),
)
if mibBuilder.loadTexts:
    vlanTrunkPortTable.setStatus("current")
vlanTrunkPortEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1),
).setIndexNames((0, "CISCO-VTP-MIB", "vlanTrunkPortIfIndex"))
if mibBuilder.loadTexts:
    vlanTrunkPortEntry.setStatus("current")
vlanTrunkPortIfIndex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 1), InterfaceIndex()
)
if mibBuilder.loadTexts:
    vlanTrunkPortIfIndex.setStatus("current")
vlanTrunkPortManagementDomain = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 2), ManagementDomainIndex()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortManagementDomain.setStatus("current")
vlanTrunkPortEncapsulationType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5)))
    .clone(
        namedValues=NamedValues(
            ("isl", 1), ("dot10", 2), ("lane", 3), ("dot1Q", 4), ("negotiate", 5)
        )
    ),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortEncapsulationType.setStatus("current")
vlanTrunkPortVlansEnabled = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 4),
    OctetString()
    .subtype(subtypeSpec=ValueSizeConstraint(128, 128))
    .setFixedLength(128),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansEnabled.setStatus("current")
vlanTrunkPortNativeVlan = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 5), VlanIndex()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortNativeVlan.setStatus("current")
vlanTrunkPortRowStatus = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 6), RowStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortRowStatus.setStatus("current")
vlanTrunkPortInJoins = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 7), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortInJoins.setStatus("current")
vlanTrunkPortOutJoins = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 8), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortOutJoins.setStatus("current")
vlanTrunkPortOldAdverts = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 9), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortOldAdverts.setStatus("current")
vlanTrunkPortVlansPruningEligible = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 10),
    OctetString()
    .subtype(subtypeSpec=ValueSizeConstraint(128, 128))
    .setFixedLength(128),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansPruningEligible.setStatus("current")
vlanTrunkPortVlansXmitJoined = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 11),
    OctetString()
    .subtype(subtypeSpec=ValueSizeConstraint(128, 128))
    .setFixedLength(128),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansXmitJoined.setStatus("current")
vlanTrunkPortVlansRcvJoined = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 12),
    OctetString()
    .subtype(subtypeSpec=ValueSizeConstraint(128, 128))
    .setFixedLength(128),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansRcvJoined.setStatus("current")
vlanTrunkPortDynamicState = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 13),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5)))
    .clone(
        namedValues=NamedValues(
            ("on", 1), ("off", 2), ("desirable", 3), ("auto", 4), ("onNoNegotiate", 5)
        )
    ),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortDynamicState.setStatus("current")
vlanTrunkPortDynamicStatus = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 14),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("trunking", 1), ("notTrunking", 2))),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortDynamicStatus.setStatus("current")
vlanTrunkPortVtpEnabled = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 15), TruthValue()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortVtpEnabled.setStatus("current")
vlanTrunkPortEncapsulationOperType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 16),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6)))
    .clone(
        namedValues=NamedValues(
            ("isl", 1),
            ("dot10", 2),
            ("lane", 3),
            ("dot1Q", 4),
            ("negotiating", 5),
            ("notApplicable", 6),
        )
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortEncapsulationOperType.setStatus("current")
vlanTrunkPortVlansEnabled2k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 17),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansEnabled2k.setStatus("current")
vlanTrunkPortVlansEnabled3k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 18),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansEnabled3k.setStatus("current")
vlanTrunkPortVlansEnabled4k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 19),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansEnabled4k.setStatus("current")
vtpVlansPruningEligible2k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 20),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlansPruningEligible2k.setStatus("current")
vtpVlansPruningEligible3k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 21),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlansPruningEligible3k.setStatus("current")
vtpVlansPruningEligible4k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 22),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vtpVlansPruningEligible4k.setStatus("current")
vlanTrunkPortVlansXmitJoined2k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 23),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansXmitJoined2k.setStatus("current")
vlanTrunkPortVlansXmitJoined3k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 24),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansXmitJoined3k.setStatus("current")
vlanTrunkPortVlansXmitJoined4k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 25),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansXmitJoined4k.setStatus("current")
vlanTrunkPortVlansRcvJoined2k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 26),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansRcvJoined2k.setStatus("current")
vlanTrunkPortVlansRcvJoined3k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 27),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansRcvJoined3k.setStatus("current")
vlanTrunkPortVlansRcvJoined4k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 28),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansRcvJoined4k.setStatus("current")
vlanTrunkPortDot1qTunnel = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 29),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(namedValues=NamedValues(("trunk", 1), ("access", 2), ("disabled", 3)))
    .clone("disabled"),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    vlanTrunkPortDot1qTunnel.setStatus("deprecated")
vlanTrunkPortVlansActiveFirst2k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 30), Cisco2KVlanList()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansActiveFirst2k.setStatus("current")
vlanTrunkPortVlansActiveSecond2k = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 31), Cisco2KVlanList()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansActiveSecond2k.setStatus("current")
vlanTrunkPortSetSerialNo = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 2), TestAndIncr()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vlanTrunkPortSetSerialNo.setStatus("current")
vlanTrunkPortsDot1qTag = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 3), TruthValue().clone("false")
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vlanTrunkPortsDot1qTag.setStatus("deprecated")
vtpDiscover = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7))
vtpDiscoverTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 1),
)
if mibBuilder.loadTexts:
    vtpDiscoverTable.setStatus("current")
vtpDiscoverEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 1, 1),
).setIndexNames((0, "CISCO-VTP-MIB", "managementDomainIndex"))
if mibBuilder.loadTexts:
    vtpDiscoverEntry.setStatus("current")
vtpDiscoverAction = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 1, 1, 1),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(
        namedValues=NamedValues(("discover", 1), ("noOperation", 2), ("purgeResult", 3))
    ),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpDiscoverAction.setStatus("current")
vtpDiscoverStatus = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 1, 1, 2),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4)))
    .clone(
        namedValues=NamedValues(
            ("inProgress", 1),
            ("succeeded", 2),
            ("resourceUnavailable", 3),
            ("someOtherError", 4),
        )
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDiscoverStatus.setStatus("current")
vtpLastDiscoverTime = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 1, 1, 3), TimeStamp()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpLastDiscoverTime.setStatus("current")
vtpDiscoverResultTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2),
)
if mibBuilder.loadTexts:
    vtpDiscoverResultTable.setStatus("current")
vtpDiscoverResultEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1),
).setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
    (0, "CISCO-VTP-MIB", "vtpDiscoverResultIndex"),
)
if mibBuilder.loadTexts:
    vtpDiscoverResultEntry.setStatus("current")
vtpDiscoverResultIndex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 1), Unsigned32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDiscoverResultIndex.setStatus("current")
vtpDiscoverResultDatabaseName = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 2),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDiscoverResultDatabaseName.setStatus("current")
vtpDiscoverResultConflicting = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 3), TruthValue()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDiscoverResultConflicting.setStatus("current")
vtpDiscoverResultDeviceId = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 4),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDiscoverResultDeviceId.setStatus("current")
vtpDiscoverResultPrimaryServer = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 5),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDiscoverResultPrimaryServer.setStatus("current")
vtpDiscoverResultRevNumber = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 6), Gauge32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDiscoverResultRevNumber.setStatus("current")
vtpDiscoverResultSystemName = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 7),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDiscoverResultSystemName.setStatus("current")
vtpDatabase = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8))
vtpDatabaseTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1),
)
if mibBuilder.loadTexts:
    vtpDatabaseTable.setStatus("current")
vtpDatabaseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1),).setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
    (0, "CISCO-VTP-MIB", "vtpDatabaseIndex"),
)
if mibBuilder.loadTexts:
    vtpDatabaseEntry.setStatus("current")
vtpDatabaseIndex = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 1), Unsigned32()
)
if mibBuilder.loadTexts:
    vtpDatabaseIndex.setStatus("current")
vtpDatabaseName = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 2),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDatabaseName.setStatus("current")
vtpDatabaseLocalMode = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4)))
    .clone(
        namedValues=NamedValues(
            ("client", 1), ("server", 2), ("transparent", 3), ("off", 4)
        )
    ),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpDatabaseLocalMode.setStatus("current")
vtpDatabaseRevNumber = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 4), Gauge32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDatabaseRevNumber.setStatus("current")
vtpDatabasePrimaryServer = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 5), TruthValue()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDatabasePrimaryServer.setStatus("current")
vtpDatabasePrimaryServerId = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 6),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vtpDatabasePrimaryServerId.setStatus("current")
vtpDatabaseTakeOverPrimary = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 7), TruthValue()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpDatabaseTakeOverPrimary.setStatus("current")
vtpDatabaseTakeOverPassword = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 8),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpDatabaseTakeOverPassword.setStatus("current")
vtpAuthentication = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9))
vtpAuthenticationTable = MibTable(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9, 1),
)
if mibBuilder.loadTexts:
    vtpAuthenticationTable.setStatus("current")
vtpAuthEntry = MibTableRow(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9, 1, 1),
).setIndexNames((0, "CISCO-VTP-MIB", "managementDomainIndex"))
if mibBuilder.loadTexts:
    vtpAuthEntry.setStatus("current")
vtpAuthPassword = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9, 1, 1, 1),
    SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpAuthPassword.setStatus("current")
vtpAuthPasswordType = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9, 1, 1, 2),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("plaintext", 1), ("hidden", 2))),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpAuthPasswordType.setStatus("current")
vtpAuthSecretKey = MibTableColumn(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9, 1, 1, 3),
    OctetString().subtype(
        subtypeSpec=ConstraintsUnion(
            ValueSizeConstraint(0, 0),
            ValueSizeConstraint(16, 16),
        )
    ),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    vtpAuthSecretKey.setStatus("current")
vlanStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 10))
vlanStatsVlans = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 10, 1), Unsigned32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanStatsVlans.setStatus("current")
vlanStatsExtendedVlans = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 10, 2), Unsigned32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanStatsExtendedVlans.setStatus("current")
vlanStatsInternalVlans = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 10, 3), Unsigned32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanStatsInternalVlans.setStatus("current")
vlanStatsFreeVlans = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 10, 4), Unsigned32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    vlanStatsFreeVlans.setStatus("current")
vtpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 2))
vtpNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0))
vtpNotificationsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 1))
vtpConfigRevNumberError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 1)
).setObjects(("CISCO-VTP-MIB", "managementDomainConfigRevNumber"))
if mibBuilder.loadTexts:
    vtpConfigRevNumberError.setStatus("current")
vtpConfigDigestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 2)
).setObjects(("CISCO-VTP-MIB", "managementDomainConfigRevNumber"))
if mibBuilder.loadTexts:
    vtpConfigDigestError.setStatus("current")
vtpServerDisabled = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 3)).setObjects(
    ("CISCO-VTP-MIB", "managementDomainConfigRevNumber"),
    ("CISCO-VTP-MIB", "vtpMaxVlanStorage"),
)
if mibBuilder.loadTexts:
    vtpServerDisabled.setStatus("current")
vtpMtuTooBig = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 4)).setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortManagementDomain"),
    ("CISCO-VTP-MIB", "vtpVlanState"),
)
if mibBuilder.loadTexts:
    vtpMtuTooBig.setStatus("current")
vtpVersionOneDeviceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 6)
).setObjects(("CISCO-VTP-MIB", "vlanTrunkPortManagementDomain"))
if mibBuilder.loadTexts:
    vtpVersionOneDeviceDetected.setStatus("current")
vlanTrunkPortDynamicStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 7)
).setObjects(("CISCO-VTP-MIB", "vlanTrunkPortDynamicStatus"))
if mibBuilder.loadTexts:
    vlanTrunkPortDynamicStatusChange.setStatus("current")
vtpLocalModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 8)
).setObjects(("CISCO-VTP-MIB", "managementDomainLocalMode"))
if mibBuilder.loadTexts:
    vtpLocalModeChanged.setStatus("current")
vtpVersionInUseChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 9)
).setObjects(("CISCO-VTP-MIB", "managementDomainVersionInUse"))
if mibBuilder.loadTexts:
    vtpVersionInUseChanged.setStatus("current")
vtpVlanCreated = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 10)).setObjects(
    ("CISCO-VTP-MIB", "vtpVlanName")
)
if mibBuilder.loadTexts:
    vtpVlanCreated.setStatus("current")
vtpVlanDeleted = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 11)).setObjects(
    ("CISCO-VTP-MIB", "vtpVlanName")
)
if mibBuilder.loadTexts:
    vtpVlanDeleted.setStatus("current")
vtpVlanRingNumberConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 12)
).setObjects(
    ("CISCO-VTP-MIB", "vtpVlanRingNumber"),
    ("IF-MIB", "ifIndex"),
    ("CISCO-VTP-MIB", "vtpVlanPortLocalSegment"),
)
if mibBuilder.loadTexts:
    vtpVlanRingNumberConflict.setStatus("current")
vtpPruningStateOperChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 13)
).setObjects(("CISCO-VTP-MIB", "managementDomainPruningStateOper"))
if mibBuilder.loadTexts:
    vtpPruningStateOperChange.setStatus("current")
vtpVlanPortLocalSegment = MibScalar(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)),
).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts:
    vtpVlanPortLocalSegment.setStatus("current")
vtpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 3))
vtpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1))
vtpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2))
vtpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 1)).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance = vtpMIBCompliance.setStatus("deprecated")
vtpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 2)).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance2 = vtpMIBCompliance2.setStatus("deprecated")
vtpMIBCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 3)).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroup"),
    ("CISCO-VTP-MIB", "vtpDot1qTunnelGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance3 = vtpMIBCompliance3.setStatus("deprecated")
vtpMIBCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 4)).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroup"),
    ("CISCO-VTP-MIB", "vtpDot1qTunnelGroup"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance4 = vtpMIBCompliance4.setStatus("deprecated")
vtpMIBCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 5)).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroup"),
    ("CISCO-VTP-MIB", "vtpDot1qTunnelGroup"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance5 = vtpMIBCompliance5.setStatus("deprecated")
vtpMIBCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 6)).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpDot1qTunnelGroup"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance6 = vtpMIBCompliance6.setStatus("deprecated")
vtpMIBCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 7)).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpDot1qTunnelGroup"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance7 = vtpMIBCompliance7.setStatus("deprecated")
vtpMIBCompliance8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 8)).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpDot1qTunnelGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance8 = vtpMIBCompliance8.setStatus("deprecated")
vtpMIBCompliance9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 9)).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanNotifEnabledGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance9 = vtpMIBCompliance9.setStatus("deprecated")
vtpMIBCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 10)
).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanNotifEnabledGroup"),
    ("CISCO-VTP-MIB", "vtpDiscoverGroup"),
    ("CISCO-VTP-MIB", "vtpDatabaseGroup"),
    ("CISCO-VTP-MIB", "vtpAuthGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance10 = vtpMIBCompliance10.setStatus("deprecated")
vtpMIBCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 11)
).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroupRev1"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanNotifEnabledGroup"),
    ("CISCO-VTP-MIB", "vtpDiscoverGroup"),
    ("CISCO-VTP-MIB", "vtpDatabaseGroup"),
    ("CISCO-VTP-MIB", "vtpAuthGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance11 = vtpMIBCompliance11.setStatus("deprecated")
vtpMIBCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 12)
).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroupRev1"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanNotifEnabledGroup"),
    ("CISCO-VTP-MIB", "vtpDiscoverGroup"),
    ("CISCO-VTP-MIB", "vtpDatabaseGroup"),
    ("CISCO-VTP-MIB", "vtpAuthGroup"),
    ("CISCO-VTP-MIB", "vtpInternalVlanGrp"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance12 = vtpMIBCompliance12.setStatus("deprecated")
vtpMIBCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 13)
).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroupRev1"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanNotifEnabledGroup"),
    ("CISCO-VTP-MIB", "vtpDiscoverGroup"),
    ("CISCO-VTP-MIB", "vtpDatabaseGroup"),
    ("CISCO-VTP-MIB", "vtpAuthGroup"),
    ("CISCO-VTP-MIB", "vtpInternalVlanGrp"),
    ("CISCO-VTP-MIB", "vlanStatsGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup6"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup7"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance13 = vtpMIBCompliance13.setStatus("deprecated")
vtpMIBCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 14)
).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroupRev1"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPruningGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPruningGroup2"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup3"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanNotifEnabledGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup2"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup3"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup4"),
    ("CISCO-VTP-MIB", "vtpDiscoverGroup"),
    ("CISCO-VTP-MIB", "vtpDatabaseGroup"),
    ("CISCO-VTP-MIB", "vtpAuthGroup"),
    ("CISCO-VTP-MIB", "vtpInternalVlanGrp"),
    ("CISCO-VTP-MIB", "vlanStatsGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup6"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup7"),
    ("CISCO-VTP-MIB", "vtpTrunkPruningGroup3"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup8"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance14 = vtpMIBCompliance14.setStatus("deprecated")
vtpMIBCompliance15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 15)
).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroupRev1"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPruningGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPruningGroup2"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup3"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanNotifEnabledGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup2"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup3"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup4"),
    ("CISCO-VTP-MIB", "vtpDiscoverGroup"),
    ("CISCO-VTP-MIB", "vtpDatabaseGroup"),
    ("CISCO-VTP-MIB", "vtpAuthGroup"),
    ("CISCO-VTP-MIB", "vtpInternalVlanGrp"),
    ("CISCO-VTP-MIB", "vlanStatsGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup6"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup7"),
    ("CISCO-VTP-MIB", "vtpTrunkPruningGroup3"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup8"),
    ("CISCO-VTP-MIB", "vlanTrunkPortActiveVlansGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance15 = vtpMIBCompliance15.setStatus("deprecated")
vtpMIBCompliance16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 16)
).setObjects(
    ("CISCO-VTP-MIB", "vtpBasicGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroupRev1"),
    ("CISCO-VTP-MIB", "vtpStatsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup"),
    ("CISCO-VTP-MIB", "vtpVersion2BasicGroup"),
    ("CISCO-VTP-MIB", "vtpNotificationObjectsGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPruningGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPruningGroup2"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup"),
    ("CISCO-VTP-MIB", "vtpTrunkPortGroup3"),
    ("CISCO-VTP-MIB", "vtp4kVlanGroupRev1"),
    ("CISCO-VTP-MIB", "vtpVlanIfIndexGroup"),
    ("CISCO-VTP-MIB", "vtpVlanInfoEditGroup2"),
    ("CISCO-VTP-MIB", "vtpVlanNotifEnabledGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup2"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup3"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup4"),
    ("CISCO-VTP-MIB", "vtpDiscoverGroup"),
    ("CISCO-VTP-MIB", "vtpDatabaseGroup"),
    ("CISCO-VTP-MIB", "vtpAuthGroup"),
    ("CISCO-VTP-MIB", "vtpInternalVlanGrp"),
    ("CISCO-VTP-MIB", "vlanStatsGroup"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup6"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup7"),
    ("CISCO-VTP-MIB", "vtpTrunkPruningGroup3"),
    ("CISCO-VTP-MIB", "vtpConfigNotificationsGroup8"),
    ("CISCO-VTP-MIB", "vlanTrunkPortActiveVlansGroup"),
    ("CISCO-VTP-MIB", "vtpSourceInterfaceGroup"),
    ("CISCO-VTP-MIB", "vtpConfigFileGroup"),
    ("CISCO-VTP-MIB", "vtpVlanLocalShutdownGroup"),
    ("CISCO-VTP-MIB", "vtpLocalUpdaterGroup"),
    ("CISCO-VTP-MIB", "vtpDeviceIdGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpMIBCompliance16 = vtpMIBCompliance16.setStatus("current")
vtpBasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 1)).setObjects(
    ("CISCO-VTP-MIB", "vtpVersion"),
    ("CISCO-VTP-MIB", "vtpMaxVlanStorage"),
    ("CISCO-VTP-MIB", "vtpNotificationsEnabled"),
    ("CISCO-VTP-MIB", "managementDomainName"),
    ("CISCO-VTP-MIB", "managementDomainLocalMode"),
    ("CISCO-VTP-MIB", "managementDomainConfigRevNumber"),
    ("CISCO-VTP-MIB", "managementDomainLastUpdater"),
    ("CISCO-VTP-MIB", "managementDomainLastChange"),
    ("CISCO-VTP-MIB", "managementDomainTftpServer"),
    ("CISCO-VTP-MIB", "managementDomainTftpPathname"),
    ("CISCO-VTP-MIB", "managementDomainRowStatus"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpBasicGroup = vtpBasicGroup.setStatus("current")
vtpVlanInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 13)).setObjects(
    ("CISCO-VTP-MIB", "vtpVlanState"),
    ("CISCO-VTP-MIB", "vtpVlanType"),
    ("CISCO-VTP-MIB", "vtpVlanName"),
    ("CISCO-VTP-MIB", "vtpVlanMtu"),
    ("CISCO-VTP-MIB", "vtpVlanDot10Said"),
    ("CISCO-VTP-MIB", "vtpVlanRingNumber"),
    ("CISCO-VTP-MIB", "vtpVlanBridgeNumber"),
    ("CISCO-VTP-MIB", "vtpVlanStpType"),
    ("CISCO-VTP-MIB", "vtpVlanParentVlan"),
    ("CISCO-VTP-MIB", "vtpVlanTranslationalVlan1"),
    ("CISCO-VTP-MIB", "vtpVlanTranslationalVlan2"),
    ("CISCO-VTP-MIB", "vtpVlanBridgeType"),
    ("CISCO-VTP-MIB", "vtpVlanAreHopCount"),
    ("CISCO-VTP-MIB", "vtpVlanSteHopCount"),
    ("CISCO-VTP-MIB", "vtpVlanIsCRFBackup"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpVlanInfoGroup = vtpVlanInfoGroup.setStatus("current")
vtpVlanInfoEditGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 14)).setObjects(
    ("CISCO-VTP-MIB", "vtpVlanEditOperation"),
    ("CISCO-VTP-MIB", "vtpVlanApplyStatus"),
    ("CISCO-VTP-MIB", "vtpVlanEditBufferOwner"),
    ("CISCO-VTP-MIB", "vtpVlanEditConfigRevNumber"),
    ("CISCO-VTP-MIB", "vtpVlanEditState"),
    ("CISCO-VTP-MIB", "vtpVlanEditType"),
    ("CISCO-VTP-MIB", "vtpVlanEditName"),
    ("CISCO-VTP-MIB", "vtpVlanEditMtu"),
    ("CISCO-VTP-MIB", "vtpVlanEditDot10Said"),
    ("CISCO-VTP-MIB", "vtpVlanEditRingNumber"),
    ("CISCO-VTP-MIB", "vtpVlanEditBridgeNumber"),
    ("CISCO-VTP-MIB", "vtpVlanEditStpType"),
    ("CISCO-VTP-MIB", "vtpVlanEditParentVlan"),
    ("CISCO-VTP-MIB", "vtpVlanEditRowStatus"),
    ("CISCO-VTP-MIB", "vtpVlanEditTranslationalVlan1"),
    ("CISCO-VTP-MIB", "vtpVlanEditTranslationalVlan2"),
    ("CISCO-VTP-MIB", "vtpVlanEditBridgeType"),
    ("CISCO-VTP-MIB", "vtpVlanEditAreHopCount"),
    ("CISCO-VTP-MIB", "vtpVlanEditSteHopCount"),
    ("CISCO-VTP-MIB", "vtpVlanEditIsCRFBackup"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpVlanInfoEditGroup = vtpVlanInfoEditGroup.setStatus("current")
vtpStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 4)).setObjects(
    ("CISCO-VTP-MIB", "vtpInSummaryAdverts"),
    ("CISCO-VTP-MIB", "vtpInSubsetAdverts"),
    ("CISCO-VTP-MIB", "vtpInAdvertRequests"),
    ("CISCO-VTP-MIB", "vtpOutSummaryAdverts"),
    ("CISCO-VTP-MIB", "vtpOutSubsetAdverts"),
    ("CISCO-VTP-MIB", "vtpOutAdvertRequests"),
    ("CISCO-VTP-MIB", "vtpConfigRevNumberErrors"),
    ("CISCO-VTP-MIB", "vtpConfigDigestErrors"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpStatsGroup = vtpStatsGroup.setStatus("current")
vtpTrunkPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 5)).setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortManagementDomain"),
    ("CISCO-VTP-MIB", "vlanTrunkPortEncapsulationType"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled"),
    ("CISCO-VTP-MIB", "vlanTrunkPortNativeVlan"),
    ("CISCO-VTP-MIB", "vlanTrunkPortRowStatus"),
    ("CISCO-VTP-MIB", "vlanTrunkPortSetSerialNo"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpTrunkPortGroup = vtpTrunkPortGroup.setStatus("current")
vtpTrunkPortGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 11)).setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortDynamicState"),
    ("CISCO-VTP-MIB", "vlanTrunkPortDynamicStatus"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVtpEnabled"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpTrunkPortGroup2 = vtpTrunkPortGroup2.setStatus("current")
vtpTrunkPortGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 15)).setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortEncapsulationOperType")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpTrunkPortGroup3 = vtpTrunkPortGroup3.setStatus("current")
vtpTrunkPruningGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 7)).setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortInJoins"),
    ("CISCO-VTP-MIB", "vlanTrunkPortOutJoins"),
    ("CISCO-VTP-MIB", "vlanTrunkPortOldAdverts"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansPruningEligible"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpTrunkPruningGroup = vtpTrunkPruningGroup.setStatus("current")
vtpTrunkPruningGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 10)).setObjects(
    ("CISCO-VTP-MIB", "managementDomainPruningState")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpTrunkPruningGroup2 = vtpTrunkPruningGroup2.setStatus("current")
vtpVersion2BasicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 12)).setObjects(
    ("CISCO-VTP-MIB", "managementDomainVersionInUse")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpVersion2BasicGroup = vtpVersion2BasicGroup.setStatus("current")
vtpConfigNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 6)
).setObjects(
    ("CISCO-VTP-MIB", "vtpConfigDigestError"),
    ("CISCO-VTP-MIB", "vtpConfigRevNumberError"),
    ("CISCO-VTP-MIB", "vtpServerDisabled"),
    ("CISCO-VTP-MIB", "vtpMtuTooBig"),
    ("CISCO-VTP-MIB", "vtpVersionOneDeviceDetected"),
    ("CISCO-VTP-MIB", "vlanTrunkPortDynamicStatusChange"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpConfigNotificationsGroup = vtpConfigNotificationsGroup.setStatus("deprecated")
vtp4kVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 16)).setObjects(
    ("CISCO-VTP-MIB", "vtpVlanTypeExt"),
    ("CISCO-VTP-MIB", "vtpVlanEditTypeExt"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled2k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled3k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled4k"),
    ("CISCO-VTP-MIB", "vtpVlansPruningEligible2k"),
    ("CISCO-VTP-MIB", "vtpVlansPruningEligible3k"),
    ("CISCO-VTP-MIB", "vtpVlansPruningEligible4k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined2k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined3k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined4k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined2k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined3k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined4k"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtp4kVlanGroup = vtp4kVlanGroup.setStatus("deprecated")
vtpDot1qTunnelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 17)).setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortsDot1qTag"),
    ("CISCO-VTP-MIB", "vlanTrunkPortDot1qTunnel"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpDot1qTunnelGroup = vtpDot1qTunnelGroup.setStatus("deprecated")
vtpVlanIfIndexGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 18)).setObjects(
    ("CISCO-VTP-MIB", "vtpVlanIfIndex")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpVlanIfIndexGroup = vtpVlanIfIndexGroup.setStatus("current")
vtpVlanInfoEditGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 19)).setObjects(
    ("CISCO-VTP-MIB", "vtpVlanEditModifiedVlan")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpVlanInfoEditGroup2 = vtpVlanInfoEditGroup2.setStatus("current")
vtp4kVlanGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 20)).setObjects(
    ("CISCO-VTP-MIB", "vtpVlanTypeExt"),
    ("CISCO-VTP-MIB", "vtpVlanEditTypeExt2"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled2k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled3k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled4k"),
    ("CISCO-VTP-MIB", "vtpVlansPruningEligible2k"),
    ("CISCO-VTP-MIB", "vtpVlansPruningEligible3k"),
    ("CISCO-VTP-MIB", "vtpVlansPruningEligible4k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined2k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined3k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined4k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined2k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined3k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined4k"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtp4kVlanGroupRev1 = vtp4kVlanGroupRev1.setStatus("current")
vtpNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 21)
).setObjects(("CISCO-VTP-MIB", "vtpVlanPortLocalSegment"))
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpNotificationObjectsGroup = vtpNotificationObjectsGroup.setStatus("current")
vtpDot1qTunnelGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 22)).setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortsDot1qTag")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpDot1qTunnelGroup2 = vtpDot1qTunnelGroup2.setStatus("deprecated")
vtpConfigNotificationsGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 23)
).setObjects(
    ("CISCO-VTP-MIB", "vtpLocalModeChanged"),
    ("CISCO-VTP-MIB", "vtpVersionInUseChanged"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpConfigNotificationsGroup2 = vtpConfigNotificationsGroup2.setStatus("current")
vtpVlanNotifEnabledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 24)
).setObjects(
    ("CISCO-VTP-MIB", "vtpVlanCreatedNotifEnabled"),
    ("CISCO-VTP-MIB", "vtpVlanDeletedNotifEnabled"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpVlanNotifEnabledGroup = vtpVlanNotifEnabledGroup.setStatus("current")
vtpConfigNotificationsGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 25)
).setObjects(("CISCO-VTP-MIB", "vtpVlanCreated"), ("CISCO-VTP-MIB", "vtpVlanDeleted"))
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpConfigNotificationsGroup3 = vtpConfigNotificationsGroup3.setStatus("current")
vtpConfigNotificationsGroup4 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 26)
).setObjects(("CISCO-VTP-MIB", "vtpVlanRingNumberConflict"))
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpConfigNotificationsGroup4 = vtpConfigNotificationsGroup4.setStatus("current")
vtpDiscoverGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 27)).setObjects(
    ("CISCO-VTP-MIB", "vtpDiscoverAction"),
    ("CISCO-VTP-MIB", "vtpDiscoverStatus"),
    ("CISCO-VTP-MIB", "vtpLastDiscoverTime"),
    ("CISCO-VTP-MIB", "vtpDiscoverResultIndex"),
    ("CISCO-VTP-MIB", "vtpDiscoverResultDatabaseName"),
    ("CISCO-VTP-MIB", "vtpDiscoverResultConflicting"),
    ("CISCO-VTP-MIB", "vtpDiscoverResultDeviceId"),
    ("CISCO-VTP-MIB", "vtpDiscoverResultPrimaryServer"),
    ("CISCO-VTP-MIB", "vtpDiscoverResultRevNumber"),
    ("CISCO-VTP-MIB", "vtpDiscoverResultSystemName"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpDiscoverGroup = vtpDiscoverGroup.setStatus("current")
vtpDatabaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 28)).setObjects(
    ("CISCO-VTP-MIB", "vtpDatabaseName"),
    ("CISCO-VTP-MIB", "vtpDatabaseLocalMode"),
    ("CISCO-VTP-MIB", "vtpDatabaseRevNumber"),
    ("CISCO-VTP-MIB", "vtpDatabasePrimaryServer"),
    ("CISCO-VTP-MIB", "vtpDatabasePrimaryServerId"),
    ("CISCO-VTP-MIB", "vtpDatabaseTakeOverPrimary"),
    ("CISCO-VTP-MIB", "vtpDatabaseTakeOverPassword"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpDatabaseGroup = vtpDatabaseGroup.setStatus("current")
vtpAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 29)).setObjects(
    ("CISCO-VTP-MIB", "vtpAuthPassword"),
    ("CISCO-VTP-MIB", "vtpAuthPasswordType"),
    ("CISCO-VTP-MIB", "vtpAuthSecretKey"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpAuthGroup = vtpAuthGroup.setStatus("current")
vtpConfigNotificationsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 30)
).setObjects(
    ("CISCO-VTP-MIB", "vtpConfigDigestError"),
    ("CISCO-VTP-MIB", "vtpConfigRevNumberError"),
    ("CISCO-VTP-MIB", "vtpVersionOneDeviceDetected"),
    ("CISCO-VTP-MIB", "vlanTrunkPortDynamicStatusChange"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpConfigNotificationsGroupRev1 = vtpConfigNotificationsGroupRev1.setStatus(
        "current"
    )
vtpConfigNotificationsGroup5 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 31)
).setObjects(("CISCO-VTP-MIB", "vtpServerDisabled"), ("CISCO-VTP-MIB", "vtpMtuTooBig"))
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpConfigNotificationsGroup5 = vtpConfigNotificationsGroup5.setStatus("deprecated")
vtpInternalVlanGrp = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 32)).setObjects(
    ("CISCO-VTP-MIB", "vtpInternalVlanAllocPolicy"),
    ("CISCO-VTP-MIB", "vtpInternalVlanOwner"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpInternalVlanGrp = vtpInternalVlanGrp.setStatus("current")
vlanStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 33)).setObjects(
    ("CISCO-VTP-MIB", "vlanStatsVlans"),
    ("CISCO-VTP-MIB", "vlanStatsExtendedVlans"),
    ("CISCO-VTP-MIB", "vlanStatsInternalVlans"),
    ("CISCO-VTP-MIB", "vlanStatsFreeVlans"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vlanStatsGroup = vlanStatsGroup.setStatus("current")
vtpConfigNotificationsGroup6 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 34)
).setObjects(("CISCO-VTP-MIB", "vtpServerDisabled"))
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpConfigNotificationsGroup6 = vtpConfigNotificationsGroup6.setStatus("current")
vtpConfigNotificationsGroup7 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 35)
).setObjects(("CISCO-VTP-MIB", "vtpMtuTooBig"))
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpConfigNotificationsGroup7 = vtpConfigNotificationsGroup7.setStatus("current")
vtpTrunkPruningGroup3 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 36)).setObjects(
    ("CISCO-VTP-MIB", "managementDomainPruningStateOper")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpTrunkPruningGroup3 = vtpTrunkPruningGroup3.setStatus("current")
vtpConfigNotificationsGroup8 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 37)
).setObjects(("CISCO-VTP-MIB", "vtpPruningStateOperChange"))
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpConfigNotificationsGroup8 = vtpConfigNotificationsGroup8.setStatus("current")
vlanTrunkPortActiveVlansGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 38)
).setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansActiveFirst2k"),
    ("CISCO-VTP-MIB", "vlanTrunkPortVlansActiveSecond2k"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vlanTrunkPortActiveVlansGroup = vlanTrunkPortActiveVlansGroup.setStatus("current")
vtpSourceInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 39)
).setObjects(
    ("CISCO-VTP-MIB", "managementDomainAdminSrcIf"),
    ("CISCO-VTP-MIB", "managementDomainSourceOnlyMode"),
    ("CISCO-VTP-MIB", "managementDomainOperSrcIf"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpSourceInterfaceGroup = vtpSourceInterfaceGroup.setStatus("current")
vtpConfigFileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 40)).setObjects(
    ("CISCO-VTP-MIB", "managementDomainConfigFile")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpConfigFileGroup = vtpConfigFileGroup.setStatus("current")
vtpVlanLocalShutdownGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 41)
).setObjects(("CISCO-VTP-MIB", "vtpVlanLocalShutdown"))
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpVlanLocalShutdownGroup = vtpVlanLocalShutdownGroup.setStatus("current")
vtpLocalUpdaterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 42)).setObjects(
    ("CISCO-VTP-MIB", "managementDomainLocalUpdaterType"),
    ("CISCO-VTP-MIB", "managementDomainLocalUpdater"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpLocalUpdaterGroup = vtpLocalUpdaterGroup.setStatus("current")
vtpDeviceIdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 43)).setObjects(
    ("CISCO-VTP-MIB", "managementDomainDeviceID")
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    vtpDeviceIdGroup = vtpDeviceIdGroup.setStatus("current")
mibBuilder.exportSymbols(
    "CISCO-VTP-MIB",
    vtpVlanTypeExt=vtpVlanTypeExt,
    vtpPruningStateOperChange=vtpPruningStateOperChange,
    managementDomainTftpServer=managementDomainTftpServer,
    vtpStats=vtpStats,
    vtpServerDisabled=vtpServerDisabled,
    vtpVlanEditDot10Said=vtpVlanEditDot10Said,
    vtpVlanEditBridgeType=vtpVlanEditBridgeType,
    vtpMIBCompliance4=vtpMIBCompliance4,
    vtpVlanIndex=vtpVlanIndex,
    managementDomainDeviceID=managementDomainDeviceID,
    vtpVlanTranslationalVlan2=vtpVlanTranslationalVlan2,
    vlanTrunkPortDynamicStatus=vlanTrunkPortDynamicStatus,
    vtpConfigNotificationsGroup7=vtpConfigNotificationsGroup7,
    vtpVlanIsCRFBackup=vtpVlanIsCRFBackup,
    vtpVlanDot10Said=vtpVlanDot10Said,
    vtpInAdvertRequests=vtpInAdvertRequests,
    vtpVlanInfoEditGroup2=vtpVlanInfoEditGroup2,
    vtpMIBCompliance8=vtpMIBCompliance8,
    vtpDatabaseName=vtpDatabaseName,
    vtpTrunkPortGroup=vtpTrunkPortGroup,
    vlanTrunkPortOldAdverts=vlanTrunkPortOldAdverts,
    vtpConfigRevNumberError=vtpConfigRevNumberError,
    vtpOutAdvertRequests=vtpOutAdvertRequests,
    vtpDiscoverResultTable=vtpDiscoverResultTable,
    vtpDot1qTunnelGroup=vtpDot1qTunnelGroup,
    vtpVlanMtu=vtpVlanMtu,
    vtpVlanTable=vtpVlanTable,
    vtpDiscoverResultEntry=vtpDiscoverResultEntry,
    vtpConfigDigestError=vtpConfigDigestError,
    vtpMtuTooBig=vtpMtuTooBig,
    vtpVlanEditType=vtpVlanEditType,
    vtpVlansPruningEligible2k=vtpVlansPruningEligible2k,
    vlanInfo=vlanInfo,
    vlanTrunkPortVlansRcvJoined2k=vlanTrunkPortVlansRcvJoined2k,
    vtpConfigNotificationsGroup=vtpConfigNotificationsGroup,
    vtpDiscover=vtpDiscover,
    vtpVlansPruningEligible3k=vtpVlansPruningEligible3k,
    vtpVlanEditState=vtpVlanEditState,
    vlanTrunkPortDynamicState=vlanTrunkPortDynamicState,
    vtpVlanEditBridgeNumber=vtpVlanEditBridgeNumber,
    vtpVlanEditAreHopCount=vtpVlanEditAreHopCount,
    vtpVlanNotifEnabledGroup=vtpVlanNotifEnabledGroup,
    vtpDatabasePrimaryServerId=vtpDatabasePrimaryServerId,
    vlanTrunkPorts=vlanTrunkPorts,
    vlanTrunkPortVlansPruningEligible=vlanTrunkPortVlansPruningEligible,
    vtpDiscoverResultIndex=vtpDiscoverResultIndex,
    vtpDatabasePrimaryServer=vtpDatabasePrimaryServer,
    managementDomainSourceOnlyMode=managementDomainSourceOnlyMode,
    vlanTrunkPortActiveVlansGroup=vlanTrunkPortActiveVlansGroup,
    vtpVlanEditSteHopCount=vtpVlanEditSteHopCount,
    vlanTrunkPortEntry=vlanTrunkPortEntry,
    vtpOutSummaryAdverts=vtpOutSummaryAdverts,
    vtpDatabaseEntry=vtpDatabaseEntry,
    internalVlanInfo=internalVlanInfo,
    vlanStatistics=vlanStatistics,
    vtpNotificationsPrefix=vtpNotificationsPrefix,
    vtpTrunkPruningGroup3=vtpTrunkPruningGroup3,
    vlanTrunkPortVlansActiveSecond2k=vlanTrunkPortVlansActiveSecond2k,
    vtpTrunkPortGroup2=vtpTrunkPortGroup2,
    managementDomainLastChange=managementDomainLastChange,
    managementDomainPruningState=managementDomainPruningState,
    vlanTrunkPortVlansXmitJoined3k=vlanTrunkPortVlansXmitJoined3k,
    vtpVlanCreatedNotifEnabled=vtpVlanCreatedNotifEnabled,
    vtpTrunkPruningGroup2=vtpTrunkPruningGroup2,
    vtpMIBCompliance16=vtpMIBCompliance16,
    vtpVlanStpType=vtpVlanStpType,
    vtpVlanEditBufferOwner=vtpVlanEditBufferOwner,
    vlanTrunkPortVtpEnabled=vlanTrunkPortVtpEnabled,
    vtpMIBCompliance14=vtpMIBCompliance14,
    vtp4kVlanGroup=vtp4kVlanGroup,
    vtpVlanName=vtpVlanName,
    vtpDatabaseGroup=vtpDatabaseGroup,
    vtpVlanEditTypeExt2=vtpVlanEditTypeExt2,
    vtpStatus=vtpStatus,
    vtpVersionInUseChanged=vtpVersionInUseChanged,
    vtpSourceInterfaceGroup=vtpSourceInterfaceGroup,
    vtpVlanEditTranslationalVlan2=vtpVlanEditTranslationalVlan2,
    vtpVlanSteHopCount=vtpVlanSteHopCount,
    vtpInternalVlanAllocPolicy=vtpInternalVlanAllocPolicy,
    vtpVlanLocalShutdownGroup=vtpVlanLocalShutdownGroup,
    vtpDiscoverResultConflicting=vtpDiscoverResultConflicting,
    vlanTrunkPortVlansXmitJoined=vlanTrunkPortVlansXmitJoined,
    vtpNotifications=vtpNotifications,
    vtpAuthEntry=vtpAuthEntry,
    managementDomainPruningStateOper=managementDomainPruningStateOper,
    vtpVlanBridgeType=vtpVlanBridgeType,
    vlanTrunkPortIfIndex=vlanTrunkPortIfIndex,
    PYSNMP_MODULE_ID=ciscoVtpMIB,
    vtpVlanLocalShutdown=vtpVlanLocalShutdown,
    vtpDatabaseTakeOverPrimary=vtpDatabaseTakeOverPrimary,
    vtp4kVlanGroupRev1=vtp4kVlanGroupRev1,
    vtpVlanTranslationalVlan1=vtpVlanTranslationalVlan1,
    vtpDiscoverEntry=vtpDiscoverEntry,
    VlanTypeExt=VlanTypeExt,
    vtpDot1qTunnelGroup2=vtpDot1qTunnelGroup2,
    vtpVlanEditIndex=vtpVlanEditIndex,
    vlanTrunkPortVlansRcvJoined3k=vlanTrunkPortVlansRcvJoined3k,
    vtpConfigDigestErrors=vtpConfigDigestErrors,
    vtpConfigNotificationsGroup3=vtpConfigNotificationsGroup3,
    vtpMIBObjects=vtpMIBObjects,
    vtpInternalVlanGrp=vtpInternalVlanGrp,
    managementDomainLocalMode=managementDomainLocalMode,
    vtpInSubsetAdverts=vtpInSubsetAdverts,
    vtpMIBCompliance12=vtpMIBCompliance12,
    vtpDiscoverTable=vtpDiscoverTable,
    vtpVlanEntry=vtpVlanEntry,
    vlanTrunkPortManagementDomain=vlanTrunkPortManagementDomain,
    vlanTrunkPortVlansRcvJoined4k=vlanTrunkPortVlansRcvJoined4k,
    managementDomainIndex=managementDomainIndex,
    vtpVlanEditName=vtpVlanEditName,
    vlanTrunkPortDynamicStatusChange=vlanTrunkPortDynamicStatusChange,
    vtpMIBCompliance=vtpMIBCompliance,
    vlanStatsGroup=vlanStatsGroup,
    vtpConfigFileGroup=vtpConfigFileGroup,
    vtpVlanEditParentVlan=vtpVlanEditParentVlan,
    vtpDiscoverStatus=vtpDiscoverStatus,
    vtpVlanEditRingNumber=vtpVlanEditRingNumber,
    vtpLocalUpdaterGroup=vtpLocalUpdaterGroup,
    vtpConfigNotificationsGroup8=vtpConfigNotificationsGroup8,
    vtpAuthentication=vtpAuthentication,
    vlanStatsVlans=vlanStatsVlans,
    vtpBasicGroup=vtpBasicGroup,
    vlanTrunkPortVlansXmitJoined4k=vlanTrunkPortVlansXmitJoined4k,
    vlanTrunkPortVlansActiveFirst2k=vlanTrunkPortVlansActiveFirst2k,
    vlanTrunkPortVlansRcvJoined=vlanTrunkPortVlansRcvJoined,
    vtpDiscoverResultRevNumber=vtpDiscoverResultRevNumber,
    vlanTrunkPortSetSerialNo=vlanTrunkPortSetSerialNo,
    vtpAuthSecretKey=vtpAuthSecretKey,
    vtpInternalVlanTable=vtpInternalVlanTable,
    vtpMIBGroups=vtpMIBGroups,
    vtpInternalVlanEntry=vtpInternalVlanEntry,
    vtpVlanEditOperation=vtpVlanEditOperation,
    vlanTrunkPortEncapsulationType=vlanTrunkPortEncapsulationType,
    vtpMIBCompliance15=vtpMIBCompliance15,
    vtpConfigNotificationsGroup6=vtpConfigNotificationsGroup6,
    ciscoVtpMIB=ciscoVtpMIB,
    vtpStatsGroup=vtpStatsGroup,
    vtpVlanAreHopCount=vtpVlanAreHopCount,
    vtpVlanType=vtpVlanType,
    vtpVlanRingNumber=vtpVlanRingNumber,
    vlanTrunkPortVlansEnabled=vlanTrunkPortVlansEnabled,
    managementDomainVersionInUse=managementDomainVersionInUse,
    vtpStatsTable=vtpStatsTable,
    vtpVlanLocalShutdownTable=vtpVlanLocalShutdownTable,
    vlanStatsFreeVlans=vlanStatsFreeVlans,
    vtpDatabaseTable=vtpDatabaseTable,
    vtpVlanEditIsCRFBackup=vtpVlanEditIsCRFBackup,
    vlanManagementDomains=vlanManagementDomains,
    vlanTrunkPortNativeVlan=vlanTrunkPortNativeVlan,
    vtpVlanEditModifiedVlan=vtpVlanEditModifiedVlan,
    managementDomainTable=managementDomainTable,
    vtpDiscoverAction=vtpDiscoverAction,
    vtpVlanDeletedNotifEnabled=vtpVlanDeletedNotifEnabled,
    vtpVlanState=vtpVlanState,
    vtpVlanParentVlan=vtpVlanParentVlan,
    vtpDatabaseTakeOverPassword=vtpDatabaseTakeOverPassword,
    vtpLocalModeChanged=vtpLocalModeChanged,
    vlanTrunkPortRowStatus=vlanTrunkPortRowStatus,
    vtpMIBCompliance3=vtpMIBCompliance3,
    vtpAuthPassword=vtpAuthPassword,
    vtpDiscoverGroup=vtpDiscoverGroup,
    vtpNotificationObjectsGroup=vtpNotificationObjectsGroup,
    vtpNotificationsEnabled=vtpNotificationsEnabled,
    vlanTrunkPortsDot1qTag=vlanTrunkPortsDot1qTag,
    vtpNotificationsObjects=vtpNotificationsObjects,
    ManagementDomainIndex=ManagementDomainIndex,
    vtpInSummaryAdverts=vtpInSummaryAdverts,
    vtpOutSubsetAdverts=vtpOutSubsetAdverts,
    vtpDiscoverResultDatabaseName=vtpDiscoverResultDatabaseName,
    vtpVersion=vtpVersion,
    vtpConfigNotificationsGroup5=vtpConfigNotificationsGroup5,
    managementDomainName=managementDomainName,
    managementDomainOperSrcIf=managementDomainOperSrcIf,
    managementDomainEntry=managementDomainEntry,
    vtpDiscoverResultDeviceId=vtpDiscoverResultDeviceId,
    vtpTrunkPruningGroup=vtpTrunkPruningGroup,
    VlanType=VlanType,
    vlanEdit=vlanEdit,
    vtpVlanDeleted=vtpVlanDeleted,
    vlanTrunkPortInJoins=vlanTrunkPortInJoins,
    vtpMIBCompliance10=vtpMIBCompliance10,
    managementDomainLocalUpdater=managementDomainLocalUpdater,
    vtpEditControlTable=vtpEditControlTable,
    vtpVlanPortLocalSegment=vtpVlanPortLocalSegment,
    vlanTrunkPortVlansXmitJoined2k=vlanTrunkPortVlansXmitJoined2k,
    vtpConfigNotificationsGroup2=vtpConfigNotificationsGroup2,
    vtpMIBCompliance7=vtpMIBCompliance7,
    vlanTrunkPortVlansEnabled3k=vlanTrunkPortVlansEnabled3k,
    vlanStatsExtendedVlans=vlanStatsExtendedVlans,
    managementDomainLocalUpdaterType=managementDomainLocalUpdaterType,
    vlanTrunkPortVlansEnabled4k=vlanTrunkPortVlansEnabled4k,
    vtpMIBCompliance6=vtpMIBCompliance6,
    vtpVlanIfIndexGroup=vtpVlanIfIndexGroup,
    vtpVlanEditEntry=vtpVlanEditEntry,
    vtpMIBCompliances=vtpMIBCompliances,
    vlanStatsInternalVlans=vlanStatsInternalVlans,
    vtpDatabaseLocalMode=vtpDatabaseLocalMode,
    managementDomainTftpPathname=managementDomainTftpPathname,
    vlanTrunkPortDot1qTunnel=vlanTrunkPortDot1qTunnel,
    vtpMIBConformance=vtpMIBConformance,
    vtpStatsEntry=vtpStatsEntry,
    vtpMIBCompliance5=vtpMIBCompliance5,
    vtpVlanEditStpType=vtpVlanEditStpType,
    vlanTrunkPortOutJoins=vlanTrunkPortOutJoins,
    vtpDeviceIdGroup=vtpDeviceIdGroup,
    vtpDiscoverResultSystemName=vtpDiscoverResultSystemName,
    vtpVlanEditRowStatus=vtpVlanEditRowStatus,
    vtpMaxVlanStorage=vtpMaxVlanStorage,
    managementDomainAdminSrcIf=managementDomainAdminSrcIf,
    vtpTrunkPortGroup3=vtpTrunkPortGroup3,
    vtpVlanEditTranslationalVlan1=vtpVlanEditTranslationalVlan1,
    vtpVersion2BasicGroup=vtpVersion2BasicGroup,
    vtpVlansPruningEligible4k=vtpVlansPruningEligible4k,
    vtpAuthPasswordType=vtpAuthPasswordType,
    vtpDatabaseIndex=vtpDatabaseIndex,
    vlanTrunkPortVlansEnabled2k=vlanTrunkPortVlansEnabled2k,
    VlanIndex=VlanIndex,
    vtpVlanRingNumberConflict=vtpVlanRingNumberConflict,
    vtpMIBCompliance2=vtpMIBCompliance2,
    managementDomainConfigFile=managementDomainConfigFile,
    vlanTrunkPortTable=vlanTrunkPortTable,
    vtpVersionOneDeviceDetected=vtpVersionOneDeviceDetected,
    vtpAuthGroup=vtpAuthGroup,
    vtpDatabaseRevNumber=vtpDatabaseRevNumber,
    vtpVlanLocalShutdownEntry=vtpVlanLocalShutdownEntry,
    vtpLastDiscoverTime=vtpLastDiscoverTime,
    vtpDatabase=vtpDatabase,
    vtpDiscoverResultPrimaryServer=vtpDiscoverResultPrimaryServer,
    vtpVlanInfoEditGroup=vtpVlanInfoEditGroup,
    managementDomainRowStatus=managementDomainRowStatus,
    vtpVlanEditTypeExt=vtpVlanEditTypeExt,
    vtpMIBCompliance13=vtpMIBCompliance13,
    vtpVlanEditMtu=vtpVlanEditMtu,
    vtpAuthenticationTable=vtpAuthenticationTable,
    vtpMIBCompliance11=vtpMIBCompliance11,
    managementDomainLastUpdater=managementDomainLastUpdater,
    vtpConfigRevNumberErrors=vtpConfigRevNumberErrors,
    vtpVlanIfIndex=vtpVlanIfIndex,
    vtpMIBCompliance9=vtpMIBCompliance9,
    managementDomainConfigRevNumber=managementDomainConfigRevNumber,
    vtpEditControlEntry=vtpEditControlEntry,
    vlanTrunkPortEncapsulationOperType=vlanTrunkPortEncapsulationOperType,
    vtpConfigNotificationsGroupRev1=vtpConfigNotificationsGroupRev1,
    vtpVlanCreated=vtpVlanCreated,
    vtpVlanInfoGroup=vtpVlanInfoGroup,
    vtpConfigNotificationsGroup4=vtpConfigNotificationsGroup4,
    vtpVlanBridgeNumber=vtpVlanBridgeNumber,
    vtpVlanEditTable=vtpVlanEditTable,
    vtpVlanEditConfigRevNumber=vtpVlanEditConfigRevNumber,
    vtpVlanApplyStatus=vtpVlanApplyStatus,
    vtpInternalVlanOwner=vtpInternalVlanOwner,
)
