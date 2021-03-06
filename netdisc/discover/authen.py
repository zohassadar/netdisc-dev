from netdisc.base import constant
import dataclasses
import typing
import collections
import logging


@dataclasses.dataclass
class AuthMethod:
    _EXCLUDED_KEYS = ["index", "name", "proto"]
    name: str = None
    index: int = 0
    proto: str = None
    retries: int = 0
    port: int = 0
    username: str = None
    password: str = None
    secret: str = None
    community: str = None
    snmpuser: str = None
    authtype: str = None
    auth: str = None
    privtype: str = None
    priv: str = None

    def __post_init__(self):
        credential_validate_set = (
            self.username,
            self.password,
            self.secret,
            self.community,
            self.snmpuser,
            self.authtype,
            self.auth,
            self.priv,
            self.privtype,
        )
        match credential_validate_set:
            case (
                str(),  # username
                str(),  # password
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ):
                pass
            case (
                str(),  # username
                str(),  # password
                str(),  # secret
                None,
                None,
                None,
                None,
                None,
                None,
            ):
                pass
            case (
                None,
                None,
                None,
                str(),  # community
                None,
                None,
                None,
                None,
                None,
            ):
                pass
            case (
                None,
                None,
                None,
                None,
                str(),  # snmpuser
                None,
                None,
                None,
                None,
            ):
                pass
            case (
                None,
                None,
                None,
                None,
                str(),  # snmpuser
                str(),  # authtype
                str(),  # auth
                None,
                None,
            ):
                pass
            case (
                None,
                None,
                None,
                None,
                str(),  # snmpuser
                str(),  # authtype
                str(),  # auth
                str(),  # priv
                str(),  # privtype
            ):
                pass
            case _:
                raise ValueError(
                    f"Invalid credential options: {credential_validate_set}"
                )

    @property
    def protoport(self):
        return str(self.proto) + str(self.port)

    @property
    def kwargs(self):
        return {
            k: v
            for k, v in dataclasses.asdict(self).items()
            if v and k not in self._EXCLUDED_KEYS
        }


@dataclasses.dataclass
class ScoreKeeper:
    keep_score: bool
    scores: collections.defaultdict = dataclasses.field(
        default_factory=lambda: collections.defaultdict(int)
    )

    def record_failure(self, auth_method: AuthMethod, from_copy: bool):
        if from_copy and self.keep_score:
            self.scores[auth_method.name] += 1
        elif not from_copy:
            raise RuntimeError("AuthMethodList cannot keep score directly")


class AuthMethodList:
    """A global instance is established with all configured Authentication Methods in the
    order they were configured.

    copy() delivers a copy with the list sorted.  One copy is made per device.

    On the copies of the instance:

    next() is called when a password fails
    next_protocol() is called when the connection fails or the device fails discovery
        and excludes all other credentials sharing the same protocol

    Both return an AuthMethod() instance

    These methods result in failure() being called for the AuthMethod instance.  If ranking
    is enabled, then this decrements its score, resulting in the list being ordered differently
    for subsequent devices.

    """

    def __init__(
        self,
        keep_score: bool = False,
        ssh: bool = True,
        api: bool = True,
        telnet: bool = False,
        authlist: list = None,
        scorekeeper: ScoreKeeper = None,
    ):
        # These are setup for the original
        if not isinstance(keep_score, bool):
            raise ValueError("keep_score must be boolean")

        if not isinstance(ssh, bool):
            raise ValueError("ssh must be boolean")

        if not isinstance(telnet, bool):
            raise ValueError("telnet must be boolean")

        if not isinstance(api, bool):
            raise ValueError("api must be boolean")

        self.keep_score = keep_score
        self.ssh = ssh
        self.telnet = telnet
        self.api = api
        if authlist is None:
            self.authlist = []
            self.scorekeeper = ScoreKeeper(self.keep_score)
            self._copy = False
        else:
            self.authlist = authlist
            self.scorekeeper = scorekeeper
            self._copy = True

        # These are setup for copies to use
        self._on_deck: AuthMethod = None
        self._on_deck_retries = 0
        self._failed_protocols = []

    def __repr__(self):
        return f"{self.__class__.__name__}(list={repr(self.authlist)})"

    def load_authentication_methods(self, auth_methods: dict):
        username_protos = {
            constant.Proto.API: self.api,
            constant.Proto.SSH: self.ssh,
            constant.Proto.TELNET: self.telnet,
        }

        enabled = {p: e for p, e in username_protos.items() if e}
        index = 0
        for authname, authinfo in auth_methods.items():
            match authinfo:
                case {"username": str()}:
                    for proto in enabled:
                        self.append(AuthMethod(authname, index, proto, **authinfo))
                        index += 1
                case {"community": str()}:
                    self.append(
                        AuthMethod(authname, index, constant.Proto.SNMPv2c, **authinfo)
                    )
                    index += 1
                case {"snmpuser": str()}:
                    self.append(
                        AuthMethod(authname, index, constant.Proto.SNMPv3, **authinfo)
                    )
                    index += 1
                case _:
                    raise ValueError("Invalid protocol")

    def append(self, item):
        if not isinstance(item, AuthMethod):
            logging.error(
                "Object of type %s is invalid for %s",
                type(item),
                type(self).__name__,
            )
        else:
            self.authlist.append(item)

    def extend(self, items):
        assert isinstance(items, typing.Iterable)
        for item in items:
            self.append(item)

    def copy(self):
        if self._copy:
            raise RuntimeError(
                f"{type(self).__name__}.copy() can only be called on original",
            )
        result = type(self)(
            keep_score=self.keep_score,
            authlist=sorted(
                self.authlist,
                key=lambda a: a.index + self.scorekeeper.scores[a.name],
                reverse=True,
            ),
            scorekeeper=self.scorekeeper,
        )

        return result

    def next(self, authentication_failure: bool = False) -> AuthMethod | None:

        if not self._copy:
            raise RuntimeError(
                f"{type(self).__name__}.next() cannot" " be called on the original",
            )

        if self._on_deck:
            self.scorekeeper.record_failure(self._on_deck, self._copy)
        elif authentication_failure:
            raise RuntimeError(
                "Authentication failure cannot occur before any credentials have been tried"
            )

        if (
            self._on_deck
            and not authentication_failure
            and self._on_deck_retries >= self._on_deck.retries
        ):
            self._failed_protocols.append(self._on_deck.protoport)

        if self._on_deck and self._on_deck_retries < self._on_deck.retries:
            self._on_deck_retries += 1
            return self._on_deck

        self.authlist = [
            auth
            for auth in self.authlist
            if auth.protoport not in self._failed_protocols
        ]

        if not self.authlist:
            return None

        self._on_deck = self.authlist.pop()
        self._on_deck_retries = 0
        return self._on_deck
