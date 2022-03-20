from netdisc.base import constant, device
from netdisc.snmp import engine


def discover(eng: engine.SNMPEngine, flags: constant.Discovery) -> device.Device:
    print(eng)
    print(flags)
    return device.Device()
