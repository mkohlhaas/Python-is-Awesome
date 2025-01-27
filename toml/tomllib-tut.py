#!/usr/bin/env python

import tomllib
from pprint import pprint

if __name__ == "__main__":
    with open("test.toml", "rb") as f:
        config = tomllib.load(f)
        pprint(config)
        print(f'\nHomepage: {config["project"]["urls"]["Homepage"]}')

    print("\n====================================================================\n")

    with open("test.toml") as f:
        config = tomllib.loads(f.read())
        pprint(config)
        print(f'\nHomepage: {config["project"]["urls"]["Homepage"]}')
