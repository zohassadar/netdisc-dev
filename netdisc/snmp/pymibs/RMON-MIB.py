#
# PySNMP MIB module RMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///mibs.thola.io/asn1/RMON-MIB
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
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols(
    "SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup"
)
(
    Counter32,
    MibIdentifier,
    IpAddress,
    mib_2,
    Counter64,
    Gauge32,
    TimeTicks,
    ModuleIdentity,
    NotificationType,
    ObjectIdentity,
    Bits,
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
    "mib-2",
    "Counter64",
    "Gauge32",
    "TimeTicks",
    "ModuleIdentity",
    "NotificationType",
    "ObjectIdentity",
    "Bits",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "Integer32",
    "iso",
    "Unsigned32",
)
DisplayString, TextualConvention = mibBuilder.importSymbols(
    "SNMPv2-TC", "DisplayString", "TextualConvention"
)
rmonMibModule = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 20, 8))
rmonMibModule.setRevisions(
    (
        "2000-05-11 00:00",
        "1995-02-01 00:00",
        "1991-11-01 00:00",
    )
)
if mibBuilder.loadTexts:
    rmonMibModule.setLastUpdated("200005110000Z")
if mibBuilder.loadTexts:
    rmonMibModule.setOrganization("IETF RMON MIB Working Group")
rmon = MibIdentifier((1, 3, 6, 1, 2, 1, 16))


class OwnerString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)


class EntryStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(
        SingleValueConstraint(1, 2, 3, 4)
    )
    namedValues = NamedValues(
        ("valid", 1), ("createRequest", 2), ("underCreation", 3), ("invalid", 4)
    )


statistics = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 1))
history = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 2))
alarm = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 3))
hosts = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 4))
hostTopN = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 5))
matrix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 6))
filter = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 7))
capture = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 8))
event = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 9))
rmonConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 20))
etherStatsTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 1, 1),
)
if mibBuilder.loadTexts:
    etherStatsTable.setStatus("current")
etherStatsEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1),
).setIndexNames((0, "RMON-MIB", "etherStatsIndex"))
if mibBuilder.loadTexts:
    etherStatsEntry.setStatus("current")
etherStatsIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    etherStatsIndex.setStatus("current")
etherStatsDataSource = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 2), ObjectIdentifier()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    etherStatsDataSource.setStatus("current")
etherStatsDropEvents = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 3), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    etherStatsDropEvents.setStatus("current")
etherStatsOctets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 4), Counter32())
    .setUnits("Octets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsOctets.setStatus("current")
etherStatsPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 5), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsPkts.setStatus("current")
etherStatsBroadcastPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 6), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsBroadcastPkts.setStatus("current")
etherStatsMulticastPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 7), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsMulticastPkts.setStatus("current")
etherStatsCRCAlignErrors = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 8), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsCRCAlignErrors.setStatus("current")
etherStatsUndersizePkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 9), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsUndersizePkts.setStatus("current")
etherStatsOversizePkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 10), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsOversizePkts.setStatus("current")
etherStatsFragments = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 11), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsFragments.setStatus("current")
etherStatsJabbers = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 12), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsJabbers.setStatus("current")
etherStatsCollisions = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 13), Counter32())
    .setUnits("Collisions")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsCollisions.setStatus("current")
etherStatsPkts64Octets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 14), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsPkts64Octets.setStatus("current")
etherStatsPkts65to127Octets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 15), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsPkts65to127Octets.setStatus("current")
etherStatsPkts128to255Octets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 16), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsPkts128to255Octets.setStatus("current")
etherStatsPkts256to511Octets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 17), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsPkts256to511Octets.setStatus("current")
etherStatsPkts512to1023Octets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 18), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsPkts512to1023Octets.setStatus("current")
etherStatsPkts1024to1518Octets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 19), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherStatsPkts1024to1518Octets.setStatus("current")
etherStatsOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 20), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    etherStatsOwner.setStatus("current")
etherStatsStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 1, 1, 1, 21), EntryStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    etherStatsStatus.setStatus("current")
historyControlTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 2, 1),
)
if mibBuilder.loadTexts:
    historyControlTable.setStatus("current")
historyControlEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1),
).setIndexNames((0, "RMON-MIB", "historyControlIndex"))
if mibBuilder.loadTexts:
    historyControlEntry.setStatus("current")
historyControlIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    historyControlIndex.setStatus("current")
historyControlDataSource = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 2), ObjectIdentifier()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    historyControlDataSource.setStatus("current")
historyControlBucketsRequested = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 3),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(50),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    historyControlBucketsRequested.setStatus("current")
historyControlBucketsGranted = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 4),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    historyControlBucketsGranted.setStatus("current")
historyControlInterval = (
    MibTableColumn(
        (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 5),
        Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3600)).clone(1800),
    )
    .setUnits("Seconds")
    .setMaxAccess("readcreate")
)
if mibBuilder.loadTexts:
    historyControlInterval.setStatus("current")
historyControlOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 6), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    historyControlOwner.setStatus("current")
historyControlStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 1, 1, 7), EntryStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    historyControlStatus.setStatus("current")
etherHistoryTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 2, 2),
)
if mibBuilder.loadTexts:
    etherHistoryTable.setStatus("current")
etherHistoryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 2, 2, 1),).setIndexNames(
    (0, "RMON-MIB", "etherHistoryIndex"), (0, "RMON-MIB", "etherHistorySampleIndex")
)
if mibBuilder.loadTexts:
    etherHistoryEntry.setStatus("current")
etherHistoryIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    etherHistoryIndex.setStatus("current")
etherHistorySampleIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    etherHistorySampleIndex.setStatus("current")
etherHistoryIntervalStart = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 3), TimeTicks()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    etherHistoryIntervalStart.setStatus("current")
etherHistoryDropEvents = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 4), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    etherHistoryDropEvents.setStatus("current")
etherHistoryOctets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 5), Counter32())
    .setUnits("Octets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherHistoryOctets.setStatus("current")
etherHistoryPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 6), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherHistoryPkts.setStatus("current")
etherHistoryBroadcastPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 7), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherHistoryBroadcastPkts.setStatus("current")
etherHistoryMulticastPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 8), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherHistoryMulticastPkts.setStatus("current")
etherHistoryCRCAlignErrors = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 9), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherHistoryCRCAlignErrors.setStatus("current")
etherHistoryUndersizePkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 10), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherHistoryUndersizePkts.setStatus("current")
etherHistoryOversizePkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 11), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherHistoryOversizePkts.setStatus("current")
etherHistoryFragments = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 12), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherHistoryFragments.setStatus("current")
etherHistoryJabbers = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 13), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherHistoryJabbers.setStatus("current")
etherHistoryCollisions = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 14), Counter32())
    .setUnits("Collisions")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    etherHistoryCollisions.setStatus("current")
