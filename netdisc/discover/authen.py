import dataclasses
import typing
import collections
import logging


from netdisc.tools import helpers
from netdisc.base import constant

EXCLUDE_KEYS = ["index", "name", "proto"]


@dataclasses.dataclass
class AuthMethod:
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

    @property
    def protoport(self):
        return str(self.proto) + str(self.port)

    def kwargs(self):
        return {
            k: v
            for k, v in dataclasses.asdict(self).items()
            if v and k not in EXCLUDE_KEYS
        }


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

    def __init__(self, keep_score: bool, _list: list = None):
        # These are setup for the original
        self.keep_score = keep_score
        self._list = []
        self._copy = False
        if _list:
            self._list = _list
            self._copy = True
        self._scores = collections.defaultdict(int)

        # These are setup for copies to use
        self._on_deck: AuthMethod = None
        self._on_deck_retries = 0
        self._failed_protocols = []

    def __repr__(self):
        return f"{self.__class__.__name__}(list={repr(self._list)})"

    def _record_failure(self, auth_item: AuthMethod) -> None:
        logging.info("Recording failure")
        if self.keep_score:
            self._scores[auth_item.name] += 1

    def append(self, item):
        if not isinstance(item, AuthMethod):
            logging.error(
                f"Object of type {type(item)} is"
                f" invalid for {self.__class__.__name__}",
            )
        else:
            self._list.append(item)

    def extend(self, items):
        assert isinstance(items, typing.Iterable)
        for item in items:
            self.append(item)

    def copy(self):
        if self._copy:
            raise RuntimeError(
                f"{self.__class__.__name__}.copy() cannot" " be called on the original",
            )
        result = self.__class__(
            self.keep_score,
            _list=sorted(
                self._list,
                key=lambda a: a.index + self._scores[a.name],
                reverse=True,
            ),
        )
        result._record_failure = self._record_failure
        return result

    def next(self) -> AuthMethod | None:
        """Returns an AuthItem when one is available.

        The same one is delivered multiple times if retries are enabled

        Returns
        -------
        AuthItem | None
            None when the list is exhausted

        Raises
        ------
        RuntimeError
            _description_
        """
        if not self._copy:
            raise RuntimeError(
                f"{self.__class__.__name__}.next() cannot" " be called on the original",
            )

        if self._on_deck:
            self._record_failure(self._on_deck)

        if self._on_deck and self._on_deck_retries < self._on_deck.retries:
            self._on_deck_retries += 1
            return self._on_deck

        self._list = [
            auth for auth in self._list if auth.protoport not in self._failed_protocols
        ]

        if not self._list:
            return

        self._on_deck = self._list.pop()
        self._on_deck_retries = 0
        return self._on_deck

    def next_protocol(self) -> AuthMethod:
        """Used to request the next token when a protocol failure has occured.

        If connections to telnet are failing, then other usernames and passwords for
        telnet will be excluded

        Returns
        -------
        AuthItem
            Authentication Item

        Raises
        ------
        RuntimeError
            next_protocol cannot be called unless AuthItem is on deck
        """
        if not self._on_deck:
            raise RuntimeError(
                f"{self.__class__.__name__}.next_protocol"
                " cannot be called unless AuthItem is on deck",
            )
        if self._on_deck_retries >= self._retries:
            self._failed_protocols.append(self._on_deck.protoport)
        return self.next()
