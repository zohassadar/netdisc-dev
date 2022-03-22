import logging
from unittest import mock

import pytest
from netdisc.tools import helpers

startswith_a = lambda x: x.startswith("a")

fake_arg_kwargs = (
    ("args", "kwargs"),
    (
        pytest.param((), {}, id="None"),
        pytest.param((1,), {}, id="Arg"),
        pytest.param((1, 2), {}, id="Args"),
        pytest.param((), dict(a=1), id="Kwarg"),
        pytest.param((), dict(a=1, b=2), id="Kwargs"),
        pytest.param((1,), dict(a=1), id="ArgKwarg"),
        pytest.param(
            ("multi\nline",),
            dict(a={"input": "contains\ndict"}, b={x: x for x in range(1000)}),
            id="ComplicatedArgKwarg",
        ),
    ),
)


@pytest.mark.parametrize(*fake_arg_kwargs)
def test_dummy(args, kwargs):
    dummy = helpers.dummy(*args, **kwargs)
    assert callable(dummy)


@pytest.mark.parametrize(*fake_arg_kwargs)
def test_fake_orm_relationship(args, kwargs):
    relationship = helpers.fake_orm_relationship(*args, **kwargs)
    assert relationship is helpers.NEED_LIST


def test_add_kwargs_init():
    @helpers.add_kwargs_init
    class Test:
        ...

    assert Test()


@pytest.mark.parametrize(*fake_arg_kwargs)
def test_add_kwargs_init_with_fake_relationship(args, kwargs):
    @helpers.add_kwargs_init
    class Test:
        fake = helpers.fake_orm_relationship(*args, **kwargs)

    assert isinstance(Test().fake, list)


def test_add_kwargs_init_valid_filter():
    @helpers.add_kwargs_init(filter_=startswith_a)
    class Test:
        ...

    assert Test()


def test_add_kwargs_init_invalid_call():
    with pytest.raises(ValueError):

        helpers.add_kwargs_init(1, 2)


def test_add_kwargs_init_invalid_filter():
    with pytest.raises(AssertionError):
        helpers.add_kwargs_init(filter_=1)


def test_add_kwargs_init_forgot_keyword():
    with pytest.raises(AssertionError):
        helpers.add_kwargs_init(startswith_a)


def test_add_kwargs_init_wrapped_function():
    with pytest.raises(AssertionError):

        @helpers.add_kwargs_init
        def test():
            ...


def test_add_kwargs_init_wrapped_function_valid_filter():
    with pytest.raises(AssertionError):

        @helpers.add_kwargs_init(filter_=startswith_a)
        def test():
            ...


def test_no_kwargs_init_applied():
    with pytest.raises(TypeError):

        class Test:
            a: int = 0

        assert Test(a=1)


def test_kwargs_init_applied():
    @helpers.add_kwargs_init
    class Test:
        a: int = 0

    assert Test(a=1)


def test_kwargs_init_applied_with_filter_error():
    with pytest.raises(AttributeError):

        @helpers.add_kwargs_init(filter_=startswith_a)
        class Test:
            a: int = 0
            b: int = 0

        assert Test(a=1, b=2)


def test_kwargs_init_applied_with_filter():
    @helpers.add_kwargs_init(filter_=startswith_a)
    class Test:
        a: int = 0
        b: int = 0

    assert Test(a=1)


def test_add_as_dict_no_filter():
    @helpers.add_as_dict
    @helpers.add_kwargs_init
    class Test:
        a: int = 0
        b: int = 0

    assert Test(a=1, b=2)._asdict() == dict(a=1, b=2)


def test_add_as_dict_filter():
    @helpers.add_as_dict(filter_=startswith_a)
    @helpers.add_kwargs_init
    class Test:
        a: int = 0
        b: int = 0

    assert Test(a=1, b=2)._asdict() == dict(a=1)


def test_add_repr_helper_no_filter():
    @helpers.dict_repr_helper
    @helpers.add_kwargs_init
    class Test:
        a: int = 0
        b: int = 0

    assert repr(Test(a=1, b=2)) == "Test(a=1, b=2)"


def test_add_repr_helper_with_filter():
    @helpers.dict_repr_helper(filter_=startswith_a)
    @helpers.add_kwargs_init
    class Test:
        a: int = 0
        b: int = 0

    assert repr(Test(a=1, b=2)) == "Test(a=1)"


