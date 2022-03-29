#
# PySNMP MIB module BRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///mibs.thola.io/asn1/BRIDGE-MIB
# Produced by pysmi-0.3.4 at Tue Mar 29 10:05:52 2022
# On host dump platform Linux version 5.4.0-100-generic by user rwd
# Using Python version 3.10.4 (main, Mar 24 2022, 16:12:56) [GCC 9.4.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols(
    "ASN1", "Integer", "ObjectIdentifier", "OctetString"
)
(NamedValues,) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
(
    ValueRangeConstraint,
    ValueSizeConstraint,
    ConstraintsIntersection,
    ConstraintsUnion,
    SingleValueConstraint,
) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
)
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols(
    "SNMPv2-CONF", "ModuleCompliance", "NotificationGroup"
)
(
    NotificationType,
    Bits,
    ModuleIdentity,
    Counter32,
    Integer32,
    Counter64,
    IpAddress,
    Gauge32,
    MibScalar,
    MibTable,
    MibTableRow,
    MibTableColumn,
    ObjectIdentity,
    iso,
    TimeTicks,
    Unsigned32,
    MibIdentifier,
    mib_2,
    NotificationType,
) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "NotificationType",
    "Bits",
    "ModuleIdentity",
    "Counter32",
    "Integer32",
    "Counter64",
    "IpAddress",
    "Gauge32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "ObjectIdentity",
    "iso",
    "TimeTicks",
    "Unsigned32",
    "MibIdentifier",
    "mib-2",
    "NotificationType",
)
DisplayString, TextualConvention = mibBuilder.importSymbols(
    "SNMPv2-TC", "DisplayString", "TextualConvention"
)


class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6


class BridgeId(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8


class Timeout(Integer32):
    pass


dot1dBridge = MibIdentifier((1, 3, 6, 1, 2, 1, 17))
dot1dBase = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 1))
dot1dStp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 2))
dot1dSr = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 3))
dot1dTp = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 4))
dot1dStatic = MibIdentifier((1, 3, 6, 1, 2, 1, 17, 5))
dot1dBaseBridgeAddress = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 1, 1), MacAddress()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dBaseBridgeAddress.setStatus("mandatory")
dot1dBaseNumPorts = MibScalar((1, 3, 6, 1, 2, 1, 17, 1, 2), Integer32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    dot1dBaseNumPorts.setStatus("mandatory")
dot1dBaseType = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4)))
    .clone(
        namedValues=NamedValues(
            ("unknown", 1), ("transparent-only", 2), ("sourceroute-only", 3), ("srt", 4)
        )
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dBaseType.setStatus("mandatory")
dot1dBasePortTable = MibTable(
    (1, 3, 6, 1, 2, 1, 17, 1, 4),
)
if mibBuilder.loadTexts:
    dot1dBasePortTable.setStatus("mandatory")
dot1dBasePortEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1),
).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"))
if mibBuilder.loadTexts:
    dot1dBasePortEntry.setStatus("mandatory")
dot1dBasePort = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dBasePort.setStatus("mandatory")
dot1dBasePortIfIndex = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 2), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dBasePortIfIndex.setStatus("mandatory")
dot1dBasePortCircuit = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 3), ObjectIdentifier()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dBasePortCircuit.setStatus("mandatory")
dot1dBasePortDelayExceededDiscards = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 4), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dBasePortDelayExceededDiscards.setStatus("mandatory")
dot1dBasePortMtuExceededDiscards = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 1, 4, 1, 5), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dBasePortMtuExceededDiscards.setStatus("mandatory")
dot1dStpProtocolSpecification = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 2, 1),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3)))
    .clone(namedValues=NamedValues(("unknown", 1), ("decLb100", 2), ("ieee8021d", 3))),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dStpProtocolSpecification.setStatus("mandatory")
