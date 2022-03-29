import argparse
import pprint

from netdisc.tools import log_setup


pprinter = pprint.PrettyPrinter()
pp = pprinter.pprint

parser = argparse.ArgumentParser()
parser.add_argument(
    "-c",
    "--community",
    type=str,
    help="SNMPv2 community string",
)
parser.add_argument(
    "-u",
    "--snmpuser",
    type=str,
    help="SNMPv3 Security name",
)
parser.add_argument(
    "-a",
    "--authtype",
    type=str,
    help="Authentication protocol (MD5|SHA)",
)
parser.add_argument(
    "-A",
    "--auth",
    type=str,
    help="Authentication passphrase",
)
parser.add_argument(
    "-x",
    "--priv",
    type=str,
    help="Privacy protocol (DES|AES)",
)
parser.add_argument(
    "-X",
    "--privtype",
    type=str,
    help="Privacy passphrase",
)
parser.add_argument(
    "host",
    type=str,
    help="Hostname of endpoint",
)
parser.add_argument(
    "-v",
    "--verbose",
    action="count",
    default=0,
    help="Logging verbosity.  -v through -vvvvv",
)
args = parser.parse_args()
if __name__ == "__main__":
    args = parser.parse_args()
    log_setup.set_logger(args.verbose)
    from netdisc.snmp import gatherer, pyeng, mibhelp, easyeng, snmpbase
    from netdisc.discover import dischelp

    kwargs = vars(args)
    kwargs.pop("verbose")

    pyhelp = mibhelp.MIBHelper(flags=snmpbase.MIBXlate.PYSNMP)
    py_engine = pyeng.PySNMPEngine(mib_helper=pyhelp, **kwargs)
    py_gather = gatherer.SNMPGeneric(py_engine)
    error, result = dischelp.gather_and_test(py_gather, disabled=True)
    print("pysnmp output:")
    pp(result)
    print("")
    easyhelp = mibhelp.MIBHelper(flags=snmpbase.MIBXlate.EASYSNMP)
    easy_engine = easyeng.EasySNMPEngine(mib_helper=easyhelp, **kwargs)
    easy_gather = gatherer.SNMPGeneric(easy_engine)
    error, result = dischelp.gather_and_test(easy_gather, disabled=True)
    print("easysnmp output:")
    pp(result)
