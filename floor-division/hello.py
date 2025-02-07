#!/usr/bin/env python


if __name__ == "__main__":
    x = [4, -5, 6]
    # // (floor division) -> rounds to towards negative infinity
    z = list(map(lambda x: abs(x // 2), x))
    print(z)  # [2, 3, 3]
