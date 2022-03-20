import sys

from netdisc.base.category import Categorizer, Category, DeviceCategory

if not sys.version_info >= (3, 10):
    sys.exit("Minimum supported python version is 3.10")
