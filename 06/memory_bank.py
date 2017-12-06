#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv


def redistribute(arr):

    l = len(arr)
    ret = arr.copy()
    val = max(ret)
    idx = ret.index(val)
    i = (idx + 1) % l
    while val > 0:
        if i != idx:
            ret[i] += 1
            val -= 1
        i = (i + 1) % l
        if i == idx and val == 1:
            break
    ret[idx] = val
    return ret

def memory_bank(arr):
    configurations = {}
    cycles = 0
    while True:
        h = hash(str(arr))
        if h in configurations.keys():
            return cycles, cycles - configurations[h]
        else:
            configurations[h] = cycles
        arr = redistribute(arr)
        cycles += 1

def test_redistribute():
    assert redistribute([0,2,7,0]) == [2,4,1,2]
    assert redistribute([2,4,1,2]) == [3,1,2,3]
    assert redistribute([3,1,2,3]) == [0,2,3,4]
    assert redistribute([0,2,3,4]) == [1,3,4,1]
    assert redistribute([1,2,5,4,3]) == [2,3,1,5,4]
    assert redistribute([1,6,3,1]) == [3,0,5,3]


def test_memory_bank():
    arr = [0, 2, 7, 0]
    assert memory_bank(arr) == (5,4)


# Main
if __name__=="__main__":

    test_redistribute()
    test_memory_bank()

    with open("input.txt", 'r') as f:
        arr = [int(a) for a in f.readline().split()]
        print(memory_bank(arr))


