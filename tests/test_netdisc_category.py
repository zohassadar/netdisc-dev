"""
python -c \
'import sys
import json
data = json.loads(sys.stdin.read())
print (
    "\n".join(
        set(
            [d.get("sysinfo", "") for d in data]
            )
        )
    )' \
< raw_json_sysinfos.json > sysinfo_examples.txt
"""
import pytest
from netdisc.base import Categorizer, Category


@pytest.mark.parametrize(
    ("sysinfo", "expected"),
    (
        pytest.param(
            "Cisco IOS Software",
            Category.CISCO_IOS,
            id=Category.CISCO_IOS.name,
        ),
        pytest.param(
            "Cisco Adaptive Security Appliance Software Version ",
            Category.CISCO_ASA,
            id=Category.CISCO_ASA.name,
        ),
        pytest.param(
            "Cisco FX-OS(tm) fxos, Software (fxos-k9-system)",
            Category.CISCO_FXOS,
            id=Category.CISCO_FXOS.name,
        ),
        pytest.param(
            "Cisco NX-OS(tm)",
            Category.CISCO_NXOS,
            id=Category.CISCO_NXOS.name,
        ),
        pytest.param(
            "Cisco IOS XR Software",
            Category.CISCO_XR,
            id=Category.CISCO_XR.name,
        ),
        pytest.param(
            "HP Comware Platform Software",
            Category.HP_COMWARE,
            id=Category.HP_COMWARE.name,
        ),
        pytest.param(
            "Arista Networks EOS version",
            Category.ARISTA_EOS,
            id=Category.ARISTA_EOS.name,
        ),
        pytest.param(
            "Avaya Inc.,",
            Category.AVAYA,
            id=Category.AVAYA.name,
        ),
        pytest.param(
            "Dell EMC Networking OS10",
            Category.DELL,
            id=Category.DELL.name,
        ),
        pytest.param(
            "Palo Alto Networks",
            Category.PALOALTO_PANOS,
            id=Category.PALOALTO_PANOS.name,
        ),
    ),
)
def test_name_by_sysinfo(sysinfo: str, expected: Category):
    categorizer = Categorizer()
    assert categorizer.category_by_sysinfo(sysinfo).category is expected


@pytest.mark.parametrize(
    ("name", "category"),
    (
        pytest.param("CISCO_IOS", Category.CISCO_IOS),
        pytest.param("CISCO_FXOS", Category.CISCO_FXOS),
        pytest.param("CISCO_ASA", Category.CISCO_ASA),
        pytest.param("CISCO_ISE", Category.CISCO_ISE),
        pytest.param("CISCO_NXOS", Category.CISCO_NXOS),
        pytest.param("CISCO_WLC", Category.CISCO_WLC),
        pytest.param("CISCO_XR", Category.CISCO_XR),
        pytest.param("ARISTA_EOS", Category.ARISTA_EOS),
        pytest.param("AVAYA", Category.AVAYA),
        pytest.param("NETGEAR", Category.NETGEAR),
        pytest.param("NIMBLE", Category.NIMBLE),
    ),
)
def test_category_by_name(name, category):
    categorizer = Categorizer()
    assert categorizer.category_by_name(name).category is category


@pytest.mark.parametrize(
    ("netmiko", "category"),
    (
        pytest.param("cisco_ios", Category.CISCO_IOS),
        pytest.param("cisco_asa", Category.CISCO_ASA),
        pytest.param("cisco_nxos", Category.CISCO_NXOS),
        pytest.param("cisco_xr", Category.CISCO_XR),
        pytest.param("arista_eos", Category.ARISTA_EOS),
    ),
)
def test_category_by_netmiko(netmiko, category):
    categorizer = Categorizer()
    assert categorizer.category_by_netmiko(netmiko).category is category


def test_category_by_netmiko_invalid():
    categorizer = Categorizer()
    assert categorizer.category_by_netmiko(netmiko).category is category
