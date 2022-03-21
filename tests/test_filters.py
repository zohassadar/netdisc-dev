import dataclasses
import unittest

import pytest
from netdisc.tools import pandor


@dataclasses.dataclass
class Included:
    ip_address: str = "10.20.30.40"
    short: str = "included"
    field: str = "abc 123 this is the included field"


@dataclasses.dataclass
class Excluded:
    ip_address: str = "40.30.20.10"
    short: str = "excluded"
    field: str = "zyx 321 this is the excluded field"


@dataclasses.dataclass
class ObjectWithIP:
    ip_address: str


included = Included()
excluded = Excluded()


stupid_tree_1 = """
    (ip_address = "10.20.30.40" and ip_address != "potato"

    and

    (field !~ '^(?=zyx 321)' and field : "included") )

    and

    (ip_address in rfc1918 and ip_address in 10.20.30.0/24)

    and

    ip_address not in 40.0.0.0/8

"""


stupid_tree_2 = """

    ((ip_address = "potato" and ip_address in rfc1918)  and (field : 'tomato'))
    or

   ( (ip_address = "10.20.30.40" and ip_address != "potato"

    and

    (field !~ '^(?=zyx 321)' and field : "included") )

    and

    (ip_address in rfc1918 and ip_address in 10.20.30.0/24)

    and

    ip_address not in 40.0.0.0/8)

"""


variations = (
    pytest.param(pandor.MatchBoth, stupid_tree_1, id="stupid tree 1"),
    pytest.param(pandor.MatchEither, stupid_tree_2, id="stupid tree 2"),
    pytest.param(
        pandor.ContainsText, 'field      :     "123"', id="contains_with_spaces"
    ),
    pytest.param(pandor.ContainsText, 'field:"123"', id="contains_with_no_spaces"),
    pytest.param(
        pandor.NotContainsText, 'field   !:    "321"', id="not_contains_with_spaces"
    ),
    pytest.param(
        pandor.NotContainsText, 'field!:"321"', id="not_contains_with_no_spaces"
    ),
    pytest.param(
        pandor.IsExactly, 'ip_address     =    "10.20.30.40"', id="exact_with_spaces"
    ),
    pytest.param(
        pandor.IsExactly, 'ip_address     =    "10.20.30.40"', id="exact_with_no_spaces"
    ),
    pytest.param(
        pandor.NotIsExactly,
        'ip_address    !=   "40.30.20.10"',
        id="not_exact_with_spaces",
    ),
    pytest.param(
        pandor.NotIsExactly, 'ip_address!="40.30.20.10"', id="not_exact_with_no_spaces"
    ),
    pytest.param(pandor.Regex, 'ip_address ~ "^10.20."', id="regex_with_spaces"),
    pytest.param(pandor.Regex, 'ip_address~"30.40$"', id="regex_with_no_spaces"),
    pytest.param(
        pandor.NotRegex, 'ip_address !~ "^40.30."', id="not_regex_with_spaces"
    ),
    pytest.param(
        pandor.NotRegex, 'ip_address!~".20.10$"', id="not_regex_with_no_spaces"
    ),
    pytest.param(
        pandor.ContainsText, "field      :     '123'", id="contains_with_spaces_single"
    ),
    pytest.param(
        pandor.ContainsText, "field:'123'", id="contains_with_no_spaces_single"
    ),
    pytest.param(
        pandor.NotContainsText,
        "field   !:    '321'",
        id="not_contains_with_spaces_single",
    ),
    pytest.param(
        pandor.NotContainsText, "field!:'321'", id="not_contains_with_no_spaces_single"
    ),
    pytest.param(
        pandor.IsExactly,
        "ip_address     =    '10.20.30.40'",
        id="exact_with_spaces_single",
    ),
    pytest.param(
        pandor.IsExactly,
        "ip_address     =    '10.20.30.40'",
        id="exact_with_no_spaces_single",
    ),
    pytest.param(
        pandor.NotIsExactly,
        "ip_address    !=   '40.30.20.10'",
        id="not_exact_with_spaces_single",
    ),
    pytest.param(
        pandor.NotIsExactly,
        "ip_address!='40.30.20.10'",
        id="not_exact_with_no_spaces_single",
    ),
    pytest.param(pandor.Regex, "ip_address ~ '^10.20.'", id="regex_with_spaces_single"),
    pytest.param(pandor.Regex, "ip_address~'30.40$'", id="regex_with_no_spaces_single"),
    pytest.param(
        pandor.NotRegex, "ip_address !~ '^40.30.'", id="not_regex_with_spaces_single"
    ),
    pytest.param(
        pandor.NotRegex, "ip_address!~'.20.10$'", id="not_regex_with_no_spaces_single"
    ),
    pytest.param(pandor.InNetwork, "ip_address in 10.0.0.0/8", id="in_network"),
    pytest.param(pandor.InNetwork, "ip_address   in rfc1918", id="in_network_rfc1918"),
    pytest.param(
        pandor.NotInNetwork, "ip_address not in 40.0.0.0/8", id="not_in_network"
    ),
)