etherHistoryUtilization = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 2, 2, 1, 15),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10000)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    etherHistoryUtilization.setStatus("current")
alarmTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 3, 1),
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
alarmEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1),
).setIndexNames((0, "RMON-MIB", "alarmIndex"))
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")
alarmIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("current")
alarmInterval = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 2), Integer32())
    .setUnits("Seconds")
    .setMaxAccess("readcreate")
)
if mibBuilder.loadTexts:
    alarmInterval.setStatus("current")
alarmVariable = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 3), ObjectIdentifier()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    alarmVariable.setStatus("current")
alarmSampleType = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 4),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2))),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    alarmSampleType.setStatus("current")
alarmValue = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 5), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    alarmValue.setStatus("current")
alarmStartupAlarm = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 6),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(
        namedValues=NamedValues(
            ("risingAlarm", 1), ("fallingAlarm", 2), ("risingOrFallingAlarm", 3)
        )
    ),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    alarmStartupAlarm.setStatus("current")
alarmRisingThreshold = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 7), Integer32()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    alarmRisingThreshold.setStatus("current")
alarmFallingThreshold = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 8), Integer32()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    alarmFallingThreshold.setStatus("current")
alarmRisingEventIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 9),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    alarmRisingEventIndex.setStatus("current")
alarmFallingEventIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 10),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    alarmFallingEventIndex.setStatus("current")
alarmOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 11), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    alarmOwner.setStatus("current")
alarmStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 12), EntryStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("current")
hostControlTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 4, 1),
)
if mibBuilder.loadTexts:
    hostControlTable.setStatus("current")
hostControlEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1),
).setIndexNames((0, "RMON-MIB", "hostControlIndex"))
if mibBuilder.loadTexts:
    hostControlEntry.setStatus("current")
hostControlIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostControlIndex.setStatus("current")
hostControlDataSource = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 2), ObjectIdentifier()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    hostControlDataSource.setStatus("current")
hostControlTableSize = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 3), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostControlTableSize.setStatus("current")
hostControlLastDeleteTime = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 4), TimeTicks()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostControlLastDeleteTime.setStatus("current")
hostControlOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 5), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    hostControlOwner.setStatus("current")
hostControlStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 1, 1, 6), EntryStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    hostControlStatus.setStatus("current")
hostTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 4, 2),
)
if mibBuilder.loadTexts:
    hostTable.setStatus("current")
hostEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1),
).setIndexNames((0, "RMON-MIB", "hostIndex"), (0, "RMON-MIB", "hostAddress"))
if mibBuilder.loadTexts:
    hostEntry.setStatus("current")
hostAddress = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 1), OctetString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostAddress.setStatus("current")
hostCreationOrder = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostCreationOrder.setStatus("current")
hostIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 3),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostIndex.setStatus("current")
hostInPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 4), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostInPkts.setStatus("current")
hostOutPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 5), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostOutPkts.setStatus("current")
hostInOctets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 6), Counter32())
    .setUnits("Octets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostInOctets.setStatus("current")
hostOutOctets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 7), Counter32())
    .setUnits("Octets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostOutOctets.setStatus("current")
hostOutErrors = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 8), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostOutErrors.setStatus("current")
hostOutBroadcastPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 9), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostOutBroadcastPkts.setStatus("current")
hostOutMulticastPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 2, 1, 10), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostOutMulticastPkts.setStatus("current")
hostTimeTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 4, 3),
)
if mibBuilder.loadTexts:
    hostTimeTable.setStatus("current")
hostTimeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 4, 3, 1),).setIndexNames(
    (0, "RMON-MIB", "hostTimeIndex"), (0, "RMON-MIB", "hostTimeCreationOrder")
)
if mibBuilder.loadTexts:
    hostTimeEntry.setStatus("current")
hostTimeAddress = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 1), OctetString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostTimeAddress.setStatus("current")
hostTimeCreationOrder = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostTimeCreationOrder.setStatus("current")
hostTimeIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 3),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostTimeIndex.setStatus("current")
hostTimeInPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 4), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostTimeInPkts.setStatus("current")
hostTimeOutPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 5), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostTimeOutPkts.setStatus("current")
hostTimeInOctets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 6), Counter32())
    .setUnits("Octets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostTimeInOctets.setStatus("current")
hostTimeOutOctets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 7), Counter32())
    .setUnits("Octets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostTimeOutOctets.setStatus("current")
hostTimeOutErrors = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 8), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostTimeOutErrors.setStatus("current")
hostTimeOutBroadcastPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 9), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostTimeOutBroadcastPkts.setStatus("current")
hostTimeOutMulticastPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 4, 3, 1, 10), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostTimeOutMulticastPkts.setStatus("current")
hostTopNControlTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 5, 1),
)
if mibBuilder.loadTexts:
    hostTopNControlTable.setStatus("current")
hostTopNControlEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1),
).setIndexNames((0, "RMON-MIB", "hostTopNControlIndex"))
if mibBuilder.loadTexts:
    hostTopNControlEntry.setStatus("current")
hostTopNControlIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostTopNControlIndex.setStatus("current")
hostTopNHostIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    hostTopNHostIndex.setStatus("current")
hostTopNRateBase = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7)))
    .clone(
        namedValues=NamedValues(
            ("hostTopNInPkts", 1),
            ("hostTopNOutPkts", 2),
            ("hostTopNInOctets", 3),
            ("hostTopNOutOctets", 4),
            ("hostTopNOutErrors", 5),
            ("hostTopNOutBroadcastPkts", 6),
            ("hostTopNOutMulticastPkts", 7),
        )
    ),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    hostTopNRateBase.setStatus("current")
