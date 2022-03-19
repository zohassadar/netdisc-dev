from netdisc import config, logger
from netdisc.base import threaded, topology
from netdisc.discover import looper, worker
from netdisc.output import printed
import logging

args, auth_methods, hosts = config.get_netdisc_args()

logger.set_logger(
    verbose=args.verbose, log_file=args.log_file, log_file_depth=args.log_file_depth
)


outputs = [printed.PrintedOutput]
hopper = [looper.PendingDevice(ip) for ip in hosts.hostlist]
queue = threaded.ThreadedQueue(worker.do_task, args.workers, args.worker_sleep)


def discover() -> topology.abstract.TopologyBase:
    topo = topology.MemoryTopology()
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
