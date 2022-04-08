import pprint
import time

from netdisc.base import device_base
from netdisc.snmp import gatherer, pyeng, snmpbase

import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

PYSNMP = "pysnmp"
EASYSNMP = "easysnmp"

EXTRA_KEY = "snmp"
ENGINE_KEY = "engine"
FLAGS_KEY = "flags"


def get_engine(name):
    if name == PYSNMP:

        return pyeng.PySNMPEngine
    elif name == EASYSNMP:
        try:
            from netdisc.snmp import easyeng

            return easyeng.EasySNMPEngine
        except ImportError:
            raise RuntimeError(f"Unable to import {EASYSNMP}")
    else:
        raise RuntimeError(f"Invalid engine: {name}")


def snmp_discover(
    host: str,
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
    logger.info("SNMP Discover called for: %s %s", host, community)
    if extra is None:
        extra = {}
    snmp_extra = extra.get(EXTRA_KEY, {})

    engine = get_engine(snmp_extra.get(ENGINE_KEY, PYSNMP))
    loaded_engine = engine(
        host=host,
        community=community,
        snmpuser=snmpuser,
        authtype=authtype,
        auth=auth,
        privtype=privtype,
        priv=priv,
        flags=snmp_extra.get(FLAGS_KEY),
    )

    try:
        gather = gatherer.SNMPGeneric(loaded_engine)
        device = gather.get_device_object()
    except RuntimeError as exc:
        device = device_base.Device(
            device_ip=host, failed=True, failure_reason=str(exc)
        )
    return device