def test_add_repr_helper_no_filter_dict():
    @helpers.dict_repr_helper
    @helpers.add_kwargs_init
    class Test:
        a: int = 0
        b: int = 0

    assert dict(Test(a=1, b=2)) == dict(a=1, b=2)


def test_add_repr_helper_with_filter_dict():
    @helpers.dict_repr_helper(filter_=startswith_a)
    @helpers.add_kwargs_init
    class Test:
        a: int = 0
        b: int = 0

    assert dict(Test(a=1, b=2)) == dict(a=1)


def test_debugger_no_args():
    with pytest.raises(ValueError):

        @helpers.debugger
        def test():
            ...


def test_debugger_one_args():
    @helpers.debugger(level=10)
    def test():
        ...

    assert callable(test)


def test_debugger_both_args():
    @helpers.debugger(level=10, old_trim=True)
    def test():
        ...

    assert callable(test)


def test_debugger_logging():
    @helpers.debugger(level=10)
    def test():
        ...

    with mock.patch("logging.log") as mock_log:
        test()
        assert mock_log.called


def test_debugger_no_logging():
    @helpers.debugger(level=10)
    def test():
        ...

    with pytest.raises(AssertionError):
        with mock.patch("logging.log") as mock_log:
            assert mock_log.called


@pytest.mark.parametrize(*fake_arg_kwargs)
def test_debugger_combinations(args, kwargs):
    @helpers.debugger(level=10)
    def test(*args, **kwargs):
        ...

    with mock.patch("logging.log") as mock_log:
        test(*args, **kwargs)
        assert mock_log.called


@pytest.mark.parametrize(*fake_arg_kwargs)
def test_debugger_combinations_old_trimmer(args, kwargs):
    @helpers.debugger(level=10, old_trim=True)
    def test(*args, **kwargs):
        ...

    with mock.patch("logging.log") as mock_log:
        test(*args, **kwargs)
        assert mock_log.called


@pytest.mark.parametrize(*fake_arg_kwargs)
def test_debugger_combinations_exception(args, kwargs):
    @helpers.debugger(level=10, old_trim=True)
    def test(*args, **kwargs):
        raise RuntimeError("what")

    with (
        mock.patch("logging.error") as mock_error,
        mock.patch("logging.log") as mock_log,
    ):
        with pytest.raises(RuntimeError):
            test(*args, **kwargs)
        assert mock_log.called
        assert mock_error.called


@pytest.mark.parametrize(*fake_arg_kwargs)
def test_debugger_combinations_exception_no_args(args, kwargs):
    @helpers.debugger(level=10, old_trim=True)
    def test(*args, **kwargs):
        raise RuntimeError

    with (
        mock.patch("logging.error") as mock_error,
        mock.patch("logging.log") as mock_log,
    ):
        with pytest.raises(RuntimeError):
            test(*args, **kwargs)
        assert mock_log.called
        assert mock_error.called


def test_debug_shorten_short():
    string = "!" * 49
    result = helpers.debug_shorten(string, length=50)
    assert result == string


def test_debug_shorten_at_limit():
    string = "!" * 50
    result = helpers.debug_shorten(string, length=50)
    assert result == string


def test_debug_shorten_exceed():
    string = "!" * 51
    result = helpers.debug_shorten(string, length=50)
    assert result == ("!" * 50) + "..."


def test_suppress_logs():
    with mock.patch("sys.stderr.write") as mocked_real_write:
        with helpers.suppress_logs():
            logger = logging.getLogger("test_logger")
            logger.addHandler(logging.StreamHandler())
            logger.critical("hi")
            assert not mocked_real_write.called
        assert mocked_real_write.called


def test_suppress_logs_with_error():
    with mock.patch("sys.stderr.write") as mocked_real_write:
        with pytest.raises(RuntimeError):
            logging.basicConfig(level=logging.CRITICAL, force=True)
            with helpers.suppress_logs():
                logger = logging.getLogger("test_logger")
                logger.addHandler(logging.StreamHandler())
                logger.critical("hi")
                assert not mocked_real_write.called
                raise RuntimeError
        assert mocked_real_write.called
