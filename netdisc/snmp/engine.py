import abc
import dataclasses
import logging

from netdisc.snmp import mibhelp, snmpbase

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class SNMPEngineAbstract(abc.ABC):
    @abc.abstractmethod
    def setup(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, *paths) -> list[tuple]:
        raise NotImplementedError

    @abc.abstractmethod
    def walk(self, *paths) -> list[tuple]:
        raise NotImplementedError

    @abc.abstractmethod
    def object_paths_compile(
        self,
        binding: snmpbase.VarBindBase,
        index: str | int = None,
    ) -> list:
        raise NotImplementedError

    @abc.abstractmethod
    def object_get(
        self, binding: snmpbase.VarBindBase, convert: bool
    ) -> list[snmpbase.VarBindBase] | snmpbase.VarBindBase:
        raise NotImplementedError

    @abc.abstractmethod
    def object_zero(self, binding: snmpbase.ZeroIndex) -> snmpbase.ZeroIndex:
        raise NotImplementedError

    @abc.abstractmethod
    def object_walk(
        self, binding: snmpbase.WalkRequired
    ) -> list[snmpbase.WalkRequired]:
        raise NotImplementedError

    @abc.abstractmethod
    def cisco_vlan_fuckery(
        self, binding: snmpbase.CiscoVLANFuckery
    ) -> snmpbase.VarBindBase:
        raise NotImplementedError

    @abc.abstractmethod
    def set_cisco_vlans(self, vlans: list[int]) -> None:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def set_v3_auth_priv(
        snmpuser: str,
        authtype: str,
        auth: str,
        privtype: str,
        priv: str,
    ) -> dict:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def set_v3_auth(
        snmpuser: str,
        authtype: str,
        auth: str,
    ) -> dict:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def set_v3(
        snmpuser: str,
    ) -> dict:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def set_v2(
        community: str,
    ) -> dict:
        raise NotImplementedError


@dataclasses.dataclass
class SNMPEngine(SNMPEngineAbstract):
    FLAGS = snmpbase.MIBXlate.NONE
    """netdisc snmp engine

    Args:
        host (str): _description_
        port (int): Port
        community (str): <community string>
        snmpuser (str): <username, or security name>
        auth (str): <authentication string>
        authtype (str): [ MD5 | SHA ]
        priv (str): <privacy string>
        privtype (str): [ AES | DES | 3DES ]

    Raises:
        ValueError: Any issues during setup
        RunTimeError: When any issues come up after running

    """

    host: str = (None,)
    port: int = 161
    community: str = None
    snmpuser: str = None
    auth: str = None
    authtype: str = None
    priv: str = None
    privtype: str = None
    cisco_vlan: int = None
    flags: snmpbase.MIBXlate = None

    def object_get(
        self,
        binding: snmpbase.VarBindBase,
        convert: bool = False,
    ) -> list[snmpbase.VarBindBase] | snmpbase.VarBindBase:
        assert issubclass(binding, snmpbase.VarBindBase)
        logger.debug("Received instance of VarBindBase")
        if issubclass(binding, snmpbase.CiscoVLANFuckery) and not self.cisco_vlan:
            logger.debug("It is CiscoVLANFuckery")
            result = self.cisco_vlan_fuckery(binding)
        elif issubclass(binding, snmpbase.WalkRequired):
            logger.debug("It is WalkRequired")
            result = self.object_walk(binding)
        elif issubclass(binding, snmpbase.ZeroIndex):
            logger.debug("It is ZeroIndex")
            result = self.object_zero(binding)
        if convert:
            self.mib_helper.convert_binding_fields(result)
        return result

    def object_walk(self, binding: type[snmpbase.WalkRequired]):
        assert isinstance(binding, type)
        assert issubclass(binding, snmpbase.WalkRequired)

        self.mib_helper.load_mib(binding)
        object_paths = self.object_paths_compile(binding)

        results = self.walk(*object_paths)

        result_dict = binding.CONTAINER()
        for index, field, value in results:
            to_int = lambda index: int(index) if str(index).isdigit() else index
            if isinstance(index, tuple):
                to_ints = tuple(to_int(i) for i in index)
                converted_index = binding.INDEX(*to_ints)
            else:
                converted_index = binding.INDEX(to_int(index))
            logger.debug("Index: %s Field: %s Value: %s", index, field, value)
            setattr(result_dict.setdefault(converted_index, binding()), field, value)
        return result_dict

    def object_zero(self, binding: snmpbase.ZeroIndex):
        test_obj = binding
        assert isinstance(test_obj, type)
        # The type hinter labels test_obj as "Never" after this is run
        assert issubclass(test_obj, snmpbase.ZeroIndex)
        self.mib_helper.load_mib(binding)

        object_paths = self.object_paths_compile(binding, index=0)

        results = self.get(*object_paths)

        new_binding = binding()
        for index, field, value in results:
            logger.debug("Index: %s Field: %s Value: %s", index, field, value)
            setattr(new_binding, field, value)
        return new_binding

    def cisco_vlan_fuckery(
        self, binding: snmpbase.CiscoVLANFuckery
    ) -> snmpbase.VarBindBase:
        if not self.cisco_vlan_instances:
            raise RuntimeError(
                "Unable to process Cisco Vlan object until cisco vlans have been set"
            )
        result = {}
        for vlan, instance in self.cisco_vlan_instances.items():
            result[vlan] = instance.object_get(binding)
        return result

    def set_cisco_vlans(self, vlans: list[int]) -> None:
        if not vlans:
            raise ValueError("Cisco VLAN list must include at least Vlan 1")
        for vlan in vlans:
            assert isinstance(vlan, int)
            logger.debug(
                "Instantiating: %s(cisco_vlan=%s)",
                type(self),
                vlan,
            )
            kwargs = {
                key: getattr(self, key)
                for key in dataclasses.asdict(self)
                if key != "cisco_vlan"
            }
            self.cisco_vlan_instances[vlan] = type(self)(
                cisco_vlan=vlan,
                **kwargs,
            )

    def __post_init__(self):
        if self.flags is not None:
            self.FLAGS = self.flags
        self.mib_helper = mibhelp.MIBHelper(self.FLAGS)
        logger.debug(
            "Instantiated.  MibHelper: %s.  Cisco VLAN: %s",
            self.mib_helper,
            self.cisco_vlan,
        )
        self.cisco_vlan_instances = {}
        self.credential = {}
        match (
            self.snmpuser,
            self.authtype,
            self.auth,
            self.privtype,
            self.priv,
            self.community,
        ):
            case (
                str(snmpuser),
                str(authtype),
                str(auth),
                str(privtype),
                str(priv),
                None,
            ):
                self.set_v3_auth_priv(
                    snmpuser,
                    authtype,
                    auth,
                    privtype,
                    priv,
                )
            case (
                str(snmpuser),
                str(authtype),
                str(auth),
                None,
                None,
                None,
            ):
                self.set_v3_auth(
                    snmpuser,
                    authtype,
                    auth,
                )
            case (
                str(snmpuser),
                None,
                None,
                None,
                None,
                None,
            ):
                self.set_v3(
                    snmpuser,
                )
            case (
                None,
                None,
                None,
                None,
                None,
                str(community),
            ):
                self.set_v2(
                    community,
                )
            case snmpuser, authtype, auth, privtype, priv, community:
                raise ValueError(
                    (
                        f"Invalid input:"
                        f" {snmpuser=}, {authtype=}, {auth=}, {privtype=}, {priv=}, {community=}"
                    )
                )
        self.setup()