dot1dStpPriority = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 2, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStpPriority.setStatus("mandatory")
dot1dStpTimeSinceTopologyChange = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 2, 3), TimeTicks()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dStpTimeSinceTopologyChange.setStatus("mandatory")
dot1dStpTopChanges = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 4), Counter32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    dot1dStpTopChanges.setStatus("mandatory")
dot1dStpDesignatedRoot = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 2, 5), BridgeId()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dStpDesignatedRoot.setStatus("mandatory")
dot1dStpRootCost = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 6), Integer32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    dot1dStpRootCost.setStatus("mandatory")
dot1dStpRootPort = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 7), Integer32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    dot1dStpRootPort.setStatus("mandatory")
dot1dStpMaxAge = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 8), Timeout()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    dot1dStpMaxAge.setStatus("mandatory")
dot1dStpHelloTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 9), Timeout()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    dot1dStpHelloTime.setStatus("mandatory")
dot1dStpHoldTime = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 10), Integer32()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    dot1dStpHoldTime.setStatus("mandatory")
dot1dStpForwardDelay = MibScalar((1, 3, 6, 1, 2, 1, 17, 2, 11), Timeout()).setMaxAccess(
    "readonly"
)
if mibBuilder.loadTexts:
    dot1dStpForwardDelay.setStatus("mandatory")
dot1dStpBridgeMaxAge = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 2, 12),
    Timeout().subtype(subtypeSpec=ValueRangeConstraint(600, 4000)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStpBridgeMaxAge.setStatus("mandatory")
dot1dStpBridgeHelloTime = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 2, 13),
    Timeout().subtype(subtypeSpec=ValueRangeConstraint(100, 1000)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStpBridgeHelloTime.setStatus("mandatory")
dot1dStpBridgeForwardDelay = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 2, 14),
    Timeout().subtype(subtypeSpec=ValueRangeConstraint(400, 3000)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStpBridgeForwardDelay.setStatus("mandatory")
dot1dStpPortTable = MibTable(
    (1, 3, 6, 1, 2, 1, 17, 2, 15),
)
if mibBuilder.loadTexts:
    dot1dStpPortTable.setStatus("mandatory")
dot1dStpPortEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1),
).setIndexNames((0, "BRIDGE-MIB", "dot1dStpPort"))
if mibBuilder.loadTexts:
    dot1dStpPortEntry.setStatus("mandatory")
dot1dStpPort = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dStpPort.setStatus("mandatory")
dot1dStpPortPriority = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStpPortPriority.setStatus("mandatory")
dot1dStpPortState = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6)))
    .clone(
        namedValues=NamedValues(
            ("disabled", 1),
            ("blocking", 2),
            ("listening", 3),
            ("learning", 4),
            ("forwarding", 5),
            ("broken", 6),
        )
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dStpPortState.setStatus("mandatory")
dot1dStpPortEnable = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 4),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2)))
    .clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStpPortEnable.setStatus("mandatory")
dot1dStpPortPathCost = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 5),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStpPortPathCost.setStatus("mandatory")
dot1dStpPortDesignatedRoot = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 6), BridgeId()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedRoot.setStatus("mandatory")
dot1dStpPortDesignatedCost = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 7), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedCost.setStatus("mandatory")
dot1dStpPortDesignatedBridge = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 8), BridgeId()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedBridge.setStatus("mandatory")
dot1dStpPortDesignatedPort = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 9),
    OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dStpPortDesignatedPort.setStatus("mandatory")
dot1dStpPortForwardTransitions = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 2, 15, 1, 10), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dStpPortForwardTransitions.setStatus("mandatory")
dot1dTpLearnedEntryDiscards = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 4, 1), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dTpLearnedEntryDiscards.setStatus("mandatory")
dot1dTpAgingTime = MibScalar(
    (1, 3, 6, 1, 2, 1, 17, 4, 2),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 1000000)),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dTpAgingTime.setStatus("mandatory")
dot1dTpFdbTable = MibTable(
    (1, 3, 6, 1, 2, 1, 17, 4, 3),
)
if mibBuilder.loadTexts:
    dot1dTpFdbTable.setStatus("mandatory")
