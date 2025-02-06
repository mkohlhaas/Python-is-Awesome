#!/usr/bin/env python


if __name__ == "__main__":
    user_input = input("Name: ")
    if user_input:
        name = user_input
    else:
        name = "N/A"
    print(name)

    # Using 'or'
    user_input = input("Name: ")
    name = user_input or "N/A"
    print(name)
