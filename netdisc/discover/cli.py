import argparse
import ipaddress
import logging
import re
import socket
import sys
import functools
from netdisc.tools import helpers


@helpers.debugger(logging.CRITICAL)
def exit(*args, **kwargs):
    print("some asshole called exit")


_exit = sys.exit
sys.exit = exit

HELP_MESSAGE = """This is where the help message goes"""


def get_cli_args():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("--ip", nargs="+", type=str, help="Starting IP Address")
    arg_parser.add_argument("--hostlist", type=str, help="Config File")
    arg_parser.add_argument("--config_file", type=str, help="Config File")

    return arg_parser.parse_args()
