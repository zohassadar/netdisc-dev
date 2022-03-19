import dataclasses
import datetime
import enum
import functools
import logging
import os
import pathlib
import re
import typing

import pysnmp.smi.builder
import pysnmp.smi.compiler
import pysnmp.smi.rfc1902
import pysnmp.smi.view
from netdisc.snmp import pymibs, snmpbase

MIBSOURCE = str(pathlib.Path(pymibs.__file__).parent)

if os.name == "nt":
    MIBSOURCE = f"file://{MIBSOURCE}"

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class FlagFunctionMapper(dict):
    def register_flag(self, flag: enum.Flag) -> typing.Callable:
        """Decorator to easily associate methods to a flag"""

        def wrapper(func: typing.Callable) -> typing.Callable:
            logger.debug("Flag %s registered to %s", flag, func)
            self[flag] = func
            return func

        return wrapper


FLAG_MAP = FlagFunctionMapper()


@dataclasses.dataclass
class MIBHelper:
    mib_source: str = MIBSOURCE
    flags: snmpbase.MIBXlate = snmpbase.MIBXlate.NONE

    def __post_init__(self):
        logger.debug("Establishing mib_builder")
        self.mib_builder = pysnmp.smi.builder.MibBuilder()
        logger.debug("Establishing mib_view")
        self.mib_view = pysnmp.smi.view.MibViewController(self.mib_builder)
        logger.debug("Adding MIB Compiler")
        pysnmp.smi.compiler.addMibCompiler(self.mib_builder)
        logger.debug("Adding MIB Sources")
        self.mib_builder.addMibSources(pysnmp.smi.builder.DirMibSource(self.mib_source))
        self._mibs_loaded = set()
        self._lookups_loaded = set()

    def load_mib(self, binding: snmpbase.VarBindBase):
        if binding.MIB in self._mibs_loaded:
            return
        mib = getattr(binding, "MIB", None)
        if not mib:
            raise ValueError(f"{type(binding)} missing MIB attribute")
        try:
            self.mib_builder.loadModule(mib)
        except Exception as exc:
            # Iterate through all returned exceptions and report on the original
            args, cause, exc = exc.cause
            while True:
                reason = cause
                args, cause, exc = cause.cause
                if cause is None:
                    logging.error(f"Unable to load mib %s: %s", mib, reason)
                    break
        self._mibs_loaded.add(binding.MIB)

    def load_lookup_mibs(self, lookup_mibs: tuple):
        for lookup in lookup_mibs:
            if lookup in self._lookups_loaded:
                continue
            self._lookups_loaded.add(lookup)
            self.mib_builder.loadModule(lookup)

    @functools.singledispatchmethod
    def get_value_from_oid(self, _):
        raise NotImplementedError

    @get_value_from_oid.register
    def _(self, oid: tuple):
        oid_raw, full_node, suffix = self.mib_view.getNodeNameByOid(oid)
        return full_node[-1]

    @get_value_from_oid.register
    def _(self, oid: str):
        oid_tuple = tuple([int(i) for i in oid.split(".") if i])
        return self.get_value_from_oid(oid_tuple)

    @functools.singledispatchmethod
    def convert_binding_fields(self, binding: typing.Any):
        raise NotImplementedError

    @convert_binding_fields.register
    def _(self, binding_list: dict):
        for value in binding_list.values():
            self.convert_binding_fields(value)

    @convert_binding_fields.register
    def _(self, binding: snmpbase.VarBindBase):
        if binding._converted:
            print("convert being skipped")
            return
        print("convert being called")
        logger.debug(
            "%s Current flags: %s",
            type(binding).__name__,
            self.flags,
        )
        logger.debug(
            "%s fields being converted",
            type(binding).__name__,
        )
        for field in dataclasses.fields(binding):
            xlate = field.metadata.get(snmpbase.METADATA_FLAG_KEY)
            if not xlate:
                continue
            if not xlate in self.flags:
                continue
            logger.debug(
                "%s field %s is a type %s",
                type(binding).__name__,
                field.name,
                type(xlate).__name__,
            )
            FLAG_MAP[xlate](self, binding, field)
        binding._converted = True


@FLAG_MAP.register_flag(snmpbase.MIBXlate.LOCAL_ENUM)
def local_enum_translation(
    helper: MIBHelper,
    binding: snmpbase.VarBindBase,
    field: dataclasses.field,
):
    value = getattr(binding, field.name)
    if not isinstance(value, int):
        logger.debug(
            "%s.%s - Skipping.  Not an integer",
            type(binding).__name__,
            field.name,
        )
        return
    enumeration = field.metadata.get(snmpbase.METADATA_LOOKUP_INFO)

    enum_result = enumeration(value)
    setattr(binding, field.name, enum_result)


