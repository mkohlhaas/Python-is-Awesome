#!/usr/bin/env python

if __name__ == "__main__":
    with open("input.txt", "r") as input, open("ouptput.txt", "w") as output:
        text = input.readlines()
        uppercase = [t.upper() for t in text]
        output.writelines(uppercase)

