import unittest
from netdisc.tools import pandor
import dataclasses


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


class TestStupidTrees(unittest.TestCase):
    def test_stupid_tree_1(self):
        attr_filter = pandor.AttrFilterForkFactory(stupid_tree_1)
        self.assertIsInstance(attr_filter, pandor.MatchBoth)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))


class TestStupidTrees(unittest.TestCase):
    def test_stupid_tree_2(self):
        attr_filter = pandor.AttrFilterForkFactory(stupid_tree_2)
        self.assertIsInstance(attr_filter, pandor.MatchEither)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))


class TestStrAttrFilters(unittest.TestCase):
    def test_contains_with_spaces(self):
        filter_ = 'field      :     "123"'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.ContainsText)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_contains_with_no_spaces(self):
        filter_ = 'field:"123"'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.ContainsText)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_contains_with_spaces(self):
        filter_ = 'field   !:    "321"'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotContainsText)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_contains_with_no_spaces(self):
        filter_ = 'field!:"321"'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotContainsText)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_exact_with_spaces(self):
        filter_ = 'ip_address     =    "10.20.30.40"'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.IsExactly)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_exact_with_no_spaces(self):
        filter_ = 'ip_address     =    "10.20.30.40"'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.IsExactly)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_exact_with_spaces(self):
        filter_ = 'ip_address    !=   "40.30.20.10"'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotIsExactly)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_exact_with_no_spaces(self):
        filter_ = 'ip_address!="40.30.20.10"'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotIsExactly)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_regex_with_spaces(self):
        filter_ = 'ip_address ~ "^10.20."'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.Regex)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_regex_with_no_spaces(self):
        filter_ = 'ip_address~"30.40$"'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.Regex)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_regex_with_spaces(self):
        filter_ = 'ip_address !~ "^40.30."'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotRegex)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_regex_with_no_spaces(self):
        filter_ = 'ip_address!~".20.10$"'
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotRegex)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_contains_with_spaces_single(self):
        filter_ = "field      :     '123'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.ContainsText)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_contains_with_no_spaces_single(self):
        filter_ = "field:'123'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.ContainsText)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_contains_with_spaces_single(self):
        filter_ = "field   !:    '321'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotContainsText)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_contains_with_no_spaces_single(self):
        filter_ = "field!:'321'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotContainsText)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_exact_with_spaces_single(self):
        filter_ = "ip_address     =    '10.20.30.40'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.IsExactly)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_exact_with_no_spaces_single(self):
        filter_ = "ip_address     =    '10.20.30.40'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.IsExactly)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_exact_with_spaces_single(self):
        filter_ = "ip_address    !=   '40.30.20.10'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotIsExactly)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_exact_with_no_spaces_single(self):
        filter_ = "ip_address!='40.30.20.10'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotIsExactly)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_regex_with_spaces_single(self):
        filter_ = "ip_address ~ '^10.20.'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.Regex)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_regex_with_no_spaces_single(self):
        filter_ = "ip_address~'30.40$'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.Regex)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_regex_with_spaces_single(self):
        filter_ = "ip_address !~ '^40.30.'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotRegex)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_regex_with_no_spaces_single(self):
        filter_ = "ip_address!~'.20.10$'"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotRegex)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))


class TestNetworkAttrFilters(unittest.TestCase):
    def test_in_network(self):
        filter_ = "ip_address in 10.0.0.0/8"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.InNetwork)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_in_network_rfc1918(self):
        filter_ = "ip_address   in rfc1918"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.InNetwork)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_in_network(self):
        filter_ = "ip_address not in 40.0.0.0/8"
        attr_filter = pandor.AttrFilterForkFactory(filter_)
        self.assertIsInstance(attr_filter, pandor.NotInNetwork)
        self.assertTrue(attr_filter.filter(included))
        self.assertFalse(attr_filter.filter(excluded))

    def test_not_in_network_rfc1918(self):
        filter_ = "   ip_address          not   in rfc1918"
        attr_filter = pandor.AttrFilterForkFactory(filter_)


        
        self.assertIsInstance(attr_filter, pandor.NotInNetwork)
        self.assertTrue(attr_filter.filter(excluded))
        self.assertFalse(attr_filter.filter(included))


if "__main__" in __name__:
    unittest.main()
