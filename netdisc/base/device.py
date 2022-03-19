import enum
import logging
import typing

from netdisc.tools import helpers
from netdisc.base import constant

ORM_BUILTINS = ("registry", "metadata", "mro")

builtin_filter = lambda key: not key.startswith("_") and not key in ORM_BUILTINS

orm_helper = helpers.dict_repr_helper(filter=builtin_filter)
add_kwargs_init = helpers.add_kwargs_init(filter=builtin_filter)

TABLE_ARP = "arp"
TABLE_DEVICE = "device"
TABLE_INTERFACE = "interface"
TABLE_IP = "ip_addresses"
TABLE_IPV6 = "ipv6_addresses"
TABLE_MAC = "mac"
TABLE_NBR = "neighbor"
TABLE_ROUTE = "route"
TABLE_VLAN = "vlan"
TABLE_VLAN_INTERFACE = "vlan_interface"
TABLE_VRF = "vrf"

KEY_DEVICE = "device_ip"
KEY_INTERFACE = "interface_name"
KEY_VLAN = "vlan_id"
KEY_VRF = "vrf_name"
import logging

try:
    import sqlalchemy
    from sqlalchemy import orm

    DeclarativeBase = orm.declarative_base()
    logging.critical("sqlalchemy loaded")
except (ModuleNotFoundError, AttributeError):

    @add_kwargs_init
    class DeclarativeBase:
        ...

    class sqlalchemy:
        Column = String = Integer = Boolean = ForeignKey = helpers.dummy

    class orm:
        relationship = helpers.fake_orm_relationship

    logging.critical("faklalchemy loaded")


@orm_helper
class Neighbor(DeclarativeBase):
    """Neighbor _summary_

    Parameters
    ----------
    device_ip : str
        IP address (foreign key) of device.  Not specific to interface.
    interface_name : str
        Interface associated with neighbor
    interface : str
       Neighbor interface
    hostname : str
       Neighbor hostname
    ip : str
       Neighbor IP address
    secondary_ip : str
       Secondary IP address
    model : str
       Model of the device
    version : str
       Software version of the device
    sysinfo : str
       Sysinfo string provided by neighbor
    """

    __tablename__ = TABLE_NBR
    device_ip = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_DEVICE, KEY_DEVICE))),
    )
    interface_name = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_INTERFACE, KEY_INTERFACE))),
    )
    interface = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    hostname = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    ip = sqlalchemy.Column(sqlalchemy.String)
    secondary_ip = sqlalchemy.Column(sqlalchemy.String)
    model = sqlalchemy.Column(sqlalchemy.String)
    version = sqlalchemy.Column(sqlalchemy.String)
    sysinfo = sqlalchemy.Column(sqlalchemy.String)


@orm_helper
class Route(DeclarativeBase):
    __tablename__ = TABLE_ROUTE
    device_ip = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_DEVICE, KEY_DEVICE))),
    )
    vrf_name = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_VRF, KEY_VRF))),
    )
    network_id = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    mask_len = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
    )
    next_hop = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    protocol = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    admin_distance = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    metric = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )


@orm_helper
class IP(DeclarativeBase):
    __tablename__ = TABLE_IP
    device_ip = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_DEVICE, KEY_DEVICE))),
    )
    interface_name = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_INTERFACE, KEY_INTERFACE))),
    )
    vrf_name = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_VRF, KEY_VRF))),
    )
    address = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    mask_len = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
    )
    is_secondary = sqlalchemy.Column(
        sqlalchemy.Boolean,
        default=False,
    )
    is_virtual = sqlalchemy.Column(
        sqlalchemy.Boolean,
        default=False,
    )
    is_loopback = sqlalchemy.Column(
        sqlalchemy.Boolean,
        default=False,
    )


@orm_helper
class IPv6(DeclarativeBase):
    __tablename__ = TABLE_IPV6
    device_ip = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_DEVICE, KEY_DEVICE))),
    )
    interface_name = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_INTERFACE, KEY_INTERFACE))),
    )
    vrf_name = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_VRF, KEY_VRF))),
    )
    address = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    mask_len = sqlalchemy.Column(sqlalchemy.Integer)
    is_secondary = sqlalchemy.Column(
        sqlalchemy.Boolean,
        default=False,
    )
    is_virtual = sqlalchemy.Column(
        sqlalchemy.Boolean,
        default=False,
    )
    is_loopback = sqlalchemy.Column(
        sqlalchemy.Boolean,
        default=False,
    )