hostTopNTimeRemaining = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 4), Integer32())
    .setUnits("Seconds")
    .setMaxAccess("readcreate")
)
if mibBuilder.loadTexts:
    hostTopNTimeRemaining.setStatus("current")
hostTopNDuration = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 5), Integer32())
    .setUnits("Seconds")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    hostTopNDuration.setStatus("current")
hostTopNRequestedSize = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 6), Integer32().clone(10)
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    hostTopNRequestedSize.setStatus("current")
hostTopNGrantedSize = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 7), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostTopNGrantedSize.setStatus("current")
hostTopNStartTime = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 8), TimeTicks()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostTopNStartTime.setStatus("current")
hostTopNOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 9), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    hostTopNOwner.setStatus("current")
hostTopNStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 1, 1, 10), EntryStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    hostTopNStatus.setStatus("current")
hostTopNTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 5, 2),
)
if mibBuilder.loadTexts:
    hostTopNTable.setStatus("current")
hostTopNEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 5, 2, 1),
).setIndexNames((0, "RMON-MIB", "hostTopNReport"), (0, "RMON-MIB", "hostTopNIndex"))
if mibBuilder.loadTexts:
    hostTopNEntry.setStatus("current")
hostTopNReport = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostTopNReport.setStatus("current")
hostTopNIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostTopNIndex.setStatus("current")
hostTopNAddress = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 3), OctetString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostTopNAddress.setStatus("current")
hostTopNRate = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 5, 2, 1, 4), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    hostTopNRate.setStatus("current")
matrixControlTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 6, 1),
)
if mibBuilder.loadTexts:
    matrixControlTable.setStatus("current")
matrixControlEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1),
).setIndexNames((0, "RMON-MIB", "matrixControlIndex"))
if mibBuilder.loadTexts:
    matrixControlEntry.setStatus("current")
matrixControlIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    matrixControlIndex.setStatus("current")
matrixControlDataSource = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 2), ObjectIdentifier()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    matrixControlDataSource.setStatus("current")
matrixControlTableSize = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 3), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    matrixControlTableSize.setStatus("current")
matrixControlLastDeleteTime = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 4), TimeTicks()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    matrixControlLastDeleteTime.setStatus("current")
matrixControlOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 5), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    matrixControlOwner.setStatus("current")
matrixControlStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 1, 1, 6), EntryStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    matrixControlStatus.setStatus("current")
matrixSDTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 6, 2),
)
if mibBuilder.loadTexts:
    matrixSDTable.setStatus("current")
matrixSDEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 6, 2, 1),).setIndexNames(
    (0, "RMON-MIB", "matrixSDIndex"),
    (0, "RMON-MIB", "matrixSDSourceAddress"),
    (0, "RMON-MIB", "matrixSDDestAddress"),
)
if mibBuilder.loadTexts:
    matrixSDEntry.setStatus("current")
matrixSDSourceAddress = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 1), OctetString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    matrixSDSourceAddress.setStatus("current")
matrixSDDestAddress = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 2), OctetString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    matrixSDDestAddress.setStatus("current")
matrixSDIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 3),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    matrixSDIndex.setStatus("current")
matrixSDPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 4), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    matrixSDPkts.setStatus("current")
matrixSDOctets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 5), Counter32())
    .setUnits("Octets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    matrixSDOctets.setStatus("current")
matrixSDErrors = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 2, 1, 6), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    matrixSDErrors.setStatus("current")
matrixDSTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 6, 3),
)
if mibBuilder.loadTexts:
    matrixDSTable.setStatus("current")
matrixDSEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 6, 3, 1),).setIndexNames(
    (0, "RMON-MIB", "matrixDSIndex"),
    (0, "RMON-MIB", "matrixDSDestAddress"),
    (0, "RMON-MIB", "matrixDSSourceAddress"),
)
if mibBuilder.loadTexts:
    matrixDSEntry.setStatus("current")
matrixDSSourceAddress = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 1), OctetString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    matrixDSSourceAddress.setStatus("current")
matrixDSDestAddress = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 2), OctetString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    matrixDSDestAddress.setStatus("current")
matrixDSIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 3),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    matrixDSIndex.setStatus("current")
matrixDSPkts = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 4), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    matrixDSPkts.setStatus("current")
matrixDSOctets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 5), Counter32())
    .setUnits("Octets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    matrixDSOctets.setStatus("current")
matrixDSErrors = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 6, 3, 1, 6), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    matrixDSErrors.setStatus("current")
filterTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 7, 1),
)
if mibBuilder.loadTexts:
    filterTable.setStatus("current")
filterEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1),
).setIndexNames((0, "RMON-MIB", "filterIndex"))
if mibBuilder.loadTexts:
    filterEntry.setStatus("current")
filterIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    filterIndex.setStatus("current")
filterChannelIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    filterChannelIndex.setStatus("current")
filterPktDataOffset = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 3), Integer32())
    .setUnits("Octets")
    .setMaxAccess("readcreate")
)
if mibBuilder.loadTexts:
    filterPktDataOffset.setStatus("current")
filterPktData = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 4), OctetString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    filterPktData.setStatus("current")
filterPktDataMask = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 5), OctetString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    filterPktDataMask.setStatus("current")
filterPktDataNotMask = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 6), OctetString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    filterPktDataNotMask.setStatus("current")
filterPktStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 7), Integer32()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    filterPktStatus.setStatus("current")
filterPktStatusMask = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 8), Integer32()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    filterPktStatusMask.setStatus("current")
filterPktStatusNotMask = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 9), Integer32()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    filterPktStatusNotMask.setStatus("current")
filterOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 10), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    filterOwner.setStatus("current")
filterStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 1, 1, 11), EntryStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    filterStatus.setStatus("current")
channelTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 7, 2),
)
if mibBuilder.loadTexts:
    channelTable.setStatus("current")
channelEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1),
).setIndexNames((0, "RMON-MIB", "channelIndex"))
if mibBuilder.loadTexts:
    channelEntry.setStatus("current")
channelIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    channelIndex.setStatus("current")
channelIfIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    channelIfIndex.setStatus("current")
channelAcceptType = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("acceptMatched", 1), ("acceptFailed", 2))),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    channelAcceptType.setStatus("current")
channelDataControl = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 4),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("on", 1), ("off", 2)))
    .clone("off"),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    channelDataControl.setStatus("current")
channelTurnOnEventIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 5),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    channelTurnOnEventIndex.setStatus("current")
channelTurnOffEventIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 6),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    channelTurnOffEventIndex.setStatus("current")
channelEventIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 7),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    channelEventIndex.setStatus("current")
channelEventStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 8),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(
        namedValues=NamedValues(
            ("eventReady", 1), ("eventFired", 2), ("eventAlwaysReady", 3)
        )
    )
    .clone("eventReady"),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    channelEventStatus.setStatus("current")
channelMatches = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 9), Counter32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    channelMatches.setStatus("current")
channelDescription = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 10),
    DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    channelDescription.setStatus("current")
channelOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 11), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    channelOwner.setStatus("current")
channelStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 7, 2, 1, 12), EntryStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    channelStatus.setStatus("current")
bufferControlTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 8, 1),
)
if mibBuilder.loadTexts:
    bufferControlTable.setStatus("current")
bufferControlEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1),
).setIndexNames((0, "RMON-MIB", "bufferControlIndex"))
if mibBuilder.loadTexts:
    bufferControlEntry.setStatus("current")
bufferControlIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    bufferControlIndex.setStatus("current")
bufferControlChannelIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    bufferControlChannelIndex.setStatus("current")
bufferControlFullStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("spaceAvailable", 1), ("full", 2))),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    bufferControlFullStatus.setStatus("current")
bufferControlFullAction = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 4),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("lockWhenFull", 1), ("wrapWhenFull", 2))),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    bufferControlFullAction.setStatus("current")
bufferControlCaptureSliceSize = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 5), Integer32().clone(100))
    .setUnits("Octets")
    .setMaxAccess("readcreate")
)
if mibBuilder.loadTexts:
    bufferControlCaptureSliceSize.setStatus("current")
bufferControlDownloadSliceSize = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 6), Integer32().clone(100))
    .setUnits("Octets")
    .setMaxAccess("readcreate")
)
if mibBuilder.loadTexts:
    bufferControlDownloadSliceSize.setStatus("current")
bufferControlDownloadOffset = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 7), Integer32())
    .setUnits("Octets")
    .setMaxAccess("readcreate")
)
if mibBuilder.loadTexts:
    bufferControlDownloadOffset.setStatus("current")
bufferControlMaxOctetsRequested = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 8), Integer32().clone(-1))
    .setUnits("Octets")
    .setMaxAccess("readcreate")
)
if mibBuilder.loadTexts:
    bufferControlMaxOctetsRequested.setStatus("current")
bufferControlMaxOctetsGranted = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 9), Integer32())
    .setUnits("Octets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    bufferControlMaxOctetsGranted.setStatus("current")
bufferControlCapturedPackets = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 10), Integer32())
    .setUnits("Packets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    bufferControlCapturedPackets.setStatus("current")
bufferControlTurnOnTime = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 11), TimeTicks()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    bufferControlTurnOnTime.setStatus("current")
bufferControlOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 12), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    bufferControlOwner.setStatus("current")
bufferControlStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 1, 1, 13), EntryStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    bufferControlStatus.setStatus("current")
captureBufferTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 8, 2),
)
if mibBuilder.loadTexts:
    captureBufferTable.setStatus("current")
captureBufferEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 8, 2, 1),).setIndexNames(
    (0, "RMON-MIB", "captureBufferControlIndex"), (0, "RMON-MIB", "captureBufferIndex")
)
if mibBuilder.loadTexts:
    captureBufferEntry.setStatus("current")
captureBufferControlIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    captureBufferControlIndex.setStatus("current")
captureBufferIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    captureBufferIndex.setStatus("current")
captureBufferPacketID = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 3), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    captureBufferPacketID.setStatus("current")
captureBufferPacketData = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 4), OctetString()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    captureBufferPacketData.setStatus("current")
captureBufferPacketLength = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 5), Integer32())
    .setUnits("Octets")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    captureBufferPacketLength.setStatus("current")
captureBufferPacketTime = (
    MibTableColumn((1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 6), Integer32())
    .setUnits("Milliseconds")
    .setMaxAccess("readonly")
)
if mibBuilder.loadTexts:
    captureBufferPacketTime.setStatus("current")
captureBufferPacketStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 8, 2, 1, 7), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    captureBufferPacketStatus.setStatus("current")
eventTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 9, 1),
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
eventEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1),
).setIndexNames((0, "RMON-MIB", "eventIndex"))
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
eventIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    eventIndex.setStatus("current")
eventDescription = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 2),
    DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    eventDescription.setStatus("current")
eventType = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4)))
    .clone(
        namedValues=NamedValues(
            ("none", 1), ("log", 2), ("snmptrap", 3), ("logandtrap", 4)
        )
    ),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
eventCommunity = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 4),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127)),
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    eventCommunity.setStatus("current")
eventLastTimeSent = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 5), TimeTicks()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    eventLastTimeSent.setStatus("current")
eventOwner = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 6), OwnerString()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    eventOwner.setStatus("current")
eventStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 7), EntryStatus()
).setMaxAccess("readcreate")
if mibBuilder.loadTexts:
    eventStatus.setStatus("current")
logTable = MibTable(
    (1, 3, 6, 1, 2, 1, 16, 9, 2),
)
if mibBuilder.loadTexts:
    logTable.setStatus("current")
logEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1),
).setIndexNames((0, "RMON-MIB", "logEventIndex"), (0, "RMON-MIB", "logIndex"))
if mibBuilder.loadTexts:
    logEntry.setStatus("current")
logEventIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    logEventIndex.setStatus("current")
logIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    logIndex.setStatus("current")
logTime = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 3), TimeTicks()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    logTime.setStatus("current")
logDescription = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 4),
    DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    logDescription.setStatus("current")
rmonEventsV2 = ObjectIdentity((1, 3, 6, 1, 2, 1, 16, 0))
if mibBuilder.loadTexts:
    rmonEventsV2.setStatus("current")
risingAlarm = NotificationType((1, 3, 6, 1, 2, 1, 16, 0, 1)).setObjects(
    ("RMON-MIB", "alarmIndex"),
    ("RMON-MIB", "alarmVariable"),
    ("RMON-MIB", "alarmSampleType"),
    ("RMON-MIB", "alarmValue"),
    ("RMON-MIB", "alarmRisingThreshold"),
)
if mibBuilder.loadTexts:
    risingAlarm.setStatus("current")
