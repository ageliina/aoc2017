#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv


def find_div_pair(row):

    row = sorted(row)

    for i in range(len(row)):
        for j in range(i+1, len(row)):
            if row[j] % row[i] == 0:
                return row[i], row[j]
    return None


def checksum(rows, even=False):
    s = 0
    for row in rows:
        if not even:
            s += max(row) - min(row)
        else:
            nums = find_div_pair(row)
            s += nums[1] // nums[0]
    return s


def get_rows(fname):
    ret = []
    with open(fname, 'r') as f:
        for line in f:
            numbers = [int(w) for w in line.split()]
            ret.append(numbers)
    return ret


def test_get_rows():
    drows = [[5, 1, 9, 5],
             [7, 5, 3],
             [2, 4, 6, 8]]
    rows = get_rows("./test_input.txt")
    assert drows == rows

    drows = [[5, 9, 2, 8],
             [9, 4, 7, 3],
             [3, 8, 6, 5]]
    rows = get_rows("./test_input2.txt")
    assert drows == rows


def test_checksum():

    rows = [[5, 1, 9, 5],
            [7, 5, 3],
            [2, 4, 6, 8]]
    assert checksum(rows, False) == 18

    rows = [[5, 9, 2, 8],
            [9, 4, 7, 3],
            [3, 8, 6, 5]]
    assert checksum(rows, True) == 9

# Main
if __name__=="__main__":
    test_get_rows()
    test_checksum()

    rows = get_rows("./input.txt")
    print("1: ", checksum(rows, False))
    print("2: ", checksum(rows, True))



