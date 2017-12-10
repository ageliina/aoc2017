#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv

def peek(a):
    return a[-1]

def stream_processing(s):
    is_garbage = False
    is_ignored = False

    score = 0
    garbage = 0
    ret = 0

    for char in s:

        if is_ignored:
            is_ignored = False
            continue

        if char == '!':
            is_ignored = True
            continue

        if char == '<' and not is_garbage:
            is_garbage = True
            continue

        if char == '>' and is_garbage:
            is_garbage = False
            continue

        if is_garbage:
            garbage += 1
            continue

        if char == '{':
            # Open a group
            score += 1
            continue

        if char == '}':
            # Close a group
            ret += score
            score -= 1
            continue

    return ret, garbage

def test_stream_processing():
    with open("test_input.txt", 'r') as f:
        assert stream_processing(f.readline().strip())[0] == 1
        assert stream_processing(f.readline().strip())[0] == 6
        assert stream_processing(f.readline().strip())[0] == 5
        assert stream_processing(f.readline().strip())[0] == 16
        assert stream_processing(f.readline().strip())[0] == 1
        assert stream_processing(f.readline().strip())[0] == 9
        assert stream_processing(f.readline().strip())[0] == 9
        assert stream_processing(f.readline().strip())[0] == 3

    with open("test_input2.txt", 'r') as f:
        assert stream_processing(f.readline().strip())[1] == 0
        assert stream_processing(f.readline().strip())[1] == 17
        assert stream_processing(f.readline().strip())[1] == 3
        assert stream_processing(f.readline().strip())[1] == 2
        assert stream_processing(f.readline().strip())[1] == 0
        assert stream_processing(f.readline().strip())[1] == 0
        assert stream_processing(f.readline().strip())[1] == 10

# Main
if __name__=="__main__":
    test_stream_processing()

    with open("input.txt", 'r') as f:
        print(stream_processing(f.readline()))


