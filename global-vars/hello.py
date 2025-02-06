#!/usr/bin/env python

global_var = 10


def slow():
    res = 0
    for i in range(1000):
        res += global_var * i
    return res


# 10% faster
def faster():
    res = 0
    local_var = global_var
    for i in range(1000):
        res += local_var * i
    return res


if __name__ == "__main__":
    print(slow())
    print(faster())

