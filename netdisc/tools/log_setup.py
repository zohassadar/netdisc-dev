import dataclasses
import logging
import logging.handlers

BASIC_FORMAT = dict(
    fmt="{levelname:<8}: {message}",
    style="{",
    validate=True,
)

DEBUG_FORMAT = dict(
    fmt="{asctime} - {name}:{levelname:<8}:{funcName}:{lineno} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    validate=True,
)

DEBUG_FORMAT_FILENAME = dict(
    fmt="{pathname}\n{asctime} - {name}:{levelname:<8}:{funcName}:{lineno} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M:%S",
    validate=True,
)


@dataclasses.dataclass
class FilterLogByModules:
    modules: list[str] = dataclasses.field(default_factory=list)

    def __post_init__(self):
        self._filtered = {}

    def is_name_filtered(self, name: str) -> bool:
        if not self.modules:
            return True
        for module in name.split("."):
            if module in self.modules:
                return True
        return False

    def filter(self, record: logging.LogRecord) -> bool:
        return self._filtered.setdefault(
            record.name,
            self.is_name_filtered(record.name),
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
    log_file: str = None,
    log_file_level: int = logging.NOTSET,
    log_file_mb: int = 10,
    log_file_depth: int = 1,
    modules: list = None,
):
    if modules is None:
        modules = []
    logger = logging.getLogger()
    stream_level = get_log_level(verbose)
    file_level = get_log_level(log_file_level)
    logger.setLevel(min(stream_level, file_level))

    log_filter = FilterLogByModules(modules)
    handler = logging.StreamHandler()
    handler.addFilter(log_filter)
    handler.setLevel(stream_level)

    log_format = BASIC_FORMAT
    if stream_level is logging.DEBUG:
        log_format = DEBUG_FORMAT
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
