import typing

from netdisc.base import device, abstract


class MemoryTopology(abstract.TopologyBase):
    def __init__(self):
        self._devices: typing.Dict[str, device.Device] = {}

    def get_device(self, ip) -> device.Device:
        for dev in self._devices.values():
            for ip_row in dev.ip_addresses:
                if ip_row.address == ip:
                    return dev

    def delete_device(self, dev: device.Device):
        assert hasattr(dev, "device_ip")
        if not self._devices.pop(dev.device_ip, None):
            raise RuntimeError("Unable to delete.  Device not found")

    def add_device(self, dev: device.Device):
        assert hasattr(dev, "device_ip")
        self._devices[dev.device_ip] = dev

    def update_device(self, dev: device.Device):
        assert hasattr(dev, "device_ip")
        pass
