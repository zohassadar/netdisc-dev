import functools
import logging
import pprint
import sys
import time
import typing

from netdisc import output

_ASDICT = "_asdict"
_ITER = "__iter__"
_REPR = "__repr__"
_INIT = "__init__"


def dummy(*args, **kwargs):
    """Stand in function that returns itself"""
    return dummy


class NEED_LIST:
    """A marker to indicate that a list is required at instantiation"""


def fake_orm_relationship(*args, **kwargs) -> NEED_LIST:
    return NEED_LIST


def add_kwargs_init(*wrapped, filter_=None):
    if wrapped and len(wrapped) > 1 or wrapped and filter_:
        raise ValueError(
            "add_as_dict takes 1 positional argument or 1 keyword argument"
        )

    if not filter_:
        filter_ = lambda _: _

    def new_init(self, **kwargs):
        for prop in dir(self):
            if not prop.startswith("_"):
                if getattr(self, prop) is NEED_LIST:
                    setattr(self, prop, [])
        for key, value in kwargs.items():
            print(f"{key=} {value=}")
            if hasattr(self, key) and filter_(key):
                setattr(self, key, value)
            else:
                raise AttributeError(
                    f"{key} is an invalid keyword for {self.__class__.__name__}"
                )

    def wrapper(cls):
        setattr(cls, _INIT, new_init)
        return cls

    if wrapped:
        return wrapper(wrapped[0])
    return wrapper


def add_as_dict(*wrapped, filter_: typing.Callable = None):
    if wrapped and len(wrapped) > 1 or wrapped and filter_:
        raise ValueError(
            "add_as_dict takes 1 positional argument or 1 keyword argument"
        )

    if not filter_:
        filter_ = lambda _: _

    def new_asdict(self):
        return {k: v for k, v in self.__dict__.items() if filter_(k)}

    def wrapper(cls):
        setattr(cls, _ASDICT, new_asdict)
        return cls

    if wrapped:
        return wrapper(wrapped[0])
    return wrapper


def dict_repr_helper(*wrapped, filter_=None):
    if wrapped and len(wrapped) > 1 or wrapped and filter_:
        raise ValueError(
            "add_as_dict takes 1 positional argument or 1 keyword argument"
        )

    if not filter_:
        filter_ = lambda _: _

    def new_repr(self):
        return (
            self.__class__.__name__
            + "("
            + ", ".join([f"{key}={value!r}" for key, value in self._asdict().items()])
            + ")"
        )

    def new_iter(self):
        return iter(self._asdict().items())

    def wrapper(cls):
        add_as_dict(filter_=filter_)(cls)
        setattr(cls, _ITER, new_iter)
        setattr(cls, _REPR, new_repr)
        return cls

    if wrapped:
        return wrapper(wrapped[0])

    return wrapper


class suppress_logs:
    def __init__(self):
        self._buffer = []
        self._start_time = 0.0
        self._real_write = sys.stderr.write

    def _buffered_write(self, *args, **kwargs):
        self._buffer.append((args, kwargs))

    def _dump(self, *args, **kwargs):
        for args, kwargs in self._buffer:
            sys.stderr.write(*args, **kwargs)

    def __enter__(self):
        self._start_time = time.perf_counter()
        logging.info("Buffering STDERR")
        sys.stderr.write = self._buffered_write

    def __exit__(self, exit_type, exit_value, exit_traceback):
        if exit_type:
            logging.critical(
                "Error encountered: %s, %s, %s", exit_type, exit_value, exit_traceback
            )
        sys.stderr.write = self._real_write
        self._dump()
        elapsed = time.perf_counter() - self._start_time
        logging.info(
            "Logging supressed for %s seconds.  %s messages buffered",
            elapsed,
            len(self._buffer),
        )


def debugger(level: int = logging.DEBUG) -> typing.Callable:
    if not isinstance(level, int):
        raise ValueError("debugger must be called with log level when decorating")

    MAX_MSG_LENGTH = 25
    TRIMMED_SUFFIX = "..."
    limiter = slice(0, MAX_MSG_LENGTH)

    def old_trimmer(obj):
        obj_repr = repr(obj)
        obj_limited = obj_repr[limiter]
        if len(obj_repr) > MAX_MSG_LENGTH:
            obj_limited = "".join((obj_limited, TRIMMED_SUFFIX))
        return obj_limited

    @functools.singledispatch
    def trimmer(obj):
        pretty = pprint.pformat(obj)
        NEWLINE = "\n"
        if NEWLINE in pretty:
            pretty = "".join((NEWLINE, pretty))
        return pretty

    # Placeholder to treat different objects differently
    # @trimmer.register
    # def _(obj: list):

    def arg_kwarg_trimmer(*args, **kwargs):
        limited = []
        for arg in args:
            limited.append(trimmer(arg))
        for key, value in kwargs.items():
            limited.append("=".join((key, trimmer(value))))
        return ", ".join(limited)

    def level_set_wrapper(wrapped: typing.Callable) -> typing.Callable:
        @functools.wraps(wrapped)
        def wrapper(*args, **kwargs):
            logging.log(
                level,
                "%s called with %s",
                wrapped.__name__,
                arg_kwarg_trimmer(*args, **kwargs),
            )
            try:
                result = wrapped(*args, **kwargs)
                logging.log(
                    level,
                    "%s returns: %s",
                    wrapped.__name__,
                    trimmer(result),
                )
                return result
            except Exception as exc:
                logging.error(
                    "%s raised %s: %s",
                    wrapped.__name__,
                    repr(exc),
                    str(exc).splitlines()[0],
                )
                raise exc

        return wrapper

    return level_set_wrapper


def debug_shorten(obj: typing.Any, length: int = 40):
    obj_repr = str(obj)
    original_length = len(obj_repr)
    suffix = ""
    if original_length > length:
        suffix = "..."
    return f"{obj_repr[:length]}{suffix}"
