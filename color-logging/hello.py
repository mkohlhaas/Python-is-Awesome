#!/usr/bin/env python

import logging
from typing import override

FMT = "[{levelname:^8}] {name}: {message}"
FORMATS = {
    logging.INFO: FMT,
    logging.WARNING: f"\33[33m{FMT}\33[0m",
    logging.DEBUG: f"\33[36m{FMT}\33[0m",
    logging.ERROR: f"\33[35m{FMT}\33[0m",
    logging.CRITICAL: f"\33[31m{FMT}\33[0m",
}


class CustomFormatter(logging.Formatter):
    @override
    def format(self, record: logging.LogRecord) -> str:
        log_fmt = FORMATS[record.levelno]
        formatter = logging.Formatter(log_fmt, style="{")
        return formatter.format(record)


if __name__ == "__main__":
    handler = logging.StreamHandler()
    handler.setFormatter(CustomFormatter())
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[handler],
    )

    log = logging.getLogger("colored-logger")
    log.info("This is a message!")
    log.debug("This is a message!")
    log.warning("This is a message!")
    log.error("This is a message!")
    log.critical("This is a message!")
