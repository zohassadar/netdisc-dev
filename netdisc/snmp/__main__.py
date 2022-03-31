import pprint

from netdisc.tools import log_setup
from netdisc.snmp import snmpargs

pprinter = pprint.PrettyPrinter()
pp = pprinter.pprint


if __name__ == "__main__":
    args = snmpargs.parser.parse_args()
    log_setup.set_logger(2, debug=True)
    from netdisc.snmp import gatherer, pyeng, mibhelp, easyeng, snmpbase
    from netdisc.discover import dischelp

    kwargs = vars(args)
    kwargs.pop("verbose")

    pyhelp = mibhelp.MIBHelper(flags=snmpbase.MIBXlate.PYSNMP)
    py_engine = pyeng.PySNMPEngine(mib_helper=pyhelp, **kwargs)
    py_gather = gatherer.SNMPGeneric(py_engine)
    error, result = dischelp.gather_and_test(py_gather)
    print("pysnmp output:")
    pp(result)
    print("")
    easyhelp = mibhelp.MIBHelper(flags=snmpbase.MIBXlate.EASYSNMP)
    easy_engine = easyeng.EasySNMPEngine(mib_helper=easyhelp, **kwargs)
    easy_gather = gatherer.SNMPGeneric(easy_engine)
    error, result = dischelp.gather_and_test(easy_gather)
    print("easysnmp output:")
    pp(result)
