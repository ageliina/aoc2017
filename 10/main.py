#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv


def get_lengths(s, asc=False):
    lengths = None
    func = None

    if asc:
        func = lambda x : ord(x)
        lengths = map(func, s)
    else:
        func = lambda x : int(x)
        lengths = map(func, s.split(','))

    return list(lengths)


def knot(lengths, numbers=list(range(256)), current_position=0, skip_size=0):

    N = len(numbers)

    for length in lengths:

        # Invalid lengths and lengths with no effect are skipped
        if length > N:
            continue

        sublist = []
        for i in range(current_position, current_position + length):
            sublist.append(numbers[i % N])
        sublist.reverse()

        for i in range(length):
            numbers[(current_position + i) % N] = sublist[i]

        # Increase current_position
        current_position = (current_position + length + skip_size) % N

        # Increase skip_size
        skip_size += 1

    return numbers[0] * numbers[1], numbers, current_position, skip_size


def knot_hash(lengths, numbers=list(range(256)), rounds=64):

    current_position = 0
    skip_size = 0
    N = len(numbers)

    sparse_hash = numbers.copy()

    # Knot the numbers
    for i in range(rounds):
        current_position, skip_size = knot(lengths,
                sparse_hash,
                current_position,
                skip_size)[2:]

    # Perform the XOR
    dense_hash = []
    for i in range(0, N, 16):
        xor = get_xor(sparse_hash[i:i+16])
        dense_hash.append(xor)

    # Get the string representation
    knot_hash = to_hexadecimal(dense_hash)
    return knot_hash


def get_knot_hash(s, numbers=list(range(256)), rounds=64, ext=[17,31,73,47,23]):
    lengths = get_lengths(s, True)
    lengths.extend(ext)
    return knot_hash(lengths, numbers, rounds)


def get_xor(a):
    ret = a[0]
    for e in a[1:]:
        ret = ret^e
    return ret


def to_hexadecimal(a):
    return "".join(["%02x" % e for e in a])


def test_get_lengths():
    assert get_lengths("1,2,3", False) == [1,2,3]
    assert get_lengths("1,2,3", True) == [49,44,50,44,51]


def test_to_hexadecimal():
    assert to_hexadecimal([64, 7, 255]) == "4007ff"


def test_knot():
    numbers = list(range(5))
    lengths = [3, 4, 1, 5]
    ret = knot(lengths, numbers)
    assert ret[0] == 12
    assert ret[2:] == (4,4)


def test_xor():
    a = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
    assert get_xor(a) == 64


def test_knot_hash():
    assert get_knot_hash("") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert get_knot_hash("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert get_knot_hash("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert get_knot_hash("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

def run_tests():
    test_get_lengths()
    test_xor()
    test_to_hexadecimal()
    test_knot()
    test_knot_hash()

# Main
if __name__=="__main__":

    run_tests()

    numbers = list(range(256))
    s = None
    with open("input.txt",'r') as f : s = f.readline().strip()

    lengths = get_lengths(s)

    print(knot(lengths, numbers)[0])
    print(get_knot_hash(s))


