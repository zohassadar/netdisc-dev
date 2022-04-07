import argparse

parser = argparse.ArgumentParser(prog="netdisc.snmp", add_help=False)
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
    "--privtype",
    type=str,
    help="Privacy protocol (DES|AES)",
)
parser.add_argument(
    "-X",
    "--priv",
    type=str,
    help="Privacy passphrase",
)
parser.add_argument(
    "host",
    type=str,
    help="Hostname of endpoint",
)
