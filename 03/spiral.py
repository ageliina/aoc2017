#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv
from math import log2

# Assume level k
# Number of adjacent blocks on level k - 1 : [1, 3] 
# Number of adjacent blocks on level k     : [2, 3]
# Number of adjacent blocks on level k + 1 : [3, 5]

# Naming convention:
# corner: 5 adjacent blocks on k+1 : distance from closest quartile = max
# edge:   3 adjacent blocks on k   : distance from closest quartile = max - 1
# middle: 3 adjacent blocks on k-1 : anything else

# level     numbers
#     0     1
#     1     4 * 2
#     2     4 * 4
#     3     4 * 6
#     4     4 * 8
#     n     4 * 2*n

# First number in level 
#     0      1 = 0 + 1 = 1
#     1      2 = 1 + 1 = 2 = 2 + 0*8
#     2     10 = 1 + 1 + 8 = 2 + 1*8
#     3     26 = 1 + 1 + 8 + 16 = 2 + 3*8
#     4     50 = 1 + 1 + 8 + 16 + 24 = 2 + 6*8
#     5     82 = 1 + 1 + 8 + 16 + 24 + 32 = 2 + 10*8
# level = k + 8 * (k**2 - k) // 2 + 1
# 4*k**2 + k/2 + 1 = level
# 4*k**2 + k/2 + 1 - level = 0

# 1
# 2 3 4 5 6 7 8 9
# 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
# 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49

for i in range(1, 25):
    print("%5d %5d" % (i, int(log2(i // 4 + 1))))
quit()

def first_number_in_level(k):
    if k == 0:
        return 1
    else:
        fact = (k**2 - k) // 2
        return k + 8*fact + 1

def is_on_level(number, level):
    return first_number_in_level(level) <= number and number < first_number_in_level(level+1)

print(is_on_level(5, 2))
quit()

class memory:
    def __init__(self, number):
        self.number = number
        self.level = _level_from_number(number)

    def _level_from_number(self):
        ret = 0
        while k >= first_number_in_level(ret + 1):
            ret += 1
        return ret

print(memory(5))
quit()

def distance_in_level(k):

    level_of_k = level_of_number(k)
    first_number = first_number_in_level(level_of_k)
    quartiles = [first_number + i * 2*level_of_k for i in range(4)]
    distances = [abs(k - q) for q in quartiles]
    return min(distances)


def distance_to_number(k):
    level_of_k = level_of_number(k)
    return level_of_k + distance_in_level(k)


def test_distance_to_number():
    assert distance_to_number(1) == 0
    assert distance_to_number(12) == 3
    assert distance_to_number(23) == 2
    assert distance_to_number(1024) == 31


def get_adjacent_numbers(k):
    print(distance_in_level(k))
get_adjacent_numbers(5)
quit()


def first_larger_than(k):
    level_of_k = level_of_number(k)

    mat = np.ones((1, 1), dtype=int)
    i = 0
    j = 0
    mat[j,i] = 1
    direction = [1, 0]

    while True:

        oob = j-1 < 0 or j > shape[0] or i-1 < 0 or i > shape[1]
        if oob:

            vec = np.zeros((mat.shape[1], 1))
            mat = np.append(mat, vec, axis=1)
            print(vec.shape, mat.shape)

            vec = np.zeros((1, mat.shape[0]))
            print(vec.shape, mat.shape)
            mat = np.append(vec.T, mat, axis=0)

            vec = np.zeros((mat.shape[0], 1))
            mat = np.append(vec, mat, axis=1)
            print(vec.shape, mat.shape)

            vec = np.zeros((1, mat.shape[1]))
            mat = np.append(mat, vec.T, axis=0)
            print(vec.shape, mat.shape)

        # UPDATE DIRECTION
        # If right 
        if direction[0] == 1 and mat[j-1,i] == 0:
            # Go up
            direction[0] = 0
            direction[1] = 1
        # If up
        elif direction[1] == 1 and mat[j,i-1] == 0:
            # Go left
            direction[0] = -1
            direction[1] = 0
        # If left
        elif direction[0] == -1 and mat[j+1,i] == 0:
            # Go down
            direction[0] = 0
            direction[1] = -1
        # If down
        elif direction[1] == -1 and mat[j,i+1] == 0:
            # Go right
            direction[0] = 1
            direction[1] = 0

        mat[j,i] = np.sum(mat[j-1:j+2,i-1:i+2])
        if mat[j,i] > k:
            return mat[j,i]

        # UPDATE COORDINATE
        i += direction[0]
        j -= direction[1]



print(first_larger_than(361527))
quit()

# Main
if __name__=="__main__":
    test_distance_to_number()
    print(distance_to_number(361527))


