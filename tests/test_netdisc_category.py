import pytest
from netdisc.base import Categorizer, Category, DeviceCategory


categorizer = Categorizer()

# python -c 'import sys;import json; print ("\n".join(set([d.get("sysinfo", "") for d in json.loads(sys.stdin.read()) ])))' < raw_json_sysinfos.json > sysinfo_examples.txt

sysinfo_examples = ["Examples of sysinfo responses go here"]


@pytest.mark.parametrize(
    ("sysinfo"),
    [pytest.param(sysinfo, id=sysinfo[:40]) for sysinfo in sysinfo_examples],
)
def test_example_sysinfos(sysinfo: str):
    assert categorizer.category_by_sysinfo(sysinfo)


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
    assert categorizer.category_by_sysinfo(sysinfo).category is expected
