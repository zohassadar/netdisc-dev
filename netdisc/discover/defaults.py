import dataclasses
import enum

from netdisc.base import constant


VERBOSE = 5

LOG_FILE = None
LOG_FILE_DEPTH = 1

DISCOVER_SSH = True
DISCOVER_SNMP = True
DISCOVER_API = True
DISCOVER_TELNET = True
DISCOVER_RETRIES = 0

KEEP_SCORE = False

PORT_API = 443
PORT_SNMP = 161
PORT_SSH = 22
PORT_TELNET = 23

DEAD_TIMER = 5
LOOP_SLEEP = 1


WORKER_LIMIT = 2
WORKER_SLEEP = 1

CONFIG_FILE = "netdisc.yaml"

SERVER_MODE = False
RETRIES = 1


@dataclasses.dataclass
class NetdiscConfig:
    """
    All netdisc options are defined here.

    Config and
    """

    hostlist: str = None  # Starting IP Addresses
    customer_name: str = None
    network_name: str = None
    server_mode: bool = SERVER_MODE
    verbose: int = VERBOSE
    log_file: str = LOG_FILE
    log_file_depth: int = LOG_FILE_DEPTH

    snmp: bool = DISCOVER_SNMP
    api: bool = DISCOVER_API
    ssh: bool = DISCOVER_SSH
    telnet: bool = DISCOVER_TELNET
    retries: int = DISCOVER_RETRIES

    keep_score: bool = KEEP_SCORE

    loop_sleep = LOOP_SLEEP
    dead_timer = DEAD_TIMER

    workers: int = WORKER_LIMIT
    worker_sleep: int = WORKER_SLEEP

    snmp_port: int = PORT_SNMP
    telnet_port: int = PORT_TELNET
    api_port: int = PORT_API
    ssh_port: int = PORT_SSH

    config_file: str = CONFIG_FILE

    _initialized = False  # Part of the locking mechanism

    def __post_init__(self):
        """Flag set after object is initialized"""
        self._initialized = True

    def __setattr__(self, key, value):
        """Enforce no new attributes after object creation"""
        if self._initialized and hasattr(self, key) or not self._initialized:
            object.__setattr__(self, key, value)
        else:
            raise AttributeError(f"{self.__class__.__name__} cannot add new attribute")
