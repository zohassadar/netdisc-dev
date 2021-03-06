from netdisc.snmp import pyeng, mibhelp, snmpbase, gatherer
from netdisc.tools import helpers
import pytest
import unittest.mock
import pathlib

# test_parameterized_fixture.py
import pytest


check_debug_info = pytest.mark.skipif(
    not pyeng.PYENG_DEBUG_OUTPUT or not pathlib.Path(pyeng.PYENG_DEBUG_OUTPUT).exists,
    reason="Debug Info Unavailable",
)


def get_fake_pyeng(mib_helper, ip_address):
    print(f"get_fake_pyeng: {mib_helper=} {ip_address=}")
    py2 = pyeng.PySNMPEngine(
        mib_helper=mib_helper,
        host=ip_address,
        community="community",
    )
    dumped_retriever = helpers.SNMPEngDumpedDebug(pyeng.PYENG_DEBUG_OUTPUT, ip_address)
    py2.get = unittest.mock.Mock(side_effect=dumped_retriever.retrieve)
    py2.walk = unittest.mock.Mock(side_effect=dumped_retriever.retrieve)
    return py2


@pytest.fixture
def mib_helper_no_flags():
    print(f"mib_helper_no_flags")
    return mibhelp.MIBHelper(flags=snmpbase.MIBXlate.NONE)


@pytest.fixture
def fake_pyeng(fake_pyeng_arg, mib_helper_no_flags):
    print(f"fake_pyeng: {fake_pyeng_arg=} {mib_helper_no_flags=}")
    """Create tester object"""
    return get_fake_pyeng(mib_helper_no_flags, fake_pyeng_arg)


@check_debug_info
@pytest.mark.parametrize(
    ("fake_pyeng_arg"),
    ("172.17.0.2",),
)
def test_pyeng(fake_pyeng):
    gatherer.SNMPGeneric(fake_pyeng)


@check_debug_info
@pytest.mark.parametrize(
    ("fake_pyeng_arg"),
    ("172.17.0.2",),
)
def test_pyeng_interfaces(fake_pyeng):
    g = gatherer.SNMPGeneric(fake_pyeng)
    print(g.get_interfaces())
