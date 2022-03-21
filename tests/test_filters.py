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


if "__main__" in __name__:
    unittest.main()