opposite_variations = (
    pytest.param(
        pandor.NotInNetwork,
        "ip_address  not in rfc1918",
        id="not_in_network_rfc1918",
    ),
)


@pytest.mark.parametrize(
    ("expected", "pattern"),
    variations,
)
def test_the_filters(expected, pattern):
    attr_filter = pandor.AttrFilterForkFactory(pattern)
    assert isinstance(attr_filter, expected)
    assert attr_filter.filter(included)
    assert not attr_filter.filter(excluded)


@pytest.mark.parametrize(
    ("expected", "pattern"),
    opposite_variations,
)
def test_the_filters_opposite(expected, pattern):
    attr_filter = pandor.AttrFilterForkFactory(pattern)
    assert isinstance(attr_filter, expected)
    assert not attr_filter.filter(included)
    assert attr_filter.filter(excluded)


def test_invalid_filter_entirely():
    with pytest.raises(ValueError):
        pandor.AttrFilterForkFactory("asdf")


def test_blank_filter():
    assert isinstance(pandor.AttrFilterForkFactory(""), pandor.AllowAll)


def test_whitespace_filter():
    assert isinstance(pandor.AttrFilterForkFactory(" \t\n\r "), pandor.AllowAll)


def test_invalid_filter_option():
    with pytest.raises(ValueError):
        pandor.StrAttrFilterFactory("test", None, "¿", "test")


def test_invalid_filter_option_negate():
    with pytest.raises(ValueError):
        pandor.StrAttrFilterFactory("test", "!", "¿", "test")


def test_invalid_filter_option_network():
    with pytest.raises(ValueError):
        pandor.NetworkAttrFilterFactory("ip", None, "ni", "192.168.0.0/24")


def test_invalid_filter_option_negate_network():
    with pytest.raises(ValueError):
        pandor.NetworkAttrFilterFactory("ip", "not", "ni", "192.168.0.0/24")


def test_plain_attr_filter():
    filter_ = pandor.AttrFilter()
    assert filter_.filter(True)
    assert not filter_.filter(False)


def test_allow_all():
    filter_ = pandor.AllowAll()
    assert filter_.filter(True)
    assert filter_.filter(False)


def test_discard_all():
    filter_ = pandor.DiscardAll()
    assert not filter_.filter(True)
    assert not filter_.filter(False)


def test_invalid_field():
    filter_ = pandor.AttrFilter(attr="good")
    with pytest.raises(ValueError):
        filter_.filter(object())


@pytest.mark.parametrize(
    ("network", "ip_address"),
    (
        ("rfc1918", "10.0.0.0"),
        ("rfc1918", "10.255.255.255"),
        ("rfc1918", "172.16.0.0"),
        ("rfc1918", "172.31.255.255"),
        ("rfc1918", "192.168.0.0"),
        ("rfc1918", "192.168.255.255"),
        ("1.1.1.1/32", "1.1.1.1"),
        ("0.0.0.0/0", "0.0.0.0"),
        ("0.0.0.0/0", "255.255.255.255"),
        ("0.0.0.0/1", "0.0.0.0"),
        ("0.0.0.0/1", "127.255.255.255"),
        ("128.0.0.0/1", "128.0.0.0"),
        ("128.0.0.0/1", "255.255.255.255"),
    ),
)
def test_good_ip_combinations(network, ip_address):
    populated_filter = f"ip_address in {network}"
    obj = ObjectWithIP(ip_address)
    filter_ = pandor.AttrFilterForkFactory(populated_filter)
    assert filter_.filter(obj)


@pytest.mark.parametrize(
    ("network", "ip_address"),
    (
        ("rfc1918", "19.0.0.0"),
        ("rfc1918", "11.255.255.255"),
        ("rfc1918", "172.15.0.0"),
        ("rfc1918", "172.32.255.255"),
        ("rfc1918", "192.167.255.255"),
        ("rfc1918", "191.168.0.0"),
        ("1.1.1.1/32", "1.1.1.2"),
        ("0.0.0.0/1", "128.0.0.0"),
        ("128.0.0.0/1", "127.255.255.255"),
    ),
)
def test_bad_ip_combinations(network, ip_address):
    populated_filter = f"ip_address in {network}"
    obj = ObjectWithIP(ip_address)
    filter_ = pandor.AttrFilterForkFactory(populated_filter)
    assert not filter_.filter(obj)
