#
# PySNMP MIB module CISCO-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///mibs.thola.io/asn1/CISCO-SMI
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
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols(
    "SNMPv2-CONF", "ModuleCompliance", "NotificationGroup"
)
(
    MibIdentifier,
    enterprises,
    IpAddress,
    Counter64,
    Gauge32,
    MibScalar,
    MibTable,
    MibTableRow,
    MibTableColumn,
    TimeTicks,
    ModuleIdentity,
    NotificationType,
    Integer32,
    Bits,
    ObjectIdentity,
    Counter32,
    iso,
    Unsigned32,
) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "MibIdentifier",
    "enterprises",
    "IpAddress",
    "Counter64",
    "Gauge32",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "ModuleIdentity",
    "NotificationType",
    "Integer32",
    "Bits",
    "ObjectIdentity",
    "Counter32",
    "iso",
    "Unsigned32",
)
DisplayString, TextualConvention = mibBuilder.importSymbols(
    "SNMPv2-TC", "DisplayString", "TextualConvention"
)
cisco = ModuleIdentity((1, 3, 6, 1, 4, 1, 9))
cisco.setRevisions(
    (
        "2016-01-15 00:00",
        "2012-08-29 00:00",
        "2009-02-03 00:00",
        "2002-03-21 00:00",
        "2001-05-22 00:00",
        "2000-11-01 22:46",
        "2000-01-11 00:00",
        "1997-04-09 00:00",
        "1995-05-16 00:00",
        "1994-04-26 20:00",
    )
)
if mibBuilder.loadTexts:
    cisco.setLastUpdated("201601150000Z")
if mibBuilder.loadTexts:
    cisco.setOrganization("Cisco Systems, Inc.")
ciscoProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 1))
if mibBuilder.loadTexts:
    ciscoProducts.setStatus("current")
local = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 2))
if mibBuilder.loadTexts:
    local.setStatus("current")
temporary = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 3))
if mibBuilder.loadTexts:
    temporary.setStatus("current")
pakmon = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 4))
if mibBuilder.loadTexts:
    pakmon.setStatus("current")
workgroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 5))
if mibBuilder.loadTexts:
    workgroup.setStatus("current")
otherEnterprises = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6))
if mibBuilder.loadTexts:
    otherEnterprises.setStatus("current")
ciscoSB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1))
if mibBuilder.loadTexts:
    ciscoSB.setStatus("current")
ciscoSMB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 6, 2))
if mibBuilder.loadTexts:
    ciscoSMB.setStatus("current")
ciscoAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 7))
if mibBuilder.loadTexts:
    ciscoAgentCapability.setStatus("current")
ciscoConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 8))
if mibBuilder.loadTexts:
    ciscoConfig.setStatus("current")
ciscoMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9))
if mibBuilder.loadTexts:
    ciscoMgmt.setStatus("current")
ciscoExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10))
if mibBuilder.loadTexts:
    ciscoExperiment.setStatus("current")
ciscoAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11))
if mibBuilder.loadTexts:
    ciscoAdmin.setStatus("current")
ciscoModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 12))
if mibBuilder.loadTexts:
    ciscoModules.setStatus("current")
lightstream = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 13))
if mibBuilder.loadTexts:
    lightstream.setStatus("current")
ciscoworks = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 14))
if mibBuilder.loadTexts:
    ciscoworks.setStatus("current")
newport = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 15))
if mibBuilder.loadTexts:
    newport.setStatus("current")
ciscoPartnerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 16))
if mibBuilder.loadTexts:
    ciscoPartnerProducts.setStatus("current")
ciscoPolicy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17))
if mibBuilder.loadTexts:
    ciscoPolicy.setStatus("current")
ciscoPIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 17, 2))
if mibBuilder.loadTexts:
    ciscoPIB.setStatus("current")
ciscoPolicyAuto = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18))
if mibBuilder.loadTexts:
    ciscoPolicyAuto.setStatus("current")
ciscoPibToMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 18, 2))
if mibBuilder.loadTexts:
    ciscoPibToMib.setStatus("current")
ciscoDomains = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19))
if mibBuilder.loadTexts:
    ciscoDomains.setStatus("current")
ciscoCIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20))
if mibBuilder.loadTexts:
    ciscoCIB.setStatus("current")
ciscoCibMmiGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20, 1))
if mibBuilder.loadTexts:
    ciscoCibMmiGroup.setStatus("current")
ciscoCibProvGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 20, 2))
if mibBuilder.loadTexts:
    ciscoCibProvGroup.setStatus("current")
ciscoPKI = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 21))
if mibBuilder.loadTexts:
    ciscoPKI.setStatus("current")
ciscoLDAP = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 22))
if mibBuilder.loadTexts:
    ciscoLDAP.setStatus("current")
ciscoProxy = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 1))
if mibBuilder.loadTexts:
    ciscoProxy.setStatus("current")
ciscoPartyProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 1))
ciscoContextProxy = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 11, 1, 2))
ciscoRptrGroupObjectID = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2))
if mibBuilder.loadTexts:
    ciscoRptrGroupObjectID.setStatus("current")
ciscoUnknownRptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 1))
if mibBuilder.loadTexts:
    ciscoUnknownRptrGroup.setStatus("current")
cisco2505RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 2))
if mibBuilder.loadTexts:
    cisco2505RptrGroup.setStatus("current")
cisco2507RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 3))
if mibBuilder.loadTexts:
    cisco2507RptrGroup.setStatus("current")
cisco2516RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 4))
if mibBuilder.loadTexts:
    cisco2516RptrGroup.setStatus("current")
