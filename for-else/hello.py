#!/usr/bin/env python


if __name__ == "__main__":
    for n in range(2, 30):
        for x in range(2, n):
            if n % x == 0:
                print(n, " = ", x, "*", n // x)
                break
        else:
            # loop fell through without finding a factor
            print(n, "is prime")
