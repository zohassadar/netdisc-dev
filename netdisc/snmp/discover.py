import pprint
import time

from netdisc.base import constant, device
from netdisc.discover import dischelp
from netdisc.snmp import easyeng, engine, gatherer, mibhelp, pyeng, snmpbase


def snmp_discover(
    host: str,
    snmpeng: engine.SNMPEngine = pyeng.PySNMPEngine,
    flags: snmpbase.MIBXlate = snmpbase.MIBXlate.NONE,
    hostname: str = None,
    sysinfo: str = None,
    extra: dict = None,
    retries: int = 0,
    port: int = 0,
    community: str = None,
    snmpuser: str = None,
    authtype: str = None,
    auth: str = None,
    privtype: str = None,
    priv: str = None,
):
    if extra is None:
        extra = {}
    mib_helper = mibhelp.MIBHelper(flags=snmpbase.MIBXlate.PYSNMP)
    loaded_engine = snmpeng(
        mib_helper=mib_helper,
        host=host,
        community=community,
        snmpuser=snmpuser,
        authtype=authtype,
        auth=auth,
        privtype=privtype,
        priv=priv,
    )
    gather = gatherer.SNMPGeneric(loaded_engine)
    error, result = dischelp.gather_and_test(gather, disabled=True)
    return result
