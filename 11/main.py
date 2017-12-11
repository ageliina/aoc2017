#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv
import numpy as np

def walk(steps):
    xy = np.array([0, 0])
    d = 0

    for step in steps:
        if step == "ne":
            xy += np.array([1, 1])
        if step == "n":
            xy += np.array([0, 1])
        if step == "nw":
            xy += np.array([-1, 1])
        if step == "sw":
            xy += np.array([-1, -1])
        if step == "s":
            xy += np.array([0, -1])
        if step == "se":
            xy += np.array([1, -1])
        dd = np.abs(xy[0])
        d = dd if dd > d else d
    return xy, d

# Main
if __name__=="__main__":
    steps = None
    with open("input.txt", 'r') as f:
        steps = f.readline().split(',')
    xy = walk(steps)
    print(xy)


