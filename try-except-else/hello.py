#!/usr/bin/env python


if __name__ == "__main__":
    n = input("Numerator: ")
    d = input("Denominator: ")

    # snippet shortcut 'trya' (there's also 'try', tryf' and 'tryef')
    try:
        res = int(n) / int(d)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    else:
        print(res)