UNDESIRED_FORMAT = re.compile(r"0x[A-F0-9]{12}", re.I).match
NOTPRINTABLE = re.compile(r"0x[A-F0-9]{12}", re.I).match


@FLAG_MAP.register_flag(snmpbase.MIBXlate.MAC)
def mac_from_bytes(
    helper: MIBHelper,
    binding: snmpbase.VarBindBase,
    field: dataclasses.field,
):
    value = getattr(binding, field.name)
    if value is None:
        logger.debug("skipping due to NoneType")
        return
    if not isinstance(value, str):
        logger.debug("skipping due to not string")
        return
    if len(value) == 6:
        converted = ":".join(f"{ord(c):02x}" for c in value)
    elif UNDESIRED_FORMAT(value):
        converted = (
            f"{value[2:4]}"
            f":{value[4:6]}"
            f":{value[6:8]}"
            f":{value[8:10]}"
            f":{value[10:12]}"
            f":{value[12:14]}"
        )
    else:
        logger.debug("Did not match format: %s", value)
        return
    logger.info("Converted %s to %s", value, converted)
    setattr(binding, field.name, converted)


@FLAG_MAP.register_flag(snmpbase.MIBXlate.IP)
def ip_from_bytes(
    helper: MIBHelper,
    binding: snmpbase.VarBindBase,
    field: dataclasses.field,
):
    return


@FLAG_MAP.register_flag(snmpbase.MIBXlate.OID)
def str_from_oid(
    helper: MIBHelper,
    binding: snmpbase.VarBindBase,
    field: dataclasses.field,
):
    oid = getattr(binding, field.name)
    lookup_mibs = field.metadata.get(snmpbase.METADATA_LOOKUP_INFO)
    helper.load_lookup_mibs(lookup_mibs)
    xlated = helper.get_value_from_oid(oid)
    setattr(binding, field.name, xlated)


@FLAG_MAP.register_flag(snmpbase.MIBXlate.NAMED_VALUE)
def lookup_named_value(
    helper: MIBHelper,
    binding: snmpbase.VarBindBase,
    field: dataclasses.field,
):
    value = getattr(binding, field.name)
    if not isinstance(value, int):
        logger.debug(
            "%s.%s - Skipping.  Not an integer",
            type(binding).__name__,
            field.name,
        )
    helper.load_mib(binding)
    node: dict = helper.mib_builder.mibSymbols.get(binding.MIB)
    if not node:
        logger.error("%s not found", binding.MIB)
        return
    mib_field = node.get(field.name)
    if not field:
        logger.error("%s::%s not found", binding.MIB, field.name)
        return
    syntax = mib_field.getSyntax()
    name = syntax.namedValues.getName(value)
    setattr(binding, field.name, name)


@FLAG_MAP.register_flag(snmpbase.MIBXlate.TIMETICKS)
def convert_timeticks_to_readable(
    helper: MIBHelper,
    binding: snmpbase.VarBindBase,
    field: dataclasses.field,
):
    value = getattr(binding, field.name)
    if not isinstance(value, int):
        logger.debug(
            "%s.%s - Skipping.  Not an integer",
            type(binding).__name__,
            field.name,
        )
        return
    readable = str(datetime.timedelta(seconds=value / 100))
    setattr(binding, field.name, readable)


@FLAG_MAP.register_flag(snmpbase.MIBXlate.TIMESTAMP)
def convert_timestamp_to_readable(
    helper: MIBHelper,
    binding: snmpbase.VarBindBase,
    field: dataclasses.field,
):
    value = getattr(binding, field.name)
    if not isinstance(value, int):
        logger.debug(
            "%s.%s - Skipping.  Not an integer",
            type(binding).__name__,
            field.name,
        )
        return
    readable = str(datetime.timedelta(seconds=value))
    setattr(binding, field.name, readable)


def get_bits_integer(byte_str: str) -> int:
    # as_bytes = b"".join(bytes.fromhex(f"{ord(c):02x}") for c in byte_str)
    as_bytes = bytes(byte_str, encoding="latin-1")
    as_int = int.from_bytes(as_bytes, byteorder="big")
    result = 0
    bits = len(as_bytes) * 8
    for i in range(bits):
        bit = 1 & as_int
        result = result | bit
        if i == bits - 2:
            break
        result = result << 1
        as_int = as_int >> 1
    return result


@FLAG_MAP.register_flag(snmpbase.MIBXlate.BITS)
def looked_named_value_from_bits(
    helper: MIBHelper,
    binding: snmpbase.VarBindBase,
    field: dataclasses.field,
):
    value = getattr(binding, field.name)
    if not isinstance(value, str):
        logger.debug(
            "%s.%s - Skipping.  Not a string",
            type(binding).__name__,
            field.name,
        )
        return
    as_int = get_bits_integer(value)
    setattr(binding, field.name, as_int)
    lookup_named_value(helper, binding, field)
