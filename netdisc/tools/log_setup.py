import argparse
import dataclasses
import logging
import logging.handlers
import pathlib

BASIC_FORMAT = dict(
    fmt="{levelname:<8}: {message}",
    style="{",
    validate=True,
)

BASIC_FORMAT_FILENAME = dict(
    fmt="{pathname}\n{levelname:<8}: {message}",
    style="{",
    validate=True,
)

DEBUG_FORMAT = dict(
    fmt="{asctime} - {name}:{levelname:<8}:{threadName}:{funcName}:{lineno} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    validate=True,
)

DEBUG_FORMAT_FILENAME = dict(
    fmt="{pathname}\n{asctime} - {name}:{levelname:<8}:{threadName}:{funcName}:{lineno} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    validate=True,
)


log_parser = argparse.ArgumentParser(add_help=False)

log_parser_group = log_parser.add_argument_group("Logging options")
log_parser_group.add_argument(
    "-v",
    "--verbose",
    action="count",
    default=0,
    help="Logging verbosity.  -v through -vvvvv",
)

log_parser_group.add_argument(
    "--debug-file",
    type=str,
    help="Debug output file",
)

log_parser_group.add_argument(
    "--debug-file-level",
    type=int,
    default=5,
    help="Debug file level.  1-5.  Default 5",
)

log_parser_group.add_argument(
    "--debug-file-size",
    type=int,
    default=10,
    help="Size in MB of debug file.  Default 10",
)

log_parser_group.add_argument(
    "--debug-file-depth",
    type=int,
    default=1,
    help="Number of archived debug files.  Minimum 1.  Default 1.",
)

log_parser_group.add_argument(
    "--include-path",
    action="store_true",
    help="Include entire module path in debug output",
)

log_parser_group.add_argument(
    "--modules",
    nargs="+",
    help="Limit logging to module(s)",
)


@dataclasses.dataclass
class FilterLogByModules:
    modules: list[str] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self._filtered = {}

    def _is_name_filtered(self, name: str) -> bool:
        if not self.modules:
            return True
        for module in self.modules:
            if module in name:
                return True
        return False

    def filter(self, record: logging.LogRecord) -> bool:
        return self._filtered.setdefault(
            record.name,
            self._is_name_filtered(record.name),
        )


def get_log_level(level: int) -> int:
    if not level:
        level = logging.CRITICAL + 1

    elif level == 1:
        level = logging.CRITICAL

    elif level == 2:
        level = logging.ERROR

    elif level == 3:
        level = logging.WARNING

    elif level == 4:
        level = logging.INFO

    elif level >= 5:
        level = logging.DEBUG
    return level


def set_logger(
    verbose: int = logging.NOTSET,
    debug=False,
    log_file: str = None,
    log_file_level: int = logging.NOTSET,
    log_file_mb: int = 10,
    log_file_depth: int = 1,
    modules: list = None,
    include_path: bool = False,
):
    if modules is None:
        modules = []
    logger = logging.getLogger()
    while logger.handlers:
        logger.handlers.pop()
    stream_level = get_log_level(verbose)
    file_level = get_log_level(log_file_level)
    logger.setLevel(min(stream_level, file_level))

    log_filter = FilterLogByModules(modules)
    handler = logging.StreamHandler()
    handler.addFilter(log_filter)
    handler.setLevel(stream_level)

    if (stream_level is logging.DEBUG or debug) and include_path:
        log_format = DEBUG_FORMAT_FILENAME
    elif stream_level is logging.DEBUG or debug:
        log_format = DEBUG_FORMAT
    elif include_path:
        log_format = BASIC_FORMAT_FILENAME
    else:
        log_format = BASIC_FORMAT

    handler.setFormatter(logging.Formatter(**log_format))
    logger.addHandler(handler)

    if log_file:
        file_size_bytes = log_file_mb * 1024 * 1024
        file_handler = logging.handlers.RotatingFileHandler(
            filename=log_file,
            maxBytes=file_size_bytes,
            backupCount=log_file_depth,
        )
        file_handler.setLevel(file_level)
        file_handler.addFilter(log_filter)
        file_handler.setFormatter(logging.Formatter(**DEBUG_FORMAT_FILENAME))
        logger.addHandler(file_handler)

    if logger.level > logging.CRITICAL:
        logger.disabled = True


def set_logger_from_args():
    (parsed, _) = log_parser.parse_known_args()
    set_logger(
        verbose=parsed.verbose,
        log_file=parsed.debug_file,
        log_file_level=parsed.debug_file_level,
        log_file_mb=parsed.debug_file_size,
        log_file_depth=parsed.debug_file_depth,
        modules=parsed.modules,
        include_path=parsed.include_path,
    )