@orm_helper
class VRF(DeclarativeBase):
    __tablename__ = TABLE_VRF
    device_ip = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_DEVICE, KEY_DEVICE))),
    )
    vrf_name = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    rd = sqlalchemy.Column(sqlalchemy.String)
    ip_addresses = orm.relationship(IP.__name__)
    ipv6_addresses = orm.relationship(IPv6.__name__)
    routes = orm.relationship(Route.__name__)


@orm_helper
class MAC(DeclarativeBase):
    __tablename__ = TABLE_MAC
    device_ip = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(
            ".".join((TABLE_DEVICE, KEY_DEVICE)),
        ),
    )
    interface_name = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(
            ".".join((TABLE_INTERFACE, KEY_INTERFACE)),
        ),
    )
    vlan_id = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(
            ".".join((TABLE_VLAN, KEY_VLAN)),
        ),
    )
    mac_address = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )


@orm_helper
class ARP(DeclarativeBase):
    __tablename__ = TABLE_ARP
    device_ip = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(
            ".".join((TABLE_DEVICE, KEY_DEVICE)),
        ),
    )
    interface_name = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(
            ".".join((TABLE_INTERFACE, KEY_INTERFACE)),
        ),
    )
    vrf_name = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(
            ".".join((TABLE_VRF, KEY_VRF)),
        ),
    )
    mac_address = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    ip_address = sqlalchemy.Column(sqlalchemy.String)


@orm_helper
class Interface(DeclarativeBase):
    """Interface _summary_

    Parameters
    ----------
    device_ip : str
        IP address (foreign key) of device.  Not specific to interface.
    interface_name : str
        Full name of interface (e.g. FastEthernet0/0/0)
    description : str
        Interface description if configured
    speed : int
        Speed, in megabits per second
    duplex : str
        Current duplex of device
    media : str
        Media type of interface

    Instance properties:
    vlans : list[VLAN]
    vlan_interfaces: list[VLANInterface]
    ip_addresses: list[IP]
    ipv6_addresses: list[IPv6]
    """

    __tablename__ = TABLE_INTERFACE
    device_ip = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_DEVICE, KEY_DEVICE))),
    )
    interface_name = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    description = sqlalchemy.Column(sqlalchemy.String)
    media = sqlalchemy.Column(sqlalchemy.String)
    speed = sqlalchemy.Column(sqlalchemy.String)
    duplex = sqlalchemy.Column(sqlalchemy.String)
    media = sqlalchemy.Column(sqlalchemy.String)
    # vlans = orm.relationship(VLAN.__name__)
    # vlan_interfaces = orm.relationship(VLANInterface.__name__)
    ip_addresses = orm.relationship(IP.__name__)
    ipv6_addresses = orm.relationship(IPv6.__name__)


# @orm_helper
# class VLANInterface(DeclarativeBase):
#     __tablename__ = TABLE_VLAN_INTERFACE
#     device_ip = sqlalchemy.Column(
#         sqlalchemy.String, sqlalchemy.ForeignKey(".".join((TABLE_DEVICE, KEY_DEVICE)))
#     )
#     interface_name = sqlalchemy.Column(
#         sqlalchemy.String,
#         sqlalchemy.ForeignKey(".".join((TABLE_INTERFACE, KEY_INTERFACE))),
#     )
#     vlan_id = sqlalchemy.Column(
#         sqlalchemy.Integer, sqlalchemy.ForeignKey(".".join((TABLE_VLAN, KEY_VLAN)))
#     )
#     native = sqlalchemy.Column(sqlalchemy.Boolean)
#     access = sqlalchemy.Column(sqlalchemy.Boolean)
#     trunk = sqlalchemy.Column(sqlalchemy.Boolean)
#     voice = sqlalchemy.Column(sqlalchemy.Boolean)
#     # macs = orm.relationship(MAC.__name__)


