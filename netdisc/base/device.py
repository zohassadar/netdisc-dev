import logging
import typing
import functools
from netdisc.tools import helpers


ORM_BUILTINS = ("registry", "metadata", "mro")

builtin_filter = lambda key: not key.startswith("_") and not key in ORM_BUILTINS

orm_helper = helpers.dict_repr_helper(filter_=builtin_filter)
add_kwargs_init = helpers.add_kwargs_init(filter_=builtin_filter)

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
    address = sqlalchemy.Column(sqlalchemy.String)


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
    # vlans = orm.relationship("VLAN")
    # vlan_interfaces = orm.relationship(VLANInterface.__name__)
    ip_addresses = orm.relationship("IP")
    ipv6_addresses = orm.relationship("IPv6")


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
    vlans: typing.List[VLAN] = orm.relationship(VLAN.__name__)
    vrfs: typing.List[VRF] = orm.relationship(VRF.__name__)
    routes: typing.List[Route] = orm.relationship(Route.__name__)
    ip_addresses: typing.List[IP] = orm.relationship(IP.__name__)
    ipv6_addresses: typing.List[IPv6] = orm.relationship(IPv6.__name__)
    macs: typing.List[MAC] = orm.relationship(MAC.__name__)
    arps: typing.List[ARP] = orm.relationship(ARP.__name__)

    def _clear_cached_properties(self):
        for name in dir(type(self)):
            if isinstance(getattr(type(self), name), functools.cached_property):
                print(f"Clearing self.{name}")
                vars(self).pop(name, None)

    @functools.cached_property
    def interfaces_dict(self) -> dict[str, Interface]:
        return {i.interface_name: i for i in self.interfaces}

    def get_interface(self, interface_name) -> Interface | None:
        return self.interfaces_dict.get(interface_name)

    @functools.cached_property
    def neighbors_dict(self) -> dict[str, Neighbor]:
        return {(n.interface_name, n.hostname, n.interface): n for n in self.neighbors}

    def get_neighbor(self, interface_name, hostname, interface) -> Neighbor | None:
        return self.neighbors_dict.get((interface_name, hostname, interface))

    @functools.cached_property
    def routes_dict(self) -> dict[str, Route]:
        return {(r.network_id, r.mask_len, r.vrf_name): r for r in self.routes}

    def get_route(self, network_id, mask_len, vrf_name=None) -> Route | None:
        return self.routes_dict.get((network_id, mask_len, vrf_name))

    @functools.cached_property
    def ip_addresses_dict(self) -> dict[str, IP]:
        return {(i.address, i.vrf_name): i for i in self.ip_addresses}

    def get_ip_address(self, address, vrf_name=None) -> IP | None:
        return self.ip_addresses_dict.get((address, vrf_name))

    @functools.cached_property
    def ipv6_addresses_dict(self) -> dict[str, IPv6]:
        return {(i.address, i.vrf_name): i for i in self.ipv6_addresses}

    def get_ipv6_address(self, address, vrf_name=None) -> IPv6 | None:
        return self.ipv6_addresses_dict.get((address, vrf_name))

    @functools.cached_property
    def vrfs_dict(self) -> dict[str, VRF]:
        return {v.vrf_name: v for v in self.vrfs}

    def get_vrf(self, vrf_name) -> VRF | None:
        return self.ipv6_addresses_dict.get(vrf_name)

    @functools.cached_property
    def mac_addresses_dict(self) -> dict[str, MAC]:
        return {(m.vlan_id, m.mac_address): m for m in self.macs}

    def get_mac(self, vlan_id, mac_address) -> MAC | None:
        return self.mac_addresses_dict.get((vlan_id, mac_address))

    @functools.cached_property
    def arp_entries_dict(self) -> dict[str, ARP]:
        return {(a.address, a.vrf_name): a for a in self.arps}

    def get_arp(self, address, vrf_name=None) -> ARP | None:
        return self.arp_entries_dict.get((address, vrf_name))

    @functools.cached_property
    def vlans_dict(self) -> dict[int, VLAN]:
        return {v.vlan_id: v for v in self.vlans}

    def get_vlan(self, vlan_id) -> VLAN | None:
        return self.vlans_dict.get(vlan_id)

    def dump(self):
        return {
            "interfaces": [dict(o) for o in self.interfaces],
            "neighbors": [dict(o) for o in self.neighbors],
            "vlans": [dict(o) for o in self.vlans],
            "routes": [dict(o) for o in self.routes],
            "ip_addresses": [dict(o) for o in self.ip_addresses],
            "ipv6_addresses": [dict(o) for o in self.ipv6_addresses],
            "macs": [dict(o) for o in self.macs],
            "arps": [dict(o) for o in self.arps],
            "vrfs": [dict(o) for o in self.routes],
        }

    def load_partial(self, dumped: dict):
        no_lists = {k: v for k, v in dumped.items() if not isinstance(v, list)}
        self.update(no_lists)

    def load_list(self, dumped, container, get_func, args, obj):
        loaded_container = getattr(self, container, None)
        if loaded_container is None:
            raise ValueError(f"Device does not have list: {container}")
        elif not isinstance(loaded_container, list):
            raise ValueError(
                f"Device field is not list: {container} {type(loaded_container)}"
            )

        getter = getattr(self, get_func)
        for entry in dumped.get(container, []):
            key = tuple(entry.get(a) for a in args)
            if existing := getter(*key):
                existing.update(entry)
            else:
                loaded_container.append(obj(**entry))

    def load(self, dumped: dict):
        self.load_partial(dumped)
        setups = (
            (
                "interfaces",
                "get_interface",
                ("interface_name",),
                Interface,
            ),
            (
                "neighbors",
                "get_neighbor",
                ("interface_name", "hostname", "interface"),
                Neighbor,
            ),
            (
                "ip_addresses",
                "get_ip_address",
                ("address", "vrf_name"),
                IP,
            ),
            (
                "ipv6_addresses",
                "get_ipv6_address",
                ("address", "vrf_name"),
                IP,
            ),
            (
                "vrfs",
                "get_vrf",
                ("vrf_name",),
                IP,
            ),
            (
                "vlans",
                "get_vlan",
                ("vlan_id",),
                VLAN,
            ),
            (
                "macs",
                "get_mac",
                ("vlan_id", "mac_address"),
                VLAN,
            ),
            (
                "arps",
                "get_arp",
                ("address", "vrf_name"),
                ARP,
            ),
        )
        for setup in setups:
            self.load_list(dumped, *setup)
        self._clear_cached_properties()
