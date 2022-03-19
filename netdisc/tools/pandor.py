import abc
import dataclasses
import ipaddress
import logging
import typing

import regex


logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

# logger.setLevel(logging.DEBUG)
# HANDLER = logging.StreamHandler()
# HANDLER.setLevel(logging.DEBUG)
# logger.addHandler(HANDLER)


class FilterAbstract(abc.ABC):
    @abc.abstractmethod
    def filter(self, obj):
        raise NotImplementedError("Base Method")


@dataclasses.dataclass
class AttrFilter(FilterAbstract):
    attr: str = None
    NOT_FOUND = object()

    def filter(self, obj):
        element = self.retrieve_attribute(obj)
        return bool(element)

    def retrieve_attribute(self, obj):
        if not self.attr:
            return obj
        element = getattr(obj, self.attr, self.NOT_FOUND)
        if element is self.NOT_FOUND:
            raise ValueError(f'Attribute "{self.attr}" not found in {obj!r}')
        return element


@dataclasses.dataclass
class AllowAll(AttrFilter):
    def filter(self, obj):
        return True


@dataclasses.dataclass
class DiscardAll(AttrFilter):
    def filter(self, obj):
        return False


@dataclasses.dataclass
class MatchBoth(FilterAbstract):
    left: AttrFilter = AllowAll()
    right: AttrFilter = AllowAll()

    def filter(self, obj: typing.Any) -> bool:
        return bool(self.left.filter(obj) and self.right.filter(obj))


@dataclasses.dataclass
class MatchEither(FilterAbstract):
    left: AttrFilter = AllowAll()
    right: AttrFilter = AllowAll()

    def filter(self, obj: typing.Any) -> bool:
        return bool(self.left.filter(obj) or self.right.filter(obj))


@dataclasses.dataclass
class InNetwork(AttrFilter):
    network: str = ipaddress.IPv4Network("0.0.0.0/0")
    RFC1918_SEARCH = regex.compile(r"rfc1918", regex.I)
    RFC10 = ipaddress.IPv4Network("10.0.0.0/8")
    RFC172 = ipaddress.IPv4Network("172.16.0.0/12")
    RFC192 = ipaddress.IPv4Network("192.168.0.0/16")

    def __post_init__(self):
        self._rfc1918 = False
        if self.RFC1918_SEARCH.search(self.network):
            logger.debug("rfc1918 mode enabled")
            self._rfc1918 = True
            return
        self._network = ipaddress.IPv4Network(self.network)

    def filter(self, obj):
        logger.debug("%s received %s to filter", repr(self), repr(obj))
        if self._rfc1918:
            logger.debug("rfc1918 mode is enabled")
            return self.rfc1918(obj)
        element = self.retrieve_attribute(obj)
        return ipaddress.IPv4Address(element) in self._network

    def rfc1918(self, obj):
        element = self.retrieve_attribute(obj)
        ip_obj = ipaddress.IPv4Address(element)
        if ip_obj in self.RFC10:
            return True
        if ip_obj in self.RFC172:
            return True
        if ip_obj in self.RFC192:
            return True
        return False


@dataclasses.dataclass
class NotInNetwork(InNetwork):
    def filter(self, obj):
        return not super().filter(obj)


@dataclasses.dataclass
class StrFilterBase(AttrFilter):
    value: str = ""


@dataclasses.dataclass
class Regex(StrFilterBase):
    def __post_init__(self):
        self._regex = regex.compile(self.value, regex.I)

    def filter(self, obj):
        element = self.retrieve_attribute(obj)
        logger.debug("%s received %s to filter", repr(self), repr(element))
        return bool(self._regex.search(element))


@dataclasses.dataclass
class NotRegex(Regex):
    def filter(self, obj):
        return not super().filter(obj)


@dataclasses.dataclass
class IsExactly(StrFilterBase):
    def filter(self, obj):
        element = self.retrieve_attribute(obj)
        logger.debug("%s received %s to filter", repr(self), repr(element))
        return element == self.value


@dataclasses.dataclass
class NotIsExactly(IsExactly):
    def filter(self, obj):
        return not super().filter(obj)


@dataclasses.dataclass
class ContainsText(StrFilterBase):
    def filter(self, obj):
        element = self.retrieve_attribute(obj)
        logger.debug("%s received %s to filter", repr(self), repr(element))
        return self.value in element


@dataclasses.dataclass
class NotContainsText(ContainsText):
    def filter(self, obj):
        return not super().filter(obj)


