#!/usr/bin/env python

import io
from contextlib import contextmanager
from io import TextIOBase
from pathlib import Path
from types import TracebackType


# 1. Class-based Context Managers (typical approach)
class File:
    def __init__(self, path: Path):
        self.path: Path = path
        self._obj: TextIOBase | None = None

    def open(self):
        try:
            self._obj = io.open(self.path)
        except FileNotFoundError:
            print("File not found.")

    def close(self):
        if self._obj:
            self._obj.close()
            self._obj = None

    def read(self):
        if self._obj:
            return self._obj.read()

    def __enter__(self):
        print("Entering context...")
        self.open()
        return self

    # https://adamj.eu/tech/2021/07/04/python-type-hints-how-to-type-a-context-manager/
    # Also discusses type narrowing with @overload
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ):
        errored = False
        if isinstance(exc_val, UnicodeDecodeError):
            print("Found invalid Unicode character!")
            errored = True  # Unicode exception not reraised - suppressing the error
        print("Exiting the context ...")
        self.close()
        return errored


# 2. Function-based Context Managers


@contextmanager
def open_file(path: Path):
    print("Entering context ...")
    f = open(path)
    try:
        yield f
    except UnicodeDecodeError as e:
        print("Found invalid Unicode character!")
        raise e
    finally:
        f.close()
    print("Exiting context ...")


if __name__ == "__main__":
    # 1. Class-based Context Managers (typical approach)

    with open("hello.txt", "r") as f:
        print(f.read())

    with File(Path("hello.txt")) as f:
        if txt := f.read():
            print(txt.strip())

    with File(Path("invalid_unicode.txt")) as f:
        if txt := f.read():
            print(txt.strip())
    print("Script is still running!")

    # 2. Function-based Context Managers

    with open_file(Path("hello.txt")) as f:
        if txt := f.read():
            print(txt.strip())

    with open_file(Path("invalid_unicode.txt")) as f:
        if txt := f.read():
            print(txt.strip())
