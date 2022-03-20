import pathlib
from netdisc.snmp import asn1mibs


NET_SNMP_MIBS_ENV = "MIBDIRS"

NET_SNMP_DEFAULTS = """/usr/share/snmp/mibs
/usr/share/snmp/mibs/iana
/usr/share/snmp/mibs/ietf
/usr/share/mibs/site
/usr/share/snmp/mibs
/usr/share/mibs/iana
/usr/share/mibs/ietf
/usr/share/mibs/netsnmp"""


MIB_HOME = pathlib.Path.joinpath(
    pathlib.Path.home(),
    pathlib.Path(".snmp/mibs"),
)

MIB_SOURCE = pathlib.Path(asn1mibs.__file__).parent

MIB_SEARCH_PATH = []

MIB_SEARCH_PATH.append(MIB_HOME)
MIB_SEARCH_PATH.extend([pathlib.Path(path) for path in NET_SNMP_DEFAULTS.splitlines()])
MIB_SEARCH_PATH.append(MIB_SOURCE)

MIB_PATHS = ":".join(str(path) for path in MIB_SEARCH_PATH)


def main():
    print(f"export {NET_SNMP_MIBS_ENV}={MIB_PATHS}")
