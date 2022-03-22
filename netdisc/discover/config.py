import ipaddress
import logging
import pathlib
import re
import contextlib

import yaml


from netdisc.base import constant, defaults
from netdisc.discover import authen, cli
from netdisc.tools import helpers, hostlist

CONFIG_KEY_INCLUDE_HOSTNAME = "include_hostname"
CONFIG_KEY_INCLUDE_NETWORK = "include_network"
CONFIG_KEY_INCLUDE_SYSINFO = "include_sysinfo"

CONFIG_KEY_EXCLUDE_HOSTNAME = "exclude_hostname"
CONFIG_KEY_EXCLUDE_NETWORK = "exclude_network"
CONFIG_KEY_EXCLUDE_SYSINFO = "exclude_sysinfo"

CONFIG_KEY_PORT = "port"
CONFIG_KEY_RETRIES = "retries"


def invalid_credential_options(
    name: str,
    invalid: dict,
):
    for key in invalid:
        raise ValueError(f"Invalid credential option for {name}: {key}")


def get_snmpv2c_auth(
    args: defaults.NetdiscConfig,
    name: str = None,
    index: int = None,
    proto: constant.Proto = None,
    community: str = None,
    port: int = None,
    retries: int = None,
    **kwargs,
):
    port = kwargs.pop(CONFIG_KEY_PORT, args.snmp_port)
    retries = kwargs.pop(CONFIG_KEY_RETRIES, args.retries)
    if kwargs:
        invalid_credential_options(name, kwargs)
    return authen.AuthMethod(
        index=index,
        name=name,
        proto=proto,
        port=port,
        retries=retries,
        community=community,
    )


def get_snmpv3_auth(
    args: defaults.NetdiscConfig = None,
    name: str = None,
    index: int = None,
    proto: constant.Proto = None,
    snmpuser: str = None,
    authtype: str = None,
    auth: str = None,
    privtype: str = None,
    priv: str = None,
    **kwargs,
):
    port = kwargs.pop(CONFIG_KEY_PORT, args.snmp_port)
    retries = kwargs.pop(CONFIG_KEY_RETRIES, args.retries)

    if kwargs:
        invalid_credential_options(name, kwargs)

    return authen.AuthMethod(
        index=index,
        name=name,
        proto=proto,
        port=port,
        retries=retries,
        snmpuser=snmpuser,
        authtype=authtype,
        auth=auth,
        privtype=privtype,
        priv=priv,
    )


def get_username_auth(
    args: defaults.NetdiscConfig = None,
    name: str = None,
    index: int = None,
    username: str = None,
    password: str = None,
    **kwargs,
):
    popped_port = kwargs.pop(CONFIG_KEY_PORT, None)
    retries = kwargs.pop(CONFIG_KEY_RETRIES, args.retries)
    secret: str = kwargs.pop("secret", None)
    if kwargs:
        invalid_credential_options(name, kwargs)

    def partial_username_auth(proto: constant.Proto, port: int):
        return authen.AuthMethod(
            name=name,
            index=index,
            username=username,
            password=password,
            secret=secret,
            retries=retries,
            proto=proto,
            port=port,
        )

    username_auths = []
    if args.ssh:
        username_auths.append(
            partial_username_auth(
                proto=constant.Proto.SSH,
                port=popped_port or args.ssh_port,
            )
        )
        index += 1
    if args.api:
        username_auths.append(
            partial_username_auth(
                proto=constant.Proto.API,
                port=popped_port or args.api_port,
            )
        )
        index += 1
    if args.telnet:
        username_auths.append(
            partial_username_auth(
                proto=constant.Proto.TELNET,
                port=popped_port or args.telnet_port,
            )
        )
        index += 1
    return username_auths


def validate_credential_list(args, credentials: list[tuple[str, dict]]):
    validated_credentials = authen.AuthMethodList(args.keep_score)
    index = 0
    for name, credential in credentials:
        match credential:
            case {"snmpuser": _}:
                validated_credentials.append(
                    get_snmpv3_auth(
                        args=args,
                        name=name,
                        index=index,
                        proto=constant.Proto.SNMPv3,
                        **credential,
                    )
                )
                index += 1
            case {"community": _}:
                validated_credentials.append(
                    get_snmpv2c_auth(
                        args=args,
                        name=name,
                        index=index,
                        proto=constant.Proto.SNMPv2c,
                        **credential,
                    )
                )
                index += 1
            case {"username": _}:

                validated = get_username_auth(
                    args=args,
                    name=name,
                    index=index,
                    **credential,
                )
                validated_credentials.extend(validated)
                index += len(validated)
    return validated_credentials


# def validate_discovery_filter_entry(filter_entry: dict) -> list[filter_.Filter]:
#     discovery_filters = []
#     for filter_type, value in filter_entry.items():
#         try:
#             match filter_type, value:
#                 case ("include_hostname", regex):
#                     discovery_filters.append(
#                         filter_.NeighborHostname(regex=regex),
#                     )
#                 case ("exclude_hostname", regex):
#                     discovery_filters.append(
#                         filter_.NeighborHostnameExclude(regex=regex),
#                     )
#                 case ("include_network", network):
#                     discovery_filters.append(
#                         filter_.NeighborNetwork(network=network),
#                     )
#                 case ("exclude_network", network):
#                     discovery_filters.append(
#                         filter_.NeighborNetworkExclude(network=network),
#                     )
#                 case ("include_sysinfo", regex):
#                     discovery_filters.append(
#                         filter_.NeighborSysinfo(regex=regex),
#                     )
#                 case ("exclude_sysinfo", regex):
#                     discovery_filters.append(
#                         filter_.NeighborSysinfoExclude(regex=regex),
#                     )
#                 case (unknown, value):
#                     raise ValueError(f"Filter of type '{unknown}' is unsupported")
#         except (TypeError, re.error, ipaddress.AddressValueError):
#             raise ValueError("Invalid value for {filter_type}")
#     return discovery_filters


