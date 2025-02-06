#!/usr/bin/env python


def do_this():
    print("Doing this!")


def do_that():
    print("Doing that!")


if __name__ == "__main__":
    match input("Do this or that? "):
        case "this":
            do_this()
        case "that":
            do_that()
        case _:
            print("Invalid input!")
