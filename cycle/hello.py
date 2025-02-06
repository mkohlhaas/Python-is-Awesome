#!/usr/bin/env python

from itertools import cycle
from time import sleep


lights = [  # (traffic light color, duration in seconds)
    ("red", 2),
    ("yellow", 0.5),
    ("green", 2),
]


if __name__ == "__main__":
    traffic_light = cycle(lights)
    while True:
        col, dur = next(traffic_light)
        print(col)
        sleep(dur)
