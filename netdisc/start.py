from netdisc.tools import log_setup
from netdisc.discover import config

args, auth_methods, filter_, hosts = config.get_netdisc_args()


log_setup.set_logger(verbose=5)


from netdisc.base import threaded, topology
from netdisc.discover import looper, worker
from netdisc.output import printed
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


outputs = [printed.PrintedOutput]
hopper = [looper.PendingDevice(ip) for ip in hosts.hostlist]
queue = threaded.ThreadedQueue(worker.do_task, args.workers, args.worker_sleep)
topo = topology.MemoryTopology()


def main() -> topology.abstract.TopologyBase:
    with looper.DiscoveryRunner(
        topo,
        hopper,
        queue,
        auth_methods,
        outputs,
        args.server_mode,
        args.dead_timer,
        args.loop_sleep,
    ) as discoverer:
        discoverer.run()
    return topo
