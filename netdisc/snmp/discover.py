from netdisc.base import device
from netdisc.snmp import snmpbase
from snmp import engine, cisco


from netdisc.base import constant




def discover(engine: engine.SNMPEngine, flags: constant.Discovery) -> device.Device:
    return device.Device()



heh = discover(engine.SNMPEngine(), constant.Discovery.DEVICE_INFO)




