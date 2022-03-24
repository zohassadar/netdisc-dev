import logging

import yaml
from netdisc.discover import defaults
from netdisc.discover import authen, cli
from netdisc.tools import hostlist, pandor

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def get_config_args(user_specified, default):
    results = {}
    config_file = user_specified or default
    try:
        with open(config_file) as f:
            config_args = yaml.safe_load(f)
            results.update(config_args)
    except FileNotFoundError:
        pass
    return results


def get_netdisc_args() -> tuple:
    # Load three config sources independently
    args = defaults.NetdiscConfig()
    cli_args = cli.get_cli_args()
    config_args = get_config_args(cli_args.config_file, args.config_file)

    # Update in order of precedence
    vars(args).update(config_args)
    vars(args).update(vars(cli_args))

    # Peel off filter
    filter_string = config_args.pop("filter")
    discovery_filter = pandor.AttrFilterForkFactory(filter_string)

    # Peel out auth methods
    authentication_methods = {
        k: vars(args).pop(k) for k, v in vars(args) if isinstance(v, dict)
    }
    # auth_object = authen.AuthMethodList(

    hosts = hostlist.HostListAccumulator()
    hosts.ingest(vars(args).pop("hostlist"))
    hosts.ingest(vars(args).pop("ip"))


# get_netdisc_args()
