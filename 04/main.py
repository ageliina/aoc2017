#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv


def is_valid(words, allow_anagrams=True):
    d = {}
    for word in words.split():
        if not allow_anagrams:
            word = "".join(sorted(word))

        if word in d.keys():
            return False

        d[word] = None
    return True


def n_valid(fname, allow_anagrams=True):
    s = 0
    with open(fname, 'r') as f:
        for line in f:
            if is_valid(line.strip(), allow_anagrams):
                s += 1
    return s

def test_is_valid():
    assert is_valid("aa bb cc dd ee")
    assert not is_valid("aa bb cc dd aa")
    assert is_valid("aa bb cc dd aaa")


# Main
if __name__=="__main__":
    test_is_valid()
    print(n_valid("input.txt"))
    print(n_valid("input.txt", False))


