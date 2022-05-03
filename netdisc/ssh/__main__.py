import argparse
import pprint
from netdisc.ssh import custparse
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
