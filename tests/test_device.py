from netdisc.base import device
import collections

DEVICE1_NAME = "switch"
DEVICE1 = "192.168.42.254"

DEVICE2_NAME = "ap1"
DEVICE2 = "192.168.42.1"

DEVICE3_NAME = "ap2"
DEVICE3 = "192.168.42.2"

DEVICE4_NAME = "asdfadf"
DEVICE4 = "192.168.42.3"


INT1_NAME = "Fa0/1"
INT2_NAME = "Fa0/2"
INT3_NAME = "Fa0/3"
INT4_NAME = "Fa0/4"
INT_NAME = "Eth0"


switch_sysinfo = """Cisco IOS Software, C3750 Software (C3750-IPSERVICESK9-M), Version 12.2(55)SE12, RELEASE SOFTWARE (fc2)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2017 by Cisco Systems, Inc."""


ap_sysinfo = """Cisco AP Software, ap1g7-k9w8 Version: 16.12.4.31
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 2014-2015 by Cisco Systems, Inc."""


unknown_sysinfo = """alsdfl;kajkl;sdfjlk;asldkjfjlasdf"""


device1_int1 = device.Interface(
    device_ip=DEVICE1, interface_name=INT1_NAME, description="management or something"
)
device1_int2 = device.Interface(
    device_ip=DEVICE1, interface_name=INT2_NAME, description="FEED TO THE FIRST AP"
)
device1_int3 = device.Interface(
    device_ip=DEVICE1, interface_name=INT3_NAME, description="FEED TO THE SECOND AP"
)
device1_int4 = device.Interface(
    device_ip=DEVICE1, interface_name=INT3_NAME, description="Some unknown crap"
)


device1_ip = device.IP(
    device_ip=DEVICE1, interface_name=INT1_NAME, address=DEVICE1, mask_len=24
)

device1_nbr1 = device.Neighbor(
    device_ip=DEVICE1,
    interface_name=INT2_NAME,
    hostname=DEVICE2_NAME,
    interface=INT_NAME,
    ip=DEVICE2,
    sysinfo=ap_sysinfo,
)
device1_nbr2 = device.Neighbor(
    device_ip=DEVICE1,
    interface_name=INT3_NAME,
    hostname=DEVICE3_NAME,
    interface=INT_NAME,
    ip=DEVICE3,
    sysinfo=ap_sysinfo,
)
device1_nbr3 = device.Neighbor(
    device_ip=DEVICE1,
    interface_name=INT4_NAME,
    hostname=DEVICE4_NAME,
    interface=INT_NAME,
    ip=DEVICE4,
    sysinfo=unknown_sysinfo,
)


device1 = device.Device(
    device_ip=DEVICE1,
    hostname=DEVICE1_NAME,
    sysinfo=switch_sysinfo,
    interfaces=[device1_int1, device1_int2, device1_int3, device1_int4],
    ip_addresses=[device1_ip],
    neighbors=[device1_nbr1, device1_nbr2, device1_nbr3],
)

device2 = device.Device(device_ip=DEVICE2, hostname=DEVICE2_NAME, sysinfo=ap_sysinfo)
device3 = device.Device(device_ip=DEVICE3, hostname=DEVICE3_NAME, sysinfo=ap_sysinfo)
device4 = device.Device(device_ip=DEVICE4, failed="Unable to get into this damn thing")


mapper = dict()
mapper[DEVICE1] = device1
mapper[DEVICE2] = device2
mapper[DEVICE3] = device3
mapper[DEVICE4] = device4
