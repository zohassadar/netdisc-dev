import abc
import typing
from netdisc.base import device


class Accumulator(abc.ABC):
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
    @abc.abstractmethod
    def get_device(
        self,
        ip,
    ) -> device.Device:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_device(
        self,
        device: device.Device,
    ) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def update_device(
        self,
        device: device.Device,
    ) -> None:
        raise NotImplementedError


class DiscoverBase(abc.ABC):
    @abc.abstractmethod
    def __init__(
        self,
        **kwargs,
    ):
        raise NotImplementedError

    @abc.abstractmethod
    def discover(
        self,
        ip: str,
        hostname: str = None,
        sysinfo: str = None,
    ):
        raise NotImplementedError


class DeviceInteract(abc.ABC):
    @abc.abstractmethod
    def get_base(self) -> dict:
        raise NotImplementedError

    def get_vlans(self) -> typing.List[dict]:
        raise NotImplementedError

    def get_macs(self) -> typing.List[dict]:
        raise NotImplementedError

    def get_interfaces(self) -> typing.List[dict]:
        raise NotImplementedError

    def get_neighbors(self) -> typing.List[dict]:
        raise NotImplementedError

    def get_vrfs(self) -> typing.List[dict]:
        raise NotImplementedError

    def get_arps(self) -> typing.List[dict]:
        raise NotImplementedError

    def get_routes(self) -> typing.List[dict]:
        raise NotImplementedError


class FilterBase(abc.ABC):
    @abc.abstractmethod
    def filter(
        self,
        item: typing.Any,
    ) -> typing.List[typing.Any]:
        raise NotImplementedError


class QueueBase(abc.ABC):
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


class WorkerBase(abc.ABC):
    @abc.abstractmethod
    def __call__(self, task):
        raise NotImplementedError


class OutputBase(abc.ABC):
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
