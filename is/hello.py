#!/usr/bin/env python

if __name__ == "__main__":
    entry = input("Password: ")
    if entry is "secret":
        print("Access Granted!")
    else:
        print("Access Denied!")

    # this is really what you mean:
    entry = input("Password: ")
    if entry == "secret":
        print("Access Granted!")
    else:
        print("Access Denied!")
