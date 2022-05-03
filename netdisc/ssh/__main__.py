import argparse
import pprint
import socket


import textfsm
from netdisc.ssh import custparse
from ntc_templates import parse
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
ssh_test_args = argparse.ArgumentParser(add_help=False)
ssh_test_args.add_argument(
    "platform",
    type=str,
    help="platform in netmiko format",
)
ssh_test_args.add_argument(
    "command",
    type=str,
    help="command",
)
ssh_test_args.add_argument(
    "data",
    type=str,
    help="text file containing command output data",
)
ssh_test_args.add_argument(
    "-c",
    "--custom",
    action="store_true",
    help="Use custom templates",
)


def get_host_by_ip(ip):
    try:
        result = socket.gethostbyaddr(ip)
        logging.debug("Resolved %s to: %s", ip, result)
        return result[0]
    except socket.herror as exc:
        logging.debug("Unable to resolve %s: %s.  Returning IP.", ip, exc)
        return ip


def nexus_mpls_route_report():
    routes = parse.parse_output("cisco_nxos", "show ip route", SHIPROUTE)
    mpls_destinations = [r for r in routes if r["nexthop_vrf"]]
    results = []
    for mpls_dest in mpls_destinations:
        result = {}
        result["network"] = mpls_dest["network"]
        result["mask"] = mpls_dest["mask"]
        result["nexthop_ip"] = mpls_dest["nexthop_ip"]
        result["nexthop_fqdn"] = get_host_by_ip(mpls_dest["nexthop_ip"])
        results.append(result)
    return results


def arista_vxlan_route_report():
    routes = parse.parse_output("arista_eos", "show ip route", SHIPROUTE)
    mpls_destinations = [r for r in routes if r["nexthop_vrf"]]
    results = []
    for mpls_dest in mpls_destinations:
        result = {}
        result["network"] = mpls_dest["network"]
        result["mask"] = mpls_dest["mask"]
        result["nexthop_ip"] = mpls_dest["nexthop_ip"]
        result["nexthop_fqdn"] = get_host_by_ip(mpls_dest["nexthop_ip"])
        results.append(result)
    return results


def test_and_pprint(
    platform: str,
    command: str,
    data: str,
    custom: bool,
):
    with open(data) as f:
        loaded_data = f.read()
    pprint.pprint(
        custparse.parse_output(
            platform,
            command,
            loaded_data,
            use_custom=custom,
        )
    )


if __name__ == "__main__":
    args = ssh_test_args.parse_args()
    test_and_pprint(
        platform=args.platform,
        command=args.command,
        data=args.data,
        custom=args.custom,
    )
