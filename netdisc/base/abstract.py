""" Definitions of base classes
Copyright 2022 Richard Dodson
"""
import abc
from netdisc.base import device


class Accumulator(abc.ABC):
    """Collect information and provide a device"""

    @abc.abstractmethod
    def base_info(self):
        raise NotImplementedError

    @abc.abstractmethod
    def interfaces(self):
        raise NotImplementedError

    @abc.abstractmethod
    def neighbors(self):
        raise NotImplementedError

    @abc.abstractmethod
    def routes(self):
        raise NotImplementedError

    @abc.abstractmethod
    def vlans(self):
        raise NotImplementedError

    @abc.abstractmethod
    def vrfs(self):
        raise NotImplementedError

    @abc.abstractmethod
    def macs(self):
        raise NotImplementedError

    @abc.abstractmethod
    def arps(self):
        raise NotImplementedError


class TopologyBase(abc.ABC):
    """Interact with the discovered topology"""

    @abc.abstractmethod
    def get_device(
        self,
        ip,
    ) -> device.Device:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_device(
        self,
        dev: device.Device,
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def update_device(
        self,
        dev: device.Device,
    ) -> None:
        raise NotImplementedError


class QueueBase(abc.ABC):
    """Queueing solution"""

    @abc.abstractmethod
    def empty(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self):
        raise NotImplementedError

    @abc.abstractmethod
    def put(self, task):
        raise NotImplementedError

    @abc.abstractmethod
    def close(self):
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
