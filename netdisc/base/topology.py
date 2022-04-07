import typing
import yaml
from netdisc.base import abstract, device_base
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class MemoryTopology(abstract.TopologyBase):
    def __init__(self):
        self._devices: typing.Dict[str, device_base.Device] = {}

    @property
    def total(self):
        return len(self._devices)

    @property
    def total_successful(self):
        return len([d for d in self._devices.values() if not d.failed])

    @property
    def yamlable(self):
        results = {}
        for ip, device in self._devices.items():
            results[ip] = {
                k: [dict(e) for e in v] if isinstance(v, list) else v
                for k, v in dict(device).items()
            }
        return results

    def update_device(self, device: device_base.Device):
        logger.info("Completed Device %s", device.device_ip)
        if device.device_ip:
            self._devices[device.device_ip] = device

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        with open("topology.yaml", "w+") as file:
            yaml.dump(self.yamlable, file)
