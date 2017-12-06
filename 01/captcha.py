#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv
from numpy.random import random_integers


def get_numbers(word):
    return [int(w) for w in word]


def captcha(word, jmp=1):

    numbers = get_numbers(word)
    s = 0
    n = len(numbers)

    for i in range(n):
        cur = numbers[i]
        nex = numbers[(i+jmp)%n]
        if numbers[i] == numbers[(i+jmp)%n]:
            s += cur
    return s


def test_single(i):
    captcha("1"*10**i)


def test():
    assert captcha("1122") == 3
    assert captcha("1111") == 4
    assert captcha("1234") == 0
    assert captcha("91212129") == 9

#def test_long():

# Main
if __name__=="__main__":

    with open("./input.txt", 'r') as f:
        s = f.readline().strip()
        print("First: ", captcha(s, 1))
        print("Second: ", captcha(s, len(s) // 2))

    test_single(5)
    test()