fallingAlarm = NotificationType((1, 3, 6, 1, 2, 1, 16, 0, 2)).setObjects(
    ("RMON-MIB", "alarmIndex"),
    ("RMON-MIB", "alarmVariable"),
    ("RMON-MIB", "alarmSampleType"),
    ("RMON-MIB", "alarmValue"),
    ("RMON-MIB", "alarmFallingThreshold"),
)
if mibBuilder.loadTexts:
    fallingAlarm.setStatus("current")
rmonCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 20, 9))
rmonGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 20, 10))
rmonCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 20, 9, 1)).setObjects(
    ("RMON-MIB", "rmonEtherStatsGroup"),
    ("RMON-MIB", "rmonHistoryControlGroup"),
    ("RMON-MIB", "rmonEthernetHistoryGroup"),
    ("RMON-MIB", "rmonAlarmGroup"),
    ("RMON-MIB", "rmonHostGroup"),
    ("RMON-MIB", "rmonHostTopNGroup"),
    ("RMON-MIB", "rmonMatrixGroup"),
    ("RMON-MIB", "rmonFilterGroup"),
    ("RMON-MIB", "rmonPacketCaptureGroup"),
    ("RMON-MIB", "rmonEventGroup"),
)

if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonCompliance = rmonCompliance.setStatus("current")
rmonEtherStatsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 10, 1)).setObjects(
    ("RMON-MIB", "etherStatsIndex"),
    ("RMON-MIB", "etherStatsDataSource"),
    ("RMON-MIB", "etherStatsDropEvents"),
    ("RMON-MIB", "etherStatsOctets"),
    ("RMON-MIB", "etherStatsPkts"),
    ("RMON-MIB", "etherStatsBroadcastPkts"),
    ("RMON-MIB", "etherStatsMulticastPkts"),
    ("RMON-MIB", "etherStatsCRCAlignErrors"),
    ("RMON-MIB", "etherStatsUndersizePkts"),
    ("RMON-MIB", "etherStatsOversizePkts"),
    ("RMON-MIB", "etherStatsFragments"),
    ("RMON-MIB", "etherStatsJabbers"),
    ("RMON-MIB", "etherStatsCollisions"),
    ("RMON-MIB", "etherStatsPkts64Octets"),
    ("RMON-MIB", "etherStatsPkts65to127Octets"),
    ("RMON-MIB", "etherStatsPkts128to255Octets"),
    ("RMON-MIB", "etherStatsPkts256to511Octets"),
    ("RMON-MIB", "etherStatsPkts512to1023Octets"),
    ("RMON-MIB", "etherStatsPkts1024to1518Octets"),
    ("RMON-MIB", "etherStatsOwner"),
    ("RMON-MIB", "etherStatsStatus"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonEtherStatsGroup = rmonEtherStatsGroup.setStatus("current")
rmonHistoryControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 10, 2)).setObjects(
    ("RMON-MIB", "historyControlIndex"),
    ("RMON-MIB", "historyControlDataSource"),
    ("RMON-MIB", "historyControlBucketsRequested"),
    ("RMON-MIB", "historyControlBucketsGranted"),
    ("RMON-MIB", "historyControlInterval"),
    ("RMON-MIB", "historyControlOwner"),
    ("RMON-MIB", "historyControlStatus"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonHistoryControlGroup = rmonHistoryControlGroup.setStatus("current")
rmonEthernetHistoryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 10, 3)).setObjects(
    ("RMON-MIB", "etherHistoryIndex"),
    ("RMON-MIB", "etherHistorySampleIndex"),
    ("RMON-MIB", "etherHistoryIntervalStart"),
    ("RMON-MIB", "etherHistoryDropEvents"),
    ("RMON-MIB", "etherHistoryOctets"),
    ("RMON-MIB", "etherHistoryPkts"),
    ("RMON-MIB", "etherHistoryBroadcastPkts"),
    ("RMON-MIB", "etherHistoryMulticastPkts"),
    ("RMON-MIB", "etherHistoryCRCAlignErrors"),
    ("RMON-MIB", "etherHistoryUndersizePkts"),
    ("RMON-MIB", "etherHistoryOversizePkts"),
    ("RMON-MIB", "etherHistoryFragments"),
    ("RMON-MIB", "etherHistoryJabbers"),
    ("RMON-MIB", "etherHistoryCollisions"),
    ("RMON-MIB", "etherHistoryUtilization"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonEthernetHistoryGroup = rmonEthernetHistoryGroup.setStatus("current")
rmonAlarmGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 10, 4)).setObjects(
    ("RMON-MIB", "alarmIndex"),
    ("RMON-MIB", "alarmInterval"),
    ("RMON-MIB", "alarmVariable"),
    ("RMON-MIB", "alarmSampleType"),
    ("RMON-MIB", "alarmValue"),
    ("RMON-MIB", "alarmStartupAlarm"),
    ("RMON-MIB", "alarmRisingThreshold"),
    ("RMON-MIB", "alarmFallingThreshold"),
    ("RMON-MIB", "alarmRisingEventIndex"),
    ("RMON-MIB", "alarmFallingEventIndex"),
    ("RMON-MIB", "alarmOwner"),
    ("RMON-MIB", "alarmStatus"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonAlarmGroup = rmonAlarmGroup.setStatus("current")
rmonHostGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 10, 5)).setObjects(
    ("RMON-MIB", "hostControlIndex"),
    ("RMON-MIB", "hostControlDataSource"),
    ("RMON-MIB", "hostControlTableSize"),
    ("RMON-MIB", "hostControlLastDeleteTime"),
    ("RMON-MIB", "hostControlOwner"),
    ("RMON-MIB", "hostControlStatus"),
    ("RMON-MIB", "hostAddress"),
    ("RMON-MIB", "hostCreationOrder"),
    ("RMON-MIB", "hostIndex"),
    ("RMON-MIB", "hostInPkts"),
    ("RMON-MIB", "hostOutPkts"),
    ("RMON-MIB", "hostInOctets"),
    ("RMON-MIB", "hostOutOctets"),
    ("RMON-MIB", "hostOutErrors"),
    ("RMON-MIB", "hostOutBroadcastPkts"),
    ("RMON-MIB", "hostOutMulticastPkts"),
    ("RMON-MIB", "hostTimeAddress"),
    ("RMON-MIB", "hostTimeCreationOrder"),
    ("RMON-MIB", "hostTimeIndex"),
    ("RMON-MIB", "hostTimeInPkts"),
    ("RMON-MIB", "hostTimeOutPkts"),
    ("RMON-MIB", "hostTimeInOctets"),
    ("RMON-MIB", "hostTimeOutOctets"),
    ("RMON-MIB", "hostTimeOutErrors"),
    ("RMON-MIB", "hostTimeOutBroadcastPkts"),
    ("RMON-MIB", "hostTimeOutMulticastPkts"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonHostGroup = rmonHostGroup.setStatus("current")
rmonHostTopNGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 10, 6)).setObjects(
    ("RMON-MIB", "hostTopNControlIndex"),
    ("RMON-MIB", "hostTopNHostIndex"),
    ("RMON-MIB", "hostTopNRateBase"),
    ("RMON-MIB", "hostTopNTimeRemaining"),
    ("RMON-MIB", "hostTopNDuration"),
    ("RMON-MIB", "hostTopNRequestedSize"),
    ("RMON-MIB", "hostTopNGrantedSize"),
    ("RMON-MIB", "hostTopNStartTime"),
    ("RMON-MIB", "hostTopNOwner"),
    ("RMON-MIB", "hostTopNStatus"),
    ("RMON-MIB", "hostTopNReport"),
    ("RMON-MIB", "hostTopNIndex"),
    ("RMON-MIB", "hostTopNAddress"),
    ("RMON-MIB", "hostTopNRate"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonHostTopNGroup = rmonHostTopNGroup.setStatus("current")
rmonMatrixGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 10, 7)).setObjects(
    ("RMON-MIB", "matrixControlIndex"),
    ("RMON-MIB", "matrixControlDataSource"),
    ("RMON-MIB", "matrixControlTableSize"),
    ("RMON-MIB", "matrixControlLastDeleteTime"),
    ("RMON-MIB", "matrixControlOwner"),
    ("RMON-MIB", "matrixControlStatus"),
    ("RMON-MIB", "matrixSDSourceAddress"),
    ("RMON-MIB", "matrixSDDestAddress"),
    ("RMON-MIB", "matrixSDIndex"),
    ("RMON-MIB", "matrixSDPkts"),
    ("RMON-MIB", "matrixSDOctets"),
    ("RMON-MIB", "matrixSDErrors"),
    ("RMON-MIB", "matrixDSSourceAddress"),
    ("RMON-MIB", "matrixDSDestAddress"),
    ("RMON-MIB", "matrixDSIndex"),
    ("RMON-MIB", "matrixDSPkts"),
    ("RMON-MIB", "matrixDSOctets"),
    ("RMON-MIB", "matrixDSErrors"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonMatrixGroup = rmonMatrixGroup.setStatus("current")
rmonFilterGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 10, 8)).setObjects(
    ("RMON-MIB", "filterIndex"),
    ("RMON-MIB", "filterChannelIndex"),
    ("RMON-MIB", "filterPktDataOffset"),
    ("RMON-MIB", "filterPktData"),
    ("RMON-MIB", "filterPktDataMask"),
    ("RMON-MIB", "filterPktDataNotMask"),
    ("RMON-MIB", "filterPktStatus"),
    ("RMON-MIB", "filterPktStatusMask"),
    ("RMON-MIB", "filterPktStatusNotMask"),
    ("RMON-MIB", "filterOwner"),
    ("RMON-MIB", "filterStatus"),
    ("RMON-MIB", "channelIndex"),
    ("RMON-MIB", "channelIfIndex"),
    ("RMON-MIB", "channelAcceptType"),
    ("RMON-MIB", "channelDataControl"),
    ("RMON-MIB", "channelTurnOnEventIndex"),
    ("RMON-MIB", "channelTurnOffEventIndex"),
    ("RMON-MIB", "channelEventIndex"),
    ("RMON-MIB", "channelEventStatus"),
    ("RMON-MIB", "channelMatches"),
    ("RMON-MIB", "channelDescription"),
    ("RMON-MIB", "channelOwner"),
    ("RMON-MIB", "channelStatus"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonFilterGroup = rmonFilterGroup.setStatus("current")
rmonPacketCaptureGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 10, 9)).setObjects(
    ("RMON-MIB", "bufferControlIndex"),
    ("RMON-MIB", "bufferControlChannelIndex"),
    ("RMON-MIB", "bufferControlFullStatus"),
    ("RMON-MIB", "bufferControlFullAction"),
    ("RMON-MIB", "bufferControlCaptureSliceSize"),
    ("RMON-MIB", "bufferControlDownloadSliceSize"),
    ("RMON-MIB", "bufferControlDownloadOffset"),
    ("RMON-MIB", "bufferControlMaxOctetsRequested"),
    ("RMON-MIB", "bufferControlMaxOctetsGranted"),
    ("RMON-MIB", "bufferControlCapturedPackets"),
    ("RMON-MIB", "bufferControlTurnOnTime"),
    ("RMON-MIB", "bufferControlOwner"),
    ("RMON-MIB", "bufferControlStatus"),
    ("RMON-MIB", "captureBufferControlIndex"),
    ("RMON-MIB", "captureBufferIndex"),
    ("RMON-MIB", "captureBufferPacketID"),
    ("RMON-MIB", "captureBufferPacketData"),
    ("RMON-MIB", "captureBufferPacketLength"),
    ("RMON-MIB", "captureBufferPacketTime"),
    ("RMON-MIB", "captureBufferPacketStatus"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonPacketCaptureGroup = rmonPacketCaptureGroup.setStatus("current")
rmonEventGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 20, 10, 10)).setObjects(
    ("RMON-MIB", "eventIndex"),
    ("RMON-MIB", "eventDescription"),
    ("RMON-MIB", "eventType"),
    ("RMON-MIB", "eventCommunity"),
    ("RMON-MIB", "eventLastTimeSent"),
    ("RMON-MIB", "eventOwner"),
    ("RMON-MIB", "eventStatus"),
    ("RMON-MIB", "logEventIndex"),
    ("RMON-MIB", "logIndex"),
    ("RMON-MIB", "logTime"),
    ("RMON-MIB", "logDescription"),
)
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonEventGroup = rmonEventGroup.setStatus("current")
rmonNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 16, 20, 10, 11)
).setObjects(("RMON-MIB", "risingAlarm"), ("RMON-MIB", "fallingAlarm"))
if getattr(mibBuilder, "version", (0, 0, 0)) > (4, 4, 0):
    rmonNotificationGroup = rmonNotificationGroup.setStatus("current")
