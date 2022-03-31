""" Definitions of base classes
Copyright 2022 Richard Dodson
"""
import abc
from netdisc.base import device_base


class Gatherer(abc.ABC):
    @abc.abstractmethod
    def get_device(self) -> dict[str, str | int | bool]:
        ...

    @abc.abstractmethod
    def get_interfaces(self) -> list[dict[str, str | int | bool]]:
        ...

    @abc.abstractmethod
    def get_neighbors(self) -> list[dict[str, str | int | bool]]:
        ...

    @abc.abstractmethod
    def get_ip_addresses(self) -> list[dict[str, str | int | bool]]:
        ...

    @abc.abstractmethod
    def get_ipv6_addresses(self) -> list[dict[str, str | int | bool]]:
        ...

    @abc.abstractmethod
    def get_routes(self) -> list[dict[str, str | int | bool]]:
        ...

    @abc.abstractmethod
    def get_macs(self) -> list[dict[str, str | int | bool]]:
        ...

    @abc.abstractmethod
    def get_arps(self) -> list[dict[str, str | int | bool]]:
        ...

    @abc.abstractmethod
    def get_vlans(self) -> list[dict[str, str | int | bool]]:
        ...

    @abc.abstractmethod
    def get_vrfs(self) -> list[dict[str, str | int | bool]]:
        ...


class TopologyBase(abc.ABC):
    """Interact with the discovered topology"""

    @abc.abstractmethod
    def update_device(
        self,
        device: device_base.Device,
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def __enter__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def __exit__(self, *exc):
        raise NotImplementedError


class OutputBase(abc.ABC):
    """Output methods"""

    @abc.abstractmethod
    def dump(
        self,
        *args,
        **kwargs,
    ):
        raise NotImplementedError

    @abc.abstractmethod
    def dump_list(
        self,
        *args,
        **kwargs,
    ):
        raise NotImplementedError


class AuthMethodBase(abc.ABC):
    """Authentication methods"""

    @abc.abstractmethod
    def extend(self):
        raise NotImplementedError

    @abc.abstractmethod
    def append(self):
        raise NotImplementedError

    @abc.abstractmethod
    def copy(self):
        raise NotImplementedError

    @abc.abstractmethod
    def next(self):
        raise NotImplementedError

    @abc.abstractmethod
    def next_protocol(self):
        raise NotImplementedError
