import pprint
import time

from netdisc.base import constant, device_base
from netdisc.discover import dischelp
from netdisc.snmp import easyeng, engine, gatherer, mibhelp, pyeng, snmpbase

import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def snmp_discover(
    host: str,
    snmpeng: engine.SNMPEngine = pyeng.PySNMPEngine,
    flags: snmpbase.MIBXlate = snmpbase.MIBXlate.NONE,
    extra: dict = None,
    hostname: str = None,
    sysinfo: str = None,
    retries: int = 0,
    port: int = 0,
    community: str = None,
    snmpuser: str = None,
    authtype: str = None,
    auth: str = None,
    privtype: str = None,
    priv: str = None,
):
    logger.error("called with: %s %s", host, community)
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

    try:
        gather = gatherer.SNMPGeneric(loaded_engine)
        error, result = dischelp.gather_and_test(gather, disabled=True)
    except RuntimeError as exc:
        result = device_base.Device(
            device_ip=host, failed=True, failure_reason=str(exc)
        )
    return result