dot1dTpFdbEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1),
).setIndexNames((0, "BRIDGE-MIB", "dot1dTpFdbAddress"))
if mibBuilder.loadTexts:
    dot1dTpFdbEntry.setStatus("mandatory")
dot1dTpFdbAddress = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 1), MacAddress()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dTpFdbAddress.setStatus("mandatory")
dot1dTpFdbPort = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 2), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dTpFdbPort.setStatus("mandatory")
dot1dTpFdbStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 4, 3, 1, 3),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5)))
    .clone(
        namedValues=NamedValues(
            ("other", 1), ("invalid", 2), ("learned", 3), ("self", 4), ("mgmt", 5)
        )
    ),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dTpFdbStatus.setStatus("mandatory")
dot1dTpPortTable = MibTable(
    (1, 3, 6, 1, 2, 1, 17, 4, 4),
)
if mibBuilder.loadTexts:
    dot1dTpPortTable.setStatus("mandatory")
dot1dTpPortEntry = MibTableRow(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1),
).setIndexNames((0, "BRIDGE-MIB", "dot1dTpPort"))
if mibBuilder.loadTexts:
    dot1dTpPortEntry.setStatus("mandatory")
dot1dTpPort = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 1),
    Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)),
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dTpPort.setStatus("mandatory")
dot1dTpPortMaxInfo = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 2), Integer32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dTpPortMaxInfo.setStatus("mandatory")
dot1dTpPortInFrames = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 3), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dTpPortInFrames.setStatus("mandatory")
dot1dTpPortOutFrames = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 4), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dTpPortOutFrames.setStatus("mandatory")
dot1dTpPortInDiscards = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 4, 4, 1, 5), Counter32()
).setMaxAccess("readonly")
if mibBuilder.loadTexts:
    dot1dTpPortInDiscards.setStatus("mandatory")
dot1dStaticTable = MibTable(
    (1, 3, 6, 1, 2, 1, 17, 5, 1),
)
if mibBuilder.loadTexts:
    dot1dStaticTable.setStatus("mandatory")
dot1dStaticEntry = MibTableRow((1, 3, 6, 1, 2, 1, 17, 5, 1, 1),).setIndexNames(
    (0, "BRIDGE-MIB", "dot1dStaticAddress"), (0, "BRIDGE-MIB", "dot1dStaticReceivePort")
)
if mibBuilder.loadTexts:
    dot1dStaticEntry.setStatus("mandatory")
dot1dStaticAddress = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 1), MacAddress()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStaticAddress.setStatus("mandatory")
dot1dStaticReceivePort = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 2), Integer32()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStaticReceivePort.setStatus("mandatory")
dot1dStaticAllowedToGoTo = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 3), OctetString()
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStaticAllowedToGoTo.setStatus("mandatory")
dot1dStaticStatus = MibTableColumn(
    (1, 3, 6, 1, 2, 1, 17, 5, 1, 1, 4),
    Integer32()
    .subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5)))
    .clone(
        namedValues=NamedValues(
            ("other", 1),
            ("invalid", 2),
            ("permanent", 3),
            ("deleteOnReset", 4),
            ("deleteOnTimeout", 5),
        )
    ),
).setMaxAccess("readwrite")
if mibBuilder.loadTexts:
    dot1dStaticStatus.setStatus("mandatory")
