import enum


PROTO_API = "api"
PROTO_SNMPv3 = "snmpv3"
PROTO_SNMPv2c = "snmpv2c"
PROTO_SSH = "ssh"
PROTO_TELNET = "telnet"


KEYS_FILTER = (
    "hostname_include",
    "hostname_exclude",
    "network_include",
    "network_exclude",
)


KEYS_AUTH = (
    "username",
    "password",
    "community",
    "snmpuser",
    "authtype",
    "auth",
    "privtype",
    "priv",
    "port",
)

KEYS_DB = ("dbfile",)


class Discovery(enum.IntFlag):
    INTERFACES = enum.auto()
    VRFS = enum.auto()
    IP_ADDRESSES = enum.auto()
    IPv6_ADDRESSES = enum.auto()
    IP_DETAIL = enum.auto()
    NEIGHBORS = enum.auto()
    ROUTES = enum.auto()
    VLANS = enum.auto()
    STP = enum.auto()
    ARPS = enum.auto()
    MACS = enum.auto()
    DNS = enum.auto()
    # New below here

    # New above here
    DEVICE_INFO = 0
    FULL = -1
    FAST = INTERFACES | VRFS | IP_ADDRESSES | NEIGHBORS
    MEDIUM = FAST | DNS | ROUTES
    SLOW = MEDIUM | ARPS

    # Potential combos
    ARPMAC = ARPS | MACS
    LAYER2 = VLANS | STP | MACS
    LAYER3 = VRFS | IP_ADDRESSES | IPv6_ADDRESSES | IP_DETAIL | ROUTES | ARPS


class Proto(enum.Enum):
    TELNET = PROTO_TELNET
    SSH = PROTO_SSH
    SNMPv3 = PROTO_SNMPv3
    SNMPv2c = PROTO_SNMPv2c
    API = PROTO_API

    def __str__(self):
        return self.value


DEVICE_IOS = "ios"
DEVICE_IOSXE = "iosxe"
DEVICE_ASA = "asa"
DEVICE_NXOS = "nxos"
DEVICE_IOSXR = "iosxr"
DEVICE_EOS = "eos"


class DeviceTypes(enum.Enum):
    ios = DEVICE_IOS
    iosxe = DEVICE_IOSXE
    iosxr = DEVICE_IOSXR
    nxos = DEVICE_NXOS
    asa = DEVICE_ASA
    eos = DEVICE_EOS
