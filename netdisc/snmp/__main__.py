import argparse
import pprint

from netdisc.discover import dischelp
from netdisc.snmp import easyeng, gatherer, mibhelp, pyeng, snmpargs, snmpbase
from netdisc.snmp.engine import SNMPEngine
from netdisc.tools import log_setup

pprinter = pprint.PrettyPrinter()
pp = pprinter.pprint


def print_snmp_generic(engine):
    py_gather = gatherer.SNMPGeneric(engine)
    result = py_gather.get_device_object().dump()
    print(f"{type(engine).__name__} output:")
    pp(result)
    print("")


def print_object(engine: SNMPEngine, snmpobj):
    result = engine.object_get(snmpobj)
    pp(result)


if __name__ == "__main__":
    help_only = argparse.ArgumentParser(
        parents=[
            log_setup.log_parser,
            snmpargs.debug_parser,
            snmpargs.parser,
        ],
    )
    help_only.parse_args()
    snmp_args, _ = snmpargs.parser.parse_known_args()
    debug_args, _ = snmpargs.debug_parser.parse_known_args()
    log_setup.set_logger_from_args()

    kwargs = vars(snmp_args).copy()

    engine = debug_args.snmp_engine
    if engine is pyeng.PySNMPEngine:
        helper = mibhelp.MIBHelper(flags=snmpbase.MIBXlate.PYSNMP)
    elif engine is easyeng.EasySNMPEngine:
        helper = mibhelp.MIBHelper(flags=snmpbase.MIBXlate.EASYSNMP)
    loaded_engine = engine(mib_helper=helper, **kwargs)

    if debug_args.object:
        print_object(loaded_engine, debug_args.object)
    else:
        print_snmp_generic(loaded_engine)
