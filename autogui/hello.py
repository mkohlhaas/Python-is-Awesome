#!/usr/bin/env python

from random import randint
import pyautogui as ag


if __name__ == "__main__":
    while True:
        x = randint(0, 3440)
        y = randint(0, 1440)
        ag.moveTo(x, y, 0.5)
        ag.sleep(1)