def StrAttrFilterFactory(
    attr: str,
    negate: str,
    operator: str,
    str_value: str,
) -> StrFilterBase:
    match negate, operator:
        case None, "=":
            return IsExactly(
                attr=attr,
                value=str_value,
            )
        case "!", "=":
            return NotIsExactly(
                attr=attr,
                value=str_value,
            )
        case None, ":":
            return ContainsText(
                attr=attr,
                value=str_value,
            )
        case "!", ":":
            return NotContainsText(
                attr=attr,
                value=str_value,
            )
        case None, "~":
            return Regex(
                attr=attr,
                value=str_value,
            )
        case "!", "~":
            return NotRegex(
                attr=attr,
                value=str_value,
            )
    raise ValueError(f"StrFilter error: {attr=} {negate=} {operator=} {str_value=}")


def NetworkAttrFilterFactory(
    attr: str,
    negate: str,
    operator: str,
    network: str,
) -> AttrFilter:
    match negate, operator:
        case "not", "in":
            return NotInNetwork(
                attr=attr,
                network=network,
            )
        case None, "in":
            return InNetwork(
                attr=attr,
                network=network,
            )
    raise ValueError(f"NetworkFilter error: {attr=} {negate=} {operator=} {network=}")


@dataclasses.dataclass
class ExpressionParser:
    expression: str

    # Everything we're looking for
    NEGATE = "negate"
    ATTRIBUTE = "attribute"
    OPERATOR = "operator"
    NETWORK = "network"
    STR_VALUE = "str_value"
    GROUP = "group"
    AND = "and"
    OR = "or"
    REMAINING = "remaining"

    # This makes the crap below much easier to read
    ESC_SINGLE = r"\'"
    ESC_DOUBLE = r"\""
    SINGLE = "'"
    DOUBLE = '"'

    """
    Look for the desired attribute.  It should start with a letter or undescore and contain
    only letters, numbers and underscores after
    """
    ATTR_REGEX = rf"^\s*(?P<{ATTRIBUTE}>[a-z_]\w+)"

    """
    Network operators: "in" or "not in"
    """
    NETWORK_OPERATOR = rf"\s*(?:\b(?P<{NEGATE}>not))?\s+(?P<{OPERATOR}>in\b)"
    """
    The pattern can match invalid IPs, but the ipaddress module will verify
    """

    ROUGH_NETWORK = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}"
    NETWORK_REGEX = rf"\s*\b(?P<{NETWORK}>(?:rfc1918|{ROUGH_NETWORK}))\b"

    """
    String operators:   ":", "!:", "=", "!=", "~", or "!~"
    """
    STR_OPERATOR = rf"\s*(?P<{NEGATE}>!)?(?P<{OPERATOR}>[:~=])"

    """
    The string value should be quoted, in either kind of quotes
    """
    SINGLE_QUOTED_VALUE_REGEX = (
        rf"\s*{SINGLE}(?P<{STR_VALUE}>(?:\{ESC_SINGLE}|[^{SINGLE}])+){SINGLE}"
    )
    DOUBLE_QUOTED_VALUE_REGEX = (
        rf"\s*{DOUBLE}(?P<{STR_VALUE}>(?:\{ESC_DOUBLE}|[^{DOUBLE}])+){DOUBLE}"
    )

    """
    Look for anything parenthesized
    """
    PARENTHESIZED_GROUP_REGEX = rf"^\s*(?P<{GROUP}>\((?:(?1)|[^()])*\))"

    """
    If anything remains, the rest of the expression can be evaluated 
    as "and <remaining>" or "or <remaining>"
    """
    REMAINING_REGEX = (
        rf"\s*(?:\s+(?:(?P<{AND}>and)|(?P<{OR}>or))\s+(?P<{REMAINING}>.+))?\s*$"
    )

    """
    Build and compile the patterns
    """
    STR_SINGLE_SEARCH = regex.compile(
        "".join(
            (
                ATTR_REGEX,
                STR_OPERATOR,
                SINGLE_QUOTED_VALUE_REGEX,
                REMAINING_REGEX,
            )
        ),
        regex.IGNORECASE | regex.DOTALL,
    )

    STR_DOUBLE_SEARCH = regex.compile(
        "".join(
            (
                ATTR_REGEX,
                STR_OPERATOR,
                DOUBLE_QUOTED_VALUE_REGEX,
                REMAINING_REGEX,
            )
        ),
        regex.IGNORECASE | regex.DOTALL,
    )

    NETWORK_SEARCH = regex.compile(
        "".join(
            (
                ATTR_REGEX,
                NETWORK_OPERATOR,
                NETWORK_REGEX,
                REMAINING_REGEX,
            )
        ),
        regex.IGNORECASE | regex.DOTALL,
    )

    GROUP_SEARCH = regex.compile(
        "".join(
            (
                PARENTHESIZED_GROUP_REGEX,
                REMAINING_REGEX,
            )
        ),
        regex.IGNORECASE | regex.DOTALL,
    )

    def __post_init__(self):
        self.result = None
        self.attr = None
        self.negate = None
        self.operator = None
        self.str_value = None
        self.network = None
        self.group = None
        self.and_ = None
        self.or_ = None
        self.remaining = None

        _found = False
        print("POST INIT!!")
        logger.debug("%s", self.GROUP_SEARCH.pattern)
        logger.debug("%s", self.STR_SINGLE_SEARCH.pattern)
        logger.debug("%s", self.STR_DOUBLE_SEARCH.pattern)
        logger.debug("%s", self.NETWORK_SEARCH.pattern)
        if not _found and (
            search_network := self.NETWORK_SEARCH.search(self.expression)
        ):
            logger.debug("Found: %s", self.NETWORK_SEARCH.pattern)
            _found = True
            self.result = search_network
            self.negate = self.result.group(self.NEGATE)
            self.operator = self.result.group(self.OPERATOR)
            self.attr = search_network.group(self.ATTRIBUTE)
            self.network = search_network.group(self.NETWORK)

        if not _found and (
            search_single := self.STR_SINGLE_SEARCH.search(self.expression)
        ):
            logger.debug("Found: %s", self.STR_SINGLE_SEARCH.pattern)
            _found = True
            self.result = search_single
            self.negate = self.result.group(self.NEGATE)
            self.operator = self.result.group(self.OPERATOR)
            self.attr = search_single.group(self.ATTRIBUTE)
            self.str_value = search_single.group(self.STR_VALUE).replace(
                self.ESC_SINGLE,
                self.SINGLE,
            )

        if not _found and (
            search_double := self.STR_DOUBLE_SEARCH.search(self.expression)
        ):
            logger.debug("Found: %s", self.STR_DOUBLE_SEARCH.pattern)
            _found = True
            self.result = search_double
            self.negate = self.result.group(self.NEGATE)
            self.operator = self.result.group(self.OPERATOR)
            self.attr = search_double.group(self.ATTRIBUTE)
            self.str_value = search_double.group(self.STR_VALUE).replace(
                self.ESC_DOUBLE,
                self.DOUBLE,
            )

        if not _found and (search_group := self.GROUP_SEARCH.search(self.expression)):
            logger.debug("Found: %s", self.GROUP_SEARCH.pattern)
            _found = True
            self.result = search_group
            # If the group pattern matched, the first and last characters are parentheses
            # This strips them off
            self.group = search_group.group(self.GROUP)[1:-1]

        if not _found:
            raise ValueError(f"Unable to parse input: {self.expression}")

        logger.debug("Found: %s", self.result)
        self.and_ = self.result.group(self.AND)
        self.or_ = self.result.group(self.OR)
        self.remaining = self.result.group(self.REMAINING)


def AttrFilterForkFactory(expression: str) -> AttrFilter:
    if not expression.strip():
        return AllowAll()
    logger.debug("AttrFilterForkFactory received: %s", expression)
    parsed_expression = ExpressionParser(expression)

    if parsed_expression.network:
        left = NetworkAttrFilterFactory(
            attr=parsed_expression.attr,
            negate=parsed_expression.negate,
            operator=parsed_expression.operator,
            network=parsed_expression.network,
        )
    elif parsed_expression.str_value:
        left = StrAttrFilterFactory(
            attr=parsed_expression.attr,
            negate=parsed_expression.negate,
            operator=parsed_expression.operator,
            str_value=parsed_expression.str_value,
        )
    elif parsed_expression.group:
        left = AttrFilterForkFactory(
            expression=parsed_expression.group,
        )
    else:
        raise ValueError(f"AttrFilterForkFactory error: {expression}")

    if not parsed_expression.remaining:
        return left

    right = AttrFilterForkFactory(parsed_expression.remaining)

    if parsed_expression.or_:
        return MatchEither(
            left=left,
            right=right,
        )
    elif parsed_expression.and_:
        return MatchBoth(
            left=left,
            right=right,
        )
