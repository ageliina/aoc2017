#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv

def jump(arr, alternative=False):

    jumps = 0
    index = 0
    arr = arr.copy()

    while True:

        new_index = index + arr[index]
        jumps += 1

        if new_index >= len(arr):
            return jumps

        if not alternative or (alternative and arr[index] < 3):
            arr[index] += 1
        else:
            arr[index] -= 1
        index = new_index

def test_jump():
    arr = [0,3,0,1,-3]

    assert jump(arr) == 5
    print(jump(arr,True))

# Main
if __name__=="__main__":
    test_jump()

    arr = []
    with open("input.txt", 'r') as f:
        for line in f:
            arr.append(int(line.strip()))
    print(jump(arr))
    print(jump(arr,True))
