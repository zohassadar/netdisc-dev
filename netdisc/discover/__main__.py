import logging

from netdisc.base import threaded, topology
from netdisc.discover import authen, looper, worker
from netdisc.snmp import snmpargs
from netdisc.tools import log_setup

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


if __name__ == "__main__":
    args = vars(snmpargs.parser.parse_args()).copy()
    log_setup.set_logger(args.pop("verbose"), debug=True)
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
        )
        runner.loop()
