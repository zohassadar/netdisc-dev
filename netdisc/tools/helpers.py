import dataclasses
import functools
import logging
import pprint
import sys
import time
import typing
import pathlib

import yaml

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

_ASDICT = "_asdict"
_ITER = "__iter__"
_REPR = "__repr__"
_INIT = "__init__"
UPDATE = "update"


def dummy(*args, **kwargs):
    """Stand in function that returns itself"""
    logger.debug("Dummy Executed with args: %s kwargs: %s", args, kwargs)
    return dummy


class NEED_LIST:
    """A marker to indicate that a list is required at instantiation"""


def fake_orm_relationship(*args, **kwargs) -> NEED_LIST:
    logger.debug(
        "fake_orm_relationship Executed with args: %s kwargs: %s", args, kwargs
    )
    return NEED_LIST


def validate_wrapper_args(*wrapped, filter_=None) -> tuple[type | None, callable]:
    if wrapped and len(wrapped) > 1 or wrapped and filter_:
        raise ValueError(
            "add_kwargs_init takes 1 positional argument or 1 keyword argument"
        )
    if wrapped:
        (wrapped,) = wrapped
        print(type(wrapped))
        assert isinstance(wrapped, type)
    else:
        wrapped = None
    if filter_:
        assert callable(filter_)
    else:
        filter_ = lambda _: _
    return wrapped, filter_


def add_kwargs_init(*wrapped, filter_=None):
    wrapped, filter_ = validate_wrapper_args(*wrapped, filter_=filter_)

    def new_init(self, **kwargs):
        for prop in dir(self):
            if isinstance(getattr(type(self), prop, None), functools.cached_property):
                continue
            if prop.startswith("_"):
                continue
            if getattr(self, prop) is NEED_LIST:
                setattr(self, prop, [])
        for key, value in kwargs.items():
            if not (hasattr(self, key) and filter_(key)):
                raise AttributeError(
                    f"{key} is an invalid keyword for {self.__class__.__name__}"
                )
            if value is not None:
                setattr(self, key, value)

    def wrapper(cls):
        assert isinstance(cls, type)
        setattr(cls, _INIT, new_init)
        return cls

    if wrapped:
        return wrapper(wrapped)
    return wrapper


def add_as_dict(*wrapped, filter_: typing.Callable = None):
    wrapped, filter_ = validate_wrapper_args(*wrapped, filter_=filter_)

    def new_asdict(self):
        return {k: v for k, v in self.__dict__.items() if filter_(k) and v is not None}

    def wrapper(cls):
        assert isinstance(cls, type)
        setattr(cls, _ASDICT, new_asdict)
        return cls

    if wrapped:
        return wrapper(wrapped)
    return wrapper


def dict_repr_helper(*wrapped, filter_=None):
    wrapped, filter_ = validate_wrapper_args(*wrapped, filter_=filter_)

    def new_repr(self):
        return (
            self.__class__.__name__
            + "("
            + ", ".join([f"{key}={value!r}" for key, value in self._asdict().items()])
            + ")"
        )

    def update(self, *args, **kwargs):
        updates = kwargs
        for arg in args:
            if isinstance(arg, dict):
                updates.update(arg)
            else:
                raise ValueError("Unknown type passed to update: {type(args[0])}")
        for key, value in updates.items():
            if not hasattr(self, key):
                raise ValueError(f"Invalid Key.  {key=} {value=}")
            if value is not None:
                setattr(self, key, value)

    def new_iter(self):
        return iter(self._asdict().items())

    def wrapper(cls):
        add_as_dict(filter_=filter_)(cls)
        setattr(cls, _ITER, new_iter)
        setattr(cls, _REPR, new_repr)
        setattr(cls, UPDATE, update)
        return cls

    if wrapped:
        return wrapper(wrapped)

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


def debugger(level: int = logging.DEBUG, old_trim: bool = False) -> typing.Callable:
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

    def new_trimmer(obj):
        pretty = pprint.pformat(obj)
        NEWLINE = "\n"
        if NEWLINE in pretty:
            pretty = "".join((NEWLINE, pretty))
        return pretty

    trimmer = new_trimmer if not old_trim else old_trimmer

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
                if message := str(exc):
                    message = message.splitlines()[0]
                logging.error(
                    "%s raised %s: %s",
                    wrapped.__name__,
                    repr(exc),
                    message,
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


@dataclasses.dataclass
class SNMPEngDebugDumper:
    """Used to store data retrieved from `get` & `walk` functions of the snmp engine

    args must be tuple-able

    """

    file: str

    def __post_init__(self):
        self._enabled = False
        if self.file:
            logger.error("Writing SNMP output to: %s", self.file)
            pathlib.Path(self.file)
            self._enabled = True
        else:
            logger.info("SNMP output won't be recorded")

    def dump(self, ip, result, *args):
        if not self._enabled:
            logger.info("Skipping this dump")
            return
        logger.warning("Dumping contents for %s", ip)
        contents = None
        try:
            with open(self.file) as f:
                contents = yaml.load(f, Loader=yaml.Loader)
        except FileNotFoundError:
            pass
        if not contents:
            contents = {}

        contents.setdefault(ip, {})[args] = result
        with open(self.file, "w+") as f:
            print(yaml.dump(contents), file=f)


@dataclasses.dataclass
class SNMPEngDumpedDebug:
    file: str
    ip: str

    def __post_init__(self):
        with open(self.file) as f:
            self._loaded = yaml.load(f, Loader=yaml.Loader).get(self.ip, {})

    def retrieve(self, *keys):
        return self._loaded.get(keys)
