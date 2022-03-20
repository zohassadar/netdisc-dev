import dataclasses
import enum
import functools
import pathlib

import regex
import yaml


class NetDiscCategoryError(ValueError):
    ...


CATEGORIES_FILE = "categories.yaml"
CATEGORIES = pathlib.Path.joinpath(
    pathlib.Path(__file__).parent, pathlib.Path(CATEGORIES_FILE)
)


if not CATEGORIES.exists():
    raise NetDiscCategoryError(f"Unable to open file: {CATEGORIES}")


class Category(enum.Enum):
    NOT_SET = enum.auto()
    UNKNOWN = enum.auto()
    ARISTA_EOS = enum.auto()
    CISCO_ASA = enum.auto()
    CISCO_IOS = enum.auto()
    CISCO_FXOS = enum.auto()
    CISCO_NXOS = enum.auto()
    CISCO_XR = enum.auto()
    F5_BIGIP = enum.auto()
    HP_COMWARE = enum.auto()
    HP_PROCURVE = enum.auto()
    PALOALTO_PANOS = enum.auto()
    AVAYA = enum.auto()
    DELL = enum.auto()
    LINUX = enum.auto()
    CISCO_CIMC = enum.auto()
    NIMBLE = enum.auto()
    WINDOWS_SERVER = enum.auto()
    CISCO_WLC = enum.auto()
    SONUS = enum.auto()
    NETGEAR = enum.auto()
    CISCO_ISE = enum.auto()
    AVAYA_AURA = enum.auto()


@dataclasses.dataclass(frozen=True)
class DeviceCategory:
    """Device Category data loaded from yaml
    :param:

    """

    category: Category = Category.NOT_SET
    sysinfo: str = ""
    netmiko: str = ""
    running: str = ""
    startup: str = ""
    save: str = ""

    @functools.cached_property
    def sysinfo_compiled(self) -> regex.Pattern:
        return regex.compile(self.sysinfo)


dc = DeviceCategory(sysinfo="heh")


@dataclasses.dataclass
class Categorizer:
    def __post_init__(self):
        self._categories: dict[str, dict] = {}
        self._loaded_categories: dict[str, DeviceCategory] = {}
        with open(CATEGORIES) as file:
            self._categories = yaml.safe_load(file)
        for name, info in self._categories.items():
            if name not in self.all_categories:
                raise NetDiscCategoryError(f"Category {name} is not defined")
            category = self.flags_by_name[name]
            self._loaded_categories[name] = DeviceCategory(category=category, **info)

    @functools.cached_property
    def all_categories(self) -> list[str]:
        return [cat.name for cat in list(Category) if cat is not Category.NOT_SET]

    @functools.cached_property
    def categories_by_netmiko(self) -> dict[str, DeviceCategory]:
        by_netmiko = {}
        for category in self._loaded_categories.values():
            if netmiko_type := category.netmiko:
                by_netmiko[netmiko_type] = category
        return by_netmiko

    @functools.cached_property
    def flags_by_name(self) -> dict[str, DeviceCategory]:
        by_name = {}
        for flag in Category:
            by_name[flag.name] = flag
        return by_name

    def category_by_name(self, name: str) -> DeviceCategory:
        device_category = self._loaded_categories.get(name)
        if device_category is None:
            raise NetDiscCategoryError(
                f"Category of {name} is not defined in {CATEGORIES}"
            )
        return device_category

    def category_by_netmiko(self, netmiko_type: str) -> DeviceCategory:
        device_category = self.categories_by_netmiko.get(netmiko_type)
        if device_category is None:
            raise NetDiscCategoryError(
                f"Category with netmiko type {netmiko_type} is not defined in {CATEGORIES}"
            )
        return device_category

    def category_by_sysinfo(self, sysinfo: str) -> DeviceCategory:
        for category in self._loaded_categories.values():
            if category.sysinfo_compiled.search(sysinfo):
                return category
        raise NetDiscCategoryError(
            f"Sysinfo provided doesn't match any configured category:\n{sysinfo}"
        )
