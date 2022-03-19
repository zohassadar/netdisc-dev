import logging
import ipaddress
import socket
import functools
import dataclasses

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


@dataclasses.dataclass
class HostListAccumulator:
    hostlist: list = dataclasses.field(default_factory=list)

    def __post_init__(self):
        logger.debug("Host list generator initialized")
        self._opened_files = []

    def add_host(self, host: str):
        logger.debug("Attempting to validate what this string is: %s", host)
        host = host.strip()

        comma_separated = host.split(",")
        if len(comma_separated) > 1:
            logger.debug("This is comma separated: %s", host)
            self.ingest(comma_separated)
            return

        space_seperated = host.split()
        if len(space_seperated) > 1:
            logger.debug("This is space separated: %s", host)
            self.ingest(space_seperated)
            return

        if not host:
            logger.debug("Host is a blank string. Skipping")
            return

        logger.debug("Attempting to validate as IP address: %s", host)
        try:
            ipaddress.IPv4Address(host)
            if host not in self.hostlist:
                self.hostlist.append(host)
            return
        except ipaddress.AddressValueError:
            logger.debug("Not an IP Address: %s", host)

        logger.debug("Attempting to resolve: %s", host)
        try:
            host = socket.gethostbyname(host)
            if host not in self.hostlist:
                self.hostlist.append(host)
            return
        except socket.gaierror:
            logger.debug("Unresolvable hostname provided: %s", host)

        logger.debug("Attempting to load as file: %s", host)
        if host in self._opened_files:
            logger.error("Circular file reference: %s", host)
            return
        try:
            self._opened_files.append(host)
            with open(host) as f:
                self.add_host(f.read())
        except FileNotFoundError:
            logger.error("Invalid host entry: %s", host)

    @functools.singledispatchmethod
    def ingest(self, unknown):
        raise ValueError(f"Unknown type to get host from: {type(unknown)}")

    @ingest.register
    def _(self, host: str):
        logger.debug("String received for host list")
        self.add_host(host)

    @ingest.register
    def _(self, host: bytes):
        logger.debug("Bytes received for host list")
        try:
            host = ipaddress.IPv4Address(host)
        except:
            logger.debug("Bytes provided is not an IP address: %s", host)
        self.add_host(str(host))

    @ingest.register
    def _(self, host: int):
        logger.debug("int received for host list")
        try:
            host = ipaddress.IPv4Address(host)
        except:
            logger.debug("Int provided is not an IP address: %s", host)
        self.add_host(str(host))

    @ingest.register
    def _(self, hostlist: list):
        logger.debug("List received for host list")
        for host in hostlist:
            self.add_host(host)

    @ingest.register
    def _(self, hostlist: tuple):
        logger.debug("Tuple received for host list")
        for host in hostlist:
            self.ingest(host)

    @ingest.register
    def _(self, hostlist: dict):
        logger.debug("Dict received for host list")
        for host in hostlist.values():
            self.ingest(host)

    @ingest.register
    def _(self, nothing: None):
        ...
