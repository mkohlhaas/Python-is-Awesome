#!/usr/bin/env python


if __name__ == "__main__":
    x = "abc"
    print(x)
    # returns a copy (strings are immutable!)
    x.replace("a", "1")
    print(x)
    x + "def"
    print(x)  # abc

    # this would be the intended code
    x = "abc"
    x = x.replace("a", "1")
    x += "def"
    print(x)  # 1bcdef