newRoot = NotificationType((1, 3, 6, 1, 2, 1, 17) + (0, 1))
topologyChange = NotificationType((1, 3, 6, 1, 2, 1, 17) + (0, 2))
mibBuilder.exportSymbols(
    "BRIDGE-MIB",
    dot1dTpPortTable=dot1dTpPortTable,
    dot1dTpFdbTable=dot1dTpFdbTable,
    dot1dBaseType=dot1dBaseType,
    dot1dTpFdbAddress=dot1dTpFdbAddress,
    dot1dSr=dot1dSr,
    dot1dBaseNumPorts=dot1dBaseNumPorts,
    topologyChange=topologyChange,
    dot1dStpPortDesignatedPort=dot1dStpPortDesignatedPort,
    dot1dBasePortCircuit=dot1dBasePortCircuit,
    dot1dTpPortInFrames=dot1dTpPortInFrames,
    dot1dStpMaxAge=dot1dStpMaxAge,
    dot1dStpPortEntry=dot1dStpPortEntry,
    dot1dStaticEntry=dot1dStaticEntry,
    dot1dTpLearnedEntryDiscards=dot1dTpLearnedEntryDiscards,
    dot1dBasePortTable=dot1dBasePortTable,
    dot1dTpPort=dot1dTpPort,
    dot1dTpFdbPort=dot1dTpFdbPort,
    newRoot=newRoot,
    dot1dTp=dot1dTp,
    dot1dTpFdbStatus=dot1dTpFdbStatus,
    MacAddress=MacAddress,
    dot1dBaseBridgeAddress=dot1dBaseBridgeAddress,
    dot1dStaticStatus=dot1dStaticStatus,
    dot1dStpPortTable=dot1dStpPortTable,
    dot1dTpFdbEntry=dot1dTpFdbEntry,
    dot1dBasePort=dot1dBasePort,
    dot1dTpPortInDiscards=dot1dTpPortInDiscards,
    dot1dStpTimeSinceTopologyChange=dot1dStpTimeSinceTopologyChange,
    dot1dStpForwardDelay=dot1dStpForwardDelay,
    dot1dStp=dot1dStp,
    dot1dStpPortEnable=dot1dStpPortEnable,
    dot1dStpBridgeForwardDelay=dot1dStpBridgeForwardDelay,
    dot1dBasePortIfIndex=dot1dBasePortIfIndex,
    dot1dStpPortPriority=dot1dStpPortPriority,
    dot1dTpAgingTime=dot1dTpAgingTime,
    dot1dStpProtocolSpecification=dot1dStpProtocolSpecification,
    dot1dStpPortDesignatedRoot=dot1dStpPortDesignatedRoot,
    dot1dStaticAddress=dot1dStaticAddress,
    dot1dBasePortDelayExceededDiscards=dot1dBasePortDelayExceededDiscards,
    dot1dBasePortEntry=dot1dBasePortEntry,
    dot1dStpRootCost=dot1dStpRootCost,
    dot1dStatic=dot1dStatic,
    BridgeId=BridgeId,
    dot1dStpPriority=dot1dStpPriority,
    dot1dStpRootPort=dot1dStpRootPort,
    dot1dStpHelloTime=dot1dStpHelloTime,
    dot1dStpBridgeMaxAge=dot1dStpBridgeMaxAge,
    dot1dStpPortState=dot1dStpPortState,
    Timeout=Timeout,
    dot1dBasePortMtuExceededDiscards=dot1dBasePortMtuExceededDiscards,
    dot1dStpTopChanges=dot1dStpTopChanges,
    dot1dStpDesignatedRoot=dot1dStpDesignatedRoot,
    dot1dStpPortForwardTransitions=dot1dStpPortForwardTransitions,
    dot1dTpPortOutFrames=dot1dTpPortOutFrames,
    dot1dStpPort=dot1dStpPort,
    dot1dBase=dot1dBase,
    dot1dStaticAllowedToGoTo=dot1dStaticAllowedToGoTo,
    dot1dStpHoldTime=dot1dStpHoldTime,
    dot1dTpPortMaxInfo=dot1dTpPortMaxInfo,
    dot1dStpBridgeHelloTime=dot1dStpBridgeHelloTime,
    dot1dTpPortEntry=dot1dTpPortEntry,
    dot1dStpPortDesignatedBridge=dot1dStpPortDesignatedBridge,
    dot1dStpPortPathCost=dot1dStpPortPathCost,
    dot1dStpPortDesignatedCost=dot1dStpPortDesignatedCost,
    dot1dBridge=dot1dBridge,
    dot1dStaticReceivePort=dot1dStaticReceivePort,
    dot1dStaticTable=dot1dStaticTable,
)
