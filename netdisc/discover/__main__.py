import logging
import argparse
import pathlib
from netdisc.base import threaded, topology
from netdisc.discover import authen, looper, worker
from netdisc.snmp import snmpargs
from netdisc.tools import log_setup, pandor, interactive

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def get_filter_from_file(filename):
    try:
        with open(filename) as file:
            contents = file.read()
    except FileNotFoundError as exc:
        raise argparse.ArgumentTypeError(str(exc))
    try:
        return pandor.AttrFilterForkFactory(contents)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(str(exc))


args = argparse.ArgumentParser(add_help=False)
args.add_argument(
    "-f",
    "--filter-file",
    type=get_filter_from_file,
    default=pandor.AllowAll(),
    help="File containing netdisc filter",
)

args.add_argument(
    "-i",
    "--interactive",
    action="store_const",
    const=interactive.InteractiveNeighborFilter(),
    help="Interactively filter neighbors",
)

for_help_only = argparse.ArgumentParser(
    parents=[
        log_setup.log_parser,
        snmpargs.parser,
        args,
    ],
)
for_help_only.parse_args()


if __name__ == "__main__":
    print("running!")
    (parsed_snmp, remaining) = snmpargs.parser.parse_known_args()
    (parsed_discover, _) = args.parse_known_args(remaining)
    args = vars(parsed_snmp).copy()
    log_setup.set_logger_from_args()
    hostlist = [args.pop("host")]

    auths = authen.AuthMethodList()
    auths.load_authentication_methods(dict(from_cli=args))
    with (
        topology.MemoryTopology() as topo,
        threaded.WorkerPoolThread(worker.discovery_dispatch, 1, 2) as pool,
    ):

        # pool = threaded.WorkerPoolThread(worker.discovery_dispatch, 1, 2).__enter__()
        # topo = topology.MemoryTopology().__enter__()
        runner = looper.DiscoveryRunner(
            topology=topo,
            hostlist=hostlist,
            auth_methods=auths,
            discovery_q=pool.input,
            discovered_q=pool.output,
            filter=parsed_discover.filter_file,
            interactive=parsed_discover.interactive,
        )
        runner.loop()
        import pprint

        pprint.pp(runner._pending)