mibBuilder.exportSymbols(
    "RMON-MIB",
    captureBufferControlIndex=captureBufferControlIndex,
    captureBufferPacketStatus=captureBufferPacketStatus,
    historyControlStatus=historyControlStatus,
    EntryStatus=EntryStatus,
    hostControlStatus=hostControlStatus,
    bufferControlChannelIndex=bufferControlChannelIndex,
    matrixControlOwner=matrixControlOwner,
    matrixControlEntry=matrixControlEntry,
    filterPktData=filterPktData,
    hostTopNEntry=hostTopNEntry,
    statistics=statistics,
    matrixDSErrors=matrixDSErrors,
    rmonPacketCaptureGroup=rmonPacketCaptureGroup,
    matrixDSTable=matrixDSTable,
    etherHistoryDropEvents=etherHistoryDropEvents,
    captureBufferTable=captureBufferTable,
    etherHistoryUtilization=etherHistoryUtilization,
    matrixDSOctets=matrixDSOctets,
    rmonMatrixGroup=rmonMatrixGroup,
    hostTopN=hostTopN,
    logDescription=logDescription,
    rmonEtherStatsGroup=rmonEtherStatsGroup,
    hostTimeOutPkts=hostTimeOutPkts,
    hostTopNRateBase=hostTopNRateBase,
    logEventIndex=logEventIndex,
    rmonHostTopNGroup=rmonHostTopNGroup,
    matrixControlTable=matrixControlTable,
    matrixControlIndex=matrixControlIndex,
    rmonNotificationGroup=rmonNotificationGroup,
    rmonAlarmGroup=rmonAlarmGroup,
    matrixDSEntry=matrixDSEntry,
    alarmStatus=alarmStatus,
    logTime=logTime,
    matrixDSDestAddress=matrixDSDestAddress,
    etherStatsPkts128to255Octets=etherStatsPkts128to255Octets,
    rmonCompliances=rmonCompliances,
    hostTopNGrantedSize=hostTopNGrantedSize,
    etherHistoryCRCAlignErrors=etherHistoryCRCAlignErrors,
    bufferControlFullAction=bufferControlFullAction,
    bufferControlMaxOctetsGranted=bufferControlMaxOctetsGranted,
    capture=capture,
    etherStatsOwner=etherStatsOwner,
    matrixControlDataSource=matrixControlDataSource,
    filterPktDataOffset=filterPktDataOffset,
    channelTurnOffEventIndex=channelTurnOffEventIndex,
    etherStatsCRCAlignErrors=etherStatsCRCAlignErrors,
    hostCreationOrder=hostCreationOrder,
    hostTopNTimeRemaining=hostTopNTimeRemaining,
    rmon=rmon,
    filterPktDataMask=filterPktDataMask,
    etherHistoryFragments=etherHistoryFragments,
    hostOutOctets=hostOutOctets,
    channelIfIndex=channelIfIndex,
    hostOutBroadcastPkts=hostOutBroadcastPkts,
    rmonEventGroup=rmonEventGroup,
    eventLastTimeSent=eventLastTimeSent,
    etherHistoryMulticastPkts=etherHistoryMulticastPkts,
    hostTimeOutMulticastPkts=hostTimeOutMulticastPkts,
    historyControlBucketsRequested=historyControlBucketsRequested,
    filterIndex=filterIndex,
    bufferControlIndex=bufferControlIndex,
    etherStatsBroadcastPkts=etherStatsBroadcastPkts,
    alarmRisingThreshold=alarmRisingThreshold,
    alarm=alarm,
    alarmTable=alarmTable,
    alarmSampleType=alarmSampleType,
    hostTimeAddress=hostTimeAddress,
    matrixControlStatus=matrixControlStatus,
    eventStatus=eventStatus,
    rmonEthernetHistoryGroup=rmonEthernetHistoryGroup,
    etherStatsPkts=etherStatsPkts,
    hostTopNStartTime=hostTopNStartTime,
    PYSNMP_MODULE_ID=rmonMibModule,
    bufferControlDownloadSliceSize=bufferControlDownloadSliceSize,
    captureBufferPacketTime=captureBufferPacketTime,
    channelIndex=channelIndex,
    etherStatsTable=etherStatsTable,
    hostTimeTable=hostTimeTable,
    bufferControlCaptureSliceSize=bufferControlCaptureSliceSize,
    alarmIndex=alarmIndex,
    captureBufferPacketLength=captureBufferPacketLength,
    channelTurnOnEventIndex=channelTurnOnEventIndex,
    etherHistoryCollisions=etherHistoryCollisions,
    alarmInterval=alarmInterval,
    rmonFilterGroup=rmonFilterGroup,
    fallingAlarm=fallingAlarm,
    bufferControlTable=bufferControlTable,
    etherStatsOversizePkts=etherStatsOversizePkts,
    rmonMibModule=rmonMibModule,
    etherStatsCollisions=etherStatsCollisions,
    historyControlTable=historyControlTable,
    alarmVariable=alarmVariable,
    channelStatus=channelStatus,
    etherHistoryOctets=etherHistoryOctets,
    matrix=matrix,
    hostTopNControlTable=hostTopNControlTable,
    etherStatsDropEvents=etherStatsDropEvents,
    filterPktStatusMask=filterPktStatusMask,
    filterChannelIndex=filterChannelIndex,
    captureBufferPacketID=captureBufferPacketID,
    matrixSDErrors=matrixSDErrors,
    etherStatsPkts256to511Octets=etherStatsPkts256to511Octets,
    filterTable=filterTable,
    hostTimeInOctets=hostTimeInOctets,
    rmonHostGroup=rmonHostGroup,
    hostOutPkts=hostOutPkts,
    hostTimeCreationOrder=hostTimeCreationOrder,
    hostTimeIndex=hostTimeIndex,
    matrixControlTableSize=matrixControlTableSize,
    etherStatsIndex=etherStatsIndex,
    etherStatsMulticastPkts=etherStatsMulticastPkts,
    historyControlOwner=historyControlOwner,
    filter=filter,
    hostTopNOwner=hostTopNOwner,
    matrixDSSourceAddress=matrixDSSourceAddress,
    etherHistorySampleIndex=etherHistorySampleIndex,
    event=event,
    channelEventStatus=channelEventStatus,
    matrixSDPkts=matrixSDPkts,
    hostIndex=hostIndex,
    filterOwner=filterOwner,
    channelDataControl=channelDataControl,
    captureBufferPacketData=captureBufferPacketData,
    channelTable=channelTable,
    matrixDSIndex=matrixDSIndex,
    bufferControlEntry=bufferControlEntry,
    channelMatches=channelMatches,
    alarmStartupAlarm=alarmStartupAlarm,
    hostTable=hostTable,
    etherStatsUndersizePkts=etherStatsUndersizePkts,
    alarmFallingThreshold=alarmFallingThreshold,
    etherStatsPkts64Octets=etherStatsPkts64Octets,
    hostTopNRequestedSize=hostTopNRequestedSize,
    filterPktStatus=filterPktStatus,
    eventCommunity=eventCommunity,
    hostTimeOutOctets=hostTimeOutOctets,
    etherHistoryJabbers=etherHistoryJabbers,
    etherStatsFragments=etherStatsFragments,
    alarmValue=alarmValue,
    bufferControlCapturedPackets=bufferControlCapturedPackets,
    matrixSDTable=matrixSDTable,
    hostTimeOutBroadcastPkts=hostTimeOutBroadcastPkts,
    eventIndex=eventIndex,
    alarmOwner=alarmOwner,
    channelDescription=channelDescription,
    history=history,
    captureBufferIndex=captureBufferIndex,
    hostControlLastDeleteTime=hostControlLastDeleteTime,
    hostTimeEntry=hostTimeEntry,
    channelEntry=channelEntry,
    historyControlIndex=historyControlIndex,
    bufferControlTurnOnTime=bufferControlTurnOnTime,
    historyControlEntry=historyControlEntry,
    rmonCompliance=rmonCompliance,
    rmonHistoryControlGroup=rmonHistoryControlGroup,
    historyControlBucketsGranted=historyControlBucketsGranted,
    captureBufferEntry=captureBufferEntry,
    filterEntry=filterEntry,
    filterPktDataNotMask=filterPktDataNotMask,
    alarmFallingEventIndex=alarmFallingEventIndex,
    logIndex=logIndex,
    matrixControlLastDeleteTime=matrixControlLastDeleteTime,
    eventTable=eventTable,
    etherStatsEntry=etherStatsEntry,
    hostOutErrors=hostOutErrors,
    matrixSDSourceAddress=matrixSDSourceAddress,
    matrixSDOctets=matrixSDOctets,
    hostControlIndex=hostControlIndex,
    OwnerString=OwnerString,
    hostTimeInPkts=hostTimeInPkts,
    bufferControlStatus=bufferControlStatus,
    alarmRisingEventIndex=alarmRisingEventIndex,
    hostTopNReport=hostTopNReport,
    etherHistoryPkts=etherHistoryPkts,
    etherStatsPkts65to127Octets=etherStatsPkts65to127Octets,
    hostOutMulticastPkts=hostOutMulticastPkts,
    eventDescription=eventDescription,
    etherHistoryEntry=etherHistoryEntry,
    hostTopNIndex=hostTopNIndex,
    channelEventIndex=channelEventIndex,
    eventType=eventType,
    etherHistoryBroadcastPkts=etherHistoryBroadcastPkts,
    channelAcceptType=channelAcceptType,
    hostControlDataSource=hostControlDataSource,
    rmonConformance=rmonConformance,
    historyControlInterval=historyControlInterval,
    historyControlDataSource=historyControlDataSource,
    hostTopNControlIndex=hostTopNControlIndex,
    alarmEntry=alarmEntry,
    etherHistoryIntervalStart=etherHistoryIntervalStart,
    etherStatsJabbers=etherStatsJabbers,
    etherStatsStatus=etherStatsStatus,
    etherStatsDataSource=etherStatsDataSource,
    logTable=logTable,
    hostTopNHostIndex=hostTopNHostIndex,
    hostTopNStatus=hostTopNStatus,
    hosts=hosts,
    etherHistoryUndersizePkts=etherHistoryUndersizePkts,
    channelOwner=channelOwner,
    rmonGroups=rmonGroups,
    bufferControlFullStatus=bufferControlFullStatus,
    hostControlOwner=hostControlOwner,
    hostTopNDuration=hostTopNDuration,
    filterStatus=filterStatus,
    eventOwner=eventOwner,
    filterPktStatusNotMask=filterPktStatusNotMask,
    hostInPkts=hostInPkts,
    hostTopNControlEntry=hostTopNControlEntry,
    hostInOctets=hostInOctets,
    hostTopNAddress=hostTopNAddress,
    etherStatsOctets=etherStatsOctets,
    hostTopNRate=hostTopNRate,
    etherHistoryOversizePkts=etherHistoryOversizePkts,
    bufferControlDownloadOffset=bufferControlDownloadOffset,
    eventEntry=eventEntry,
    etherHistoryIndex=etherHistoryIndex,
    etherStatsPkts1024to1518Octets=etherStatsPkts1024to1518Octets,
    hostEntry=hostEntry,
    hostControlEntry=hostControlEntry,
    hostTimeOutErrors=hostTimeOutErrors,
    risingAlarm=risingAlarm,
    etherStatsPkts512to1023Octets=etherStatsPkts512to1023Octets,
    etherHistoryTable=etherHistoryTable,
    hostControlTable=hostControlTable,
    hostTopNTable=hostTopNTable,
    logEntry=logEntry,
    bufferControlMaxOctetsRequested=bufferControlMaxOctetsRequested,
    matrixSDEntry=matrixSDEntry,
    hostControlTableSize=hostControlTableSize,
    matrixSDDestAddress=matrixSDDestAddress,
    bufferControlOwner=bufferControlOwner,
    matrixDSPkts=matrixDSPkts,
    rmonEventsV2=rmonEventsV2,
    hostAddress=hostAddress,
    matrixSDIndex=matrixSDIndex,
)
