#!/usr/bin/env python


if __name__ == "__main__":
    x = "abcABC"
    print(x)
    y = x.title()
    print(y)
    z = y.rfind("b")  # returns highest index
    print(z)
