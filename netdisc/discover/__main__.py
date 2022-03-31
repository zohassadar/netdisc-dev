from netdisc.tools import log_setup

log_setup.set_logger(verbose=1, debug=True)

from netdisc.base import threaded, topology
from netdisc.discover import looper, worker, authen
from netdisc.output import printed
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


hostlist = ["192.168.42.254"]

auths = authen.AuthMethodList()
creds = {
    "mycreds": {
        "community": "wordup",
    },
    "other creds": {
        "username": "cisco",
        "password": "cisco",
    },
}

auths.load_authentication_methods(creds)

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