# an example mapping using the base
@orm_helper
class Device(DeclarativeBase):
    __tablename__ = TABLE_DEVICE
    device_ip = sqlalchemy.Column(
        sqlalchemy.String,
        primary_key=True,
    )
    hostname = sqlalchemy.Column(sqlalchemy.String)
    full_hostname = sqlalchemy.Column(sqlalchemy.String)
    domain_name = sqlalchemy.Column(sqlalchemy.String)
    location = sqlalchemy.Column(sqlalchemy.String)
    contact = sqlalchemy.Column(sqlalchemy.String)
    model = sqlalchemy.Column(sqlalchemy.String)
    sysinfo = sqlalchemy.Column(sqlalchemy.String)
    version = sqlalchemy.Column(sqlalchemy.String)
    failed = sqlalchemy.Column(sqlalchemy.Boolean)
    failure_reason = sqlalchemy.Column(sqlalchemy.String)
    authentication_failure = sqlalchemy.Column(sqlalchemy.Boolean)
    failure_history = sqlalchemy.Column(sqlalchemy.String)

    interfaces: typing.List[Interface] = orm.relationship(Interface.__name__)
    neighbors: typing.List[Neighbor] = orm.relationship(Neighbor.__name__)
    # vlans: typing.List[VLAN] = orm.relationship(VLAN.__name__)
    vrfs: typing.List[VRF] = orm.relationship(VRF.__name__)
    routes: typing.List[Route] = orm.relationship(Route.__name__)
    ip_addresses: typing.List[IP] = orm.relationship(IP.__name__)
    ipv6_addresses: typing.List[IPv6] = orm.relationship(IPv6.__name__)
    macs: typing.List[MAC] = orm.relationship(MAC.__name__)
    arps: typing.List[ARP] = orm.relationship(ARP.__name__)

    @helpers.debugger()
    def dump(self):
        return {
            TABLE_INTERFACE: [dict(o) for o in self.interfaces],
            TABLE_NBR: [dict(o) for o in self.neighbors],
            TABLE_VLAN: [dict(o) for o in self.vlans],
            TABLE_ROUTE: [dict(o) for o in self.routes],
            TABLE_IP: [dict(o) for o in self.ip_addresses],
            TABLE_IPV6: [dict(o) for o in self.ipv6_addresses],
            TABLE_MAC: [dict(o) for o in self.macs],
            TABLE_ARP: [dict(o) for o in self.arps],
            TABLE_VRF: [dict(o) for o in self.routes],
        }

    @helpers.debugger()
    def load_partial(self, dumped):
        for key, value in dumped.items():
            if not isinstance(value, list):
                setattr(self, key, value)

    @helpers.debugger()
    def load(self, dumped):
        self.load_partial(dumped)
        self.interfaces = [Interface(**o) for o in dumped.get(TABLE_INTERFACE, [])]
        self.neighbors = [Neighbor(**o) for o in dumped.get(TABLE_NBR, [])]
        self.vlans = [VLAN(**o) for o in dumped.get(TABLE_VLAN, [])]
        self.vrfs = [VRF(**o) for o in dumped.get(TABLE_VRF, [])]
        self.ip_addresses = [IP(**o) for o in dumped.get(TABLE_IP, [])]
        self.ipv6_addresses = [IPv6(**o) for o in dumped.get(TABLE_IPV6, [])]
        self.routes = [Route(**o) for o in dumped.get(TABLE_ROUTE, [])]
        self.macs = [MAC(**o) for o in dumped.get(TABLE_MAC, [])]
        self.arps = [ARP(**o) for o in dumped.get(TABLE_ARP, [])]

    def add_interface(self, **kwargs):
        self.interfaces.append(Interface(**kwargs))

    def add_neighbor(self, **kwargs):
        self.neighbors.append(Neighbor(**kwargs))

    def add_ip_address(self, **kwargs):
        self.ip_addresses.append(IP(**kwargs))

    def add_ipv6_address(self, **kwargs):
        self.ipv6_addresses.append(IPv6(**kwargs))

    def add_vrf(self, **kwargs):
        self.vrfs.append(VRF(**kwargs))

    def add_vlan(self, **kwargs):
        self.vlans.append(VLAN(**kwargs))

    def add_mac(self, **kwargs):
        self.macs.append(MAC(**kwargs))

    def add_arp(self, **kwargs):
        self.arps.append(ARP(**kwargs))

    def add_route(self, **kwargs):
        self.routes.append(Route(**kwargs))


@orm_helper
class VLAN(DeclarativeBase):
    __tablename__ = TABLE_VLAN
    device_ip = sqlalchemy.Column(
        sqlalchemy.String,
        sqlalchemy.ForeignKey(".".join((TABLE_DEVICE, KEY_DEVICE))),
    )
    vlan_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        primary_key=True,
    )
    name = sqlalchemy.Column(sqlalchemy.String)
    # vlan_interfaces = orm.relationship(VLANInterface.__name__)
