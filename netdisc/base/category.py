import dataclasses
import enum
import functools
import pathlib

import regex
import yaml
import yaml.scanner


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


class NetDiscCategoryError(ValueError):
    ...


DEFAULT_CATEGORIES_PATH = pathlib.Path.joinpath(
    pathlib.Path(__file__).parent, pathlib.Path("categories.yaml")
)


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


@dataclasses.dataclass
class Categorizer:
    file: str | pathlib.Path = None
    default = DEFAULT_CATEGORIES_PATH
    overwrite: bool = False

    def __post_init__(self):

        self._categories: dict[str, dict] = {}
        self._loaded_categories: dict[str, DeviceCategory] = {}
        for file in (self.file, self.default):
            if not file:
                continue
            try:
                with open(DEFAULT_CATEGORIES_PATH) as f:
                    contents = f.read()
            except FileNotFoundError as exc:
                raise NetDiscCategoryError(f"Invalid filename: {file}") from exc
            try:
                loaded = yaml.safe_load(contents)
            except yaml.scanner.ScannerError as exc:
                raise NetDiscCategoryError(f"Invalid YAML in file: {file}") from exc

            self.load_category_info(loaded)
            if self.overwrite:
                break

    def load_category_info(self, loaded_yaml):

        for name, info in loaded_yaml.items():
            if name not in self.all_categories:
                raise NetDiscCategoryError(f"Category {name} is not defined")
            category = self.flags_by_name[name]
            device_category = self._loaded_categories.setdefault(
                name, DeviceCategory(category=category)
            )
            vars(device_category).update(info)

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
        if device_category:
            return device_category
        return self._loaded_categories.setdefault(
            Category.UNKNOWN.name,
            DeviceCategory(category=Category.UNKNOWN),
        )

    def category_by_netmiko(self, netmiko_type: str) -> DeviceCategory:
        device_category = self.categories_by_netmiko.get(netmiko_type)
        if device_category:
            return device_category
        return self._loaded_categories.setdefault(
            Category.UNKNOWN.name,
            DeviceCategory(category=Category.UNKNOWN),
        )

    def category_by_sysinfo(self, sysinfo: str) -> DeviceCategory:
        for category in self._loaded_categories.values():
            if category.sysinfo_compiled.search(sysinfo):
                return category
        return self._loaded_categories.setdefault(
            Category.UNKNOWN.name,
            DeviceCategory(category=Category.UNKNOWN),
        )
