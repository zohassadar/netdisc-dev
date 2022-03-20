import unittest

from netdisc.tools import helpers

filter_ = lambda key: not key.startswith("a")


@helpers.add_kwargs_init()
class AddsKwargsEmptyCalled:
    a = 1
    b = 2


@helpers.add_kwargs_init(filter_=filter_)
class AddsKwargsFilter:
    a = 1
    b = 2


@helpers.add_kwargs_init
class AddsDictEmpty:
    a = 1
    b = 2


@helpers.add_kwargs_init()
class AddsDictEmptyCalled:
    a = 1
    b = 2


@helpers.add_kwargs_init(filter_=filter_)
class AddsDictFilter:
    a = 1
    b = 2


class TestToolsHelpers(unittest.TestCase):
    def test_helper_empty(self):
        @helpers.add_kwargs_init
        class AddsKwargsEmpty:
            a = 1
            b = 2

        AddsKwargsEmpty()
