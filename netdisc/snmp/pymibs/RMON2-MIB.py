#
# PySNMP MIB module RMON2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///mibs.thola.io/asn1/RMON2-MIB
# Produced by pysmi-0.3.4 at Tue Mar 29 10:05:57 2022
# On host dump platform Linux version 5.4.0-100-generic by user rwd
# Using Python version 3.10.4 (main, Mar 24 2022, 16:12:56) [GCC 9.4.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols(
    "ASN1", "OctetString", "ObjectIdentifier", "Integer"
)
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(
    ValueSizeConstraint,
    ConstraintsUnion,
    ConstraintsIntersection,
    SingleValueConstraint,
    ValueRangeConstraint,
) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ValueSizeConstraint",
    "ConstraintsUnion",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
)
(ifIndex,) = mibBuilder.importSymbols("IF-MIB", "ifIndex")
(
    etherStatsEntry,
    channelEntry,
    history,
    matrix,
    hostControlEntry,
    OwnerString,
    statistics,
    filterEntry,
    hosts,
    historyControlEntry,
    matrixControlEntry,
    filter,
) = mibBuilder.importSymbols(
    "RMON-MIB",
    "etherStatsEntry",
    "channelEntry",
    "history",
    "matrix",
    "hostControlEntry",
    "OwnerString",
    "statistics",
    "filterEntry",
    "hosts",
    "historyControlEntry",
    "matrixControlEntry",
    "filter",
)
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols(
    "SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup"
)
(
    Gauge32,
    MibScalar,
    MibTable,
    MibTableRow,
    MibTableColumn,
    MibIdentifier,
    Unsigned32,
    Integer32,
    Bits,
    NotificationType,
    ModuleIdentity,
    TimeTicks,
    ObjectIdentity,
    iso,
    mib_2,
    IpAddress,
    Counter32,
    Counter64,
) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Gauge32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "MibIdentifier",
    "Unsigned32",
    "Integer32",
    "Bits",
    "NotificationType",
    "ModuleIdentity",
    "TimeTicks",
    "ObjectIdentity",
    "iso",
    "mib-2",
    "IpAddress",
    "Counter32",
    "Counter64",
)
RowStatus, TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols(
    "SNMPv2-TC", "RowStatus", "TimeStamp", "DisplayString", "TextualConvention"
)
rmon = ModuleIdentity((1, 3, 6, 1, 2, 1, 16))
if mibBuilder.loadTexts:
    rmon.setLastUpdated("9605270000Z")
if mibBuilder.loadTexts:
    rmon.setOrganization("IETF RMON MIB Working Group")
protocolDir = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 11))
protocolDist = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 12))
addressMap = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 13))
nlHost = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 14))
nlMatrix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 15))
alHost = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 16))
alMatrix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 17))
usrHistory = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 18))
probeConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 19))
rmonConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 20))


class ZeroBasedCounter32(TextualConvention, Gauge32):
    status = "current"


class LastCreateTime(TimeStamp):
    status = "current"


class TimeFilter(TextualConvention, TimeTicks):
    status = "current"


class DataSource(TextualConvention, ObjectIdentifier):
    status = "current"


mibBuilder.exportSymbols(
    "RMON2-MIB",
    ZeroBasedCounter32=ZeroBasedCounter32,
    addressMap=addressMap,
    protocolDist=protocolDist,
    usrHistory=usrHistory,
    rmon=rmon,
    nlHost=nlHost,
    protocolDir=protocolDir,
    probeConfig=probeConfig,
    alHost=alHost,
    TimeFilter=TimeFilter,
    DataSource=DataSource,
    alMatrix=alMatrix,
    PYSNMP_MODULE_ID=rmon,
    LastCreateTime=LastCreateTime,
    nlMatrix=nlMatrix,
    rmonConformance=rmonConformance,
)