# def validate_discovery_filter_input(
#     discovery_filter: list | dict,
# ) -> filter_.Filter | None:
#     discovery_filters = []
#     match discovery_filter:
#         case dict():
#             discovery_filters.extend(validate_discovery_filter_entry(discovery_filter))
#         case list():
#             for filter_entry in discovery_filter:
#                 discovery_filters.extend(validate_discovery_filter_input(filter_entry))
#         case unknown:
#             raise ValueError(
#                 f"Input of type '{type(unknown)}' is invalid for discovery_filter input"
#             )

#     return discovery_filters


def pre_validate_credential_input(
    cred_name: str, credential_entry: dict
) -> tuple[str, dict]:
    match credential_entry:
        case {
            "username": _,
            "snmpuser": _,
        }:
            raise ValueError(
                f"SNMPv3c and User creds should be defined separately: {cred_name}",
            )

        case {
            "username": _,
            "community": _,
        }:
            raise ValueError(
                f"SNMPv2 and User creds should be defined separately: {cred_name}",
            )

        case {
            "snmpuser": _,
            "community": _,
        }:
            raise ValueError(
                f"SNMPv3 and SNMPv2c creds should be defined separately: {cred_name}",
            )

        case {
            "username": _,
            "password": _,
        }:
            return cred_name, credential_entry

        case {
            "username": _,
        }:
            raise ValueError(
                f"Username cannot be configured without a password: {cred_name}",
            )
        case {
            "community": _,
        }:
            return cred_name, credential_entry

        case {
            "snmpuser": _,
            "authtype": _,
            "privtype": _,
            "auth": _,
            "priv": _,
        }:
            return cred_name, credential_entry

        case {
            "snmpuser": snmpuser,
        }:
            raise ValueError(
                f"SNMPv3 cannot be configured without authtype, privtype, auth & priv: {cred_name}",
            )
        case _:
            raise ValueError(
                f"Invalid configuration section: {cred_name}",
            )


def get_raw_config(
    config_file: str,
) -> tuple[list[dict | list], list[tuple[str, dict]], dict]:

    pathobj = pathlib.Path(config_file)
    locations = [pathobj, pathlib.Path.joinpath(pathlib.Path.home(), pathobj)]
    config = {}
    for location in locations:
        with contextlib.suppress(OSError):
            with open(location) as file:
                config = yaml.safe_load(file)
                break

    # pre_validated_discovery_filters: dict | list = []
    pre_validated_credentials: list[tuple[str, dict]] = []
    pre_validated_args: dict = {}
    # pre_validated_section: dict = {}
    for key, value in config.items():
        match key, value:
            # Sections peeled off first
            # case "discovery_filters", discovery_filters:
            #     pre_validated_discovery_filters = discovery_filters
            # case "section_name", section_name:
            #     pre_validated_section = section_name

            # Unknown sections are treated as potential credentials
            case cred_name, dict():
                if pre_validated := pre_validate_credential_input(cred_name, value):
                    pre_validated_credentials.append(pre_validated)

            # Option types last
            case arg_argname, str() | bool() | int():
                pre_validated_args[arg_argname] = value

            # Anything else, dunno
            case key, value:
                raise ValueError(
                    f"Config file contains unexpected type for key: {key}: {type(value)}",
                )
    return (
        pre_validated_args,
        pre_validated_credentials,
        # pre_validated_discovery_filters,
        # pre_validated_section,
    )


def get_netdisc_args() -> tuple[
    defaults.NetdiscConfig,
    authen.AuthMethodList,
    # filter_.FilterList,
    hostlist.HostListAccumulator,
]:
    # Load all eligible arguments and their defaults
    args = defaults.NetdiscConfig()

    # Load cli args to get potential new config_file info
    cli_args = cli.get_cli_args()
    config_file = cli_args.config_file or args.config_file

    # Load raw config file
    (
        pre_args,
        pre_discovery_credentials,
        # pre_discovery_filters,
    ) = get_raw_config(config_file)

    # Peel out hostfiles
    hla = hostlist.HostListAccumulator()
    hla.ingest(vars(cli_args).pop("ip", None))
    hla.ingest(vars(cli_args).pop("hostfile", None))
    hla.ingest(pre_args.pop("ip", None))
    hla.ingest(pre_args.pop("hostfile", None))

    # Base args are layered with config file args, then cli args
    vars(args).update(pre_args)
    vars(args).update(vars(cli_args))

    # Auth methods are validated
    auth_methods = validate_credential_list(args, pre_discovery_credentials)

    # Filter list is validated
    # filter_list = validate_discovery_filter_input(pre_discovery_filters)
    # return args, auth_methods, filter_list, hla
    return args, auth_methods, hla
