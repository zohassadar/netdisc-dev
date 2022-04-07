import argparse
from netdisc.snmp import pyeng, snmpbase

PYSNMP = "pysnmp"
EASYSNMP = "easysnmp"


def get_snmpbase_objects():
    results = []
    for attr in dir(snmpbase):
        obj = getattr(snmpbase, attr)
        if isinstance(obj, type) and issubclass(obj, snmpbase.VarBindBase):
            results.append(attr)
    return results


NEWLINE = "\n"


def get_snmpbase_object(name):
    result = getattr(snmpbase, name, None)
    if not result:
        print(f"Valid object names: \n{NEWLINE.join(get_snmpbase_objects())}")
        raise argparse.ArgumentTypeError(f"Invalid object: {name}")
    return result


def get_engine(name):
    if name == PYSNMP:

        return pyeng.PySNMPEngine
    elif name == EASYSNMP:
        try:
            from netdisc.snmp import easyeng

            return easyeng.EasySNMPEngine
        except ImportError:
            raise argparse.ArgumentTypeError(f"Unable to import {EASYSNMP}")
    else:
        raise argparse.ArgumentTypeError(f"Invalid choice: {name}")


parser = argparse.ArgumentParser(prog="netdisc.snmp", add_help=False)

snmp_arg_group = parser.add_argument_group("SNMP Arguments")

snmp_arg_group.add_argument(
    "-c",
    "--community",
    type=str,
    help="SNMPv2 community string",
)
snmp_arg_group.add_argument(
    "-u",
    "--snmpuser",
    type=str,
    help="SNMPv3 Security name",
)
snmp_arg_group.add_argument(
    "-a",
    "--authtype",
    type=str,
    help="Authentication protocol (MD5|SHA)",
)
snmp_arg_group.add_argument(
    "-A",
    "--auth",
    type=str,
    help="Authentication passphrase",
)
snmp_arg_group.add_argument(
    "-x",
    "--privtype",
    type=str,
    help="Privacy protocol (DES|AES)",
)
snmp_arg_group.add_argument(
    "-X",
    "--priv",
    type=str,
    help="Privacy passphrase",
)
snmp_arg_group.add_argument(
    "host",
    type=str,
    help="Hostname of endpoint",
)


debug_parser = argparse.ArgumentParser(add_help=False)

debug_parser.add_argument(
    "--snmp-engine",
    type=get_engine,
    default=pyeng.PySNMPEngine,
    help=f"SNMP Engine: {PYSNMP} (default) or {EASYSNMP}",
)

debug_parser.add_argument(
    "--object",
    type=get_snmpbase_object,
    help=f"SNMP Object Name: ",
)
