#!/usr/bin/env python

profile = {
    "name": "N/A",
    "email": "N/A",
    "phone": "N/A",
}

user_input = {
    "name": "Bob",
    "phone": "123-456-7890",
}

if __name__ == "__main__":
    # dict union operator
    profile |= user_input
    print(profile)
