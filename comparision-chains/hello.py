#!/usr/bin/env python

if __name__ == "__main__":
    a = 1
    b = 2
    c = 3

    if a < b < c:
        print("Chaining comparison operators.")

    if a < b and b < c:
        print("The same.")