ciscoWsx5020RptrGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 2, 5))
if mibBuilder.loadTexts:
    ciscoWsx5020RptrGroup.setStatus("current")
ciscoChipSets = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3))
if mibBuilder.loadTexts:
    ciscoChipSets.setStatus("current")
ciscoChipSetSaint1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 1))
if mibBuilder.loadTexts:
    ciscoChipSetSaint1.setStatus("current")
ciscoChipSetSaint2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 2))
if mibBuilder.loadTexts:
    ciscoChipSetSaint2.setStatus("current")
ciscoChipSetSaint3 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 3))
if mibBuilder.loadTexts:
    ciscoChipSetSaint3.setStatus("current")
ciscoChipSetSaint4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 11, 3, 4))
if mibBuilder.loadTexts:
    ciscoChipSetSaint4.setStatus("current")
ciscoTDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 19, 99999))
ciscoTDomainUdpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 1))
if mibBuilder.loadTexts:
    ciscoTDomainUdpIpv4.setStatus("current")
ciscoTDomainUdpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 2))
if mibBuilder.loadTexts:
    ciscoTDomainUdpIpv6.setStatus("current")
ciscoTDomainTcpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 3))
if mibBuilder.loadTexts:
    ciscoTDomainTcpIpv4.setStatus("current")
ciscoTDomainTcpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 4))
if mibBuilder.loadTexts:
    ciscoTDomainTcpIpv6.setStatus("current")
ciscoTDomainLocal = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 5))
if mibBuilder.loadTexts:
    ciscoTDomainLocal.setStatus("current")
ciscoTDomainClns = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 6))
if mibBuilder.loadTexts:
    ciscoTDomainClns.setStatus("current")
ciscoTDomainCons = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 7))
if mibBuilder.loadTexts:
    ciscoTDomainCons.setStatus("current")
ciscoTDomainDdp = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 8))
if mibBuilder.loadTexts:
    ciscoTDomainDdp.setStatus("current")
ciscoTDomainIpx = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 9))
if mibBuilder.loadTexts:
    ciscoTDomainIpx.setStatus("current")
ciscoTDomainSctpIpv4 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 10))
if mibBuilder.loadTexts:
    ciscoTDomainSctpIpv4.setStatus("current")
ciscoTDomainSctpIpv6 = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 99999, 11))
if mibBuilder.loadTexts:
    ciscoTDomainSctpIpv6.setStatus("current")
mibBuilder.exportSymbols(
    "CISCO-SMI",
    ciscoSMB=ciscoSMB,
    PYSNMP_MODULE_ID=cisco,
    ciscoMgmt=ciscoMgmt,
    ciscoCibProvGroup=ciscoCibProvGroup,
    ciscoChipSetSaint3=ciscoChipSetSaint3,
    ciscoChipSets=ciscoChipSets,
    ciscoworks=ciscoworks,
    ciscoAgentCapability=ciscoAgentCapability,
    ciscoSB=ciscoSB,
    ciscoPKI=ciscoPKI,
    ciscoTDomainTcpIpv4=ciscoTDomainTcpIpv4,
    cisco=cisco,
    ciscoConfig=ciscoConfig,
    ciscoWsx5020RptrGroup=ciscoWsx5020RptrGroup,
    ciscoChipSetSaint4=ciscoChipSetSaint4,
    otherEnterprises=otherEnterprises,
    ciscoPartnerProducts=ciscoPartnerProducts,
    ciscoLDAP=ciscoLDAP,
    ciscoTDomains=ciscoTDomains,
    workgroup=workgroup,
    ciscoTDomainDdp=ciscoTDomainDdp,
    ciscoTDomainTcpIpv6=ciscoTDomainTcpIpv6,
    ciscoExperiment=ciscoExperiment,
    ciscoPolicy=ciscoPolicy,
    ciscoPartyProxy=ciscoPartyProxy,
    local=local,
    newport=newport,
    ciscoCIB=ciscoCIB,
    ciscoTDomainClns=ciscoTDomainClns,
    lightstream=lightstream,
    ciscoChipSetSaint1=ciscoChipSetSaint1,
    cisco2516RptrGroup=cisco2516RptrGroup,
    ciscoModules=ciscoModules,
    ciscoCibMmiGroup=ciscoCibMmiGroup,
    ciscoUnknownRptrGroup=ciscoUnknownRptrGroup,
    ciscoPolicyAuto=ciscoPolicyAuto,
    pakmon=pakmon,
    ciscoAdmin=ciscoAdmin,
    cisco2507RptrGroup=cisco2507RptrGroup,
    cisco2505RptrGroup=cisco2505RptrGroup,
    ciscoChipSetSaint2=ciscoChipSetSaint2,
    ciscoRptrGroupObjectID=ciscoRptrGroupObjectID,
    ciscoProducts=ciscoProducts,
    ciscoTDomainUdpIpv4=ciscoTDomainUdpIpv4,
    ciscoTDomainSctpIpv6=ciscoTDomainSctpIpv6,
    ciscoTDomainSctpIpv4=ciscoTDomainSctpIpv4,
    ciscoProxy=ciscoProxy,
    ciscoTDomainUdpIpv6=ciscoTDomainUdpIpv6,
    ciscoTDomainCons=ciscoTDomainCons,
    temporary=temporary,
    ciscoDomains=ciscoDomains,
    ciscoContextProxy=ciscoContextProxy,
    ciscoTDomainIpx=ciscoTDomainIpx,
    ciscoPibToMib=ciscoPibToMib,
    ciscoPIB=ciscoPIB,
    ciscoTDomainLocal=ciscoTDomainLocal,
)
