#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv
from math import ceil
import numpy as np
import time

largest_number = lambda x : 1 + 4*x*(x - 1)
level_of = lambda x : ceil((1 + x**0.5) / 2)
numbers_at = lambda x : 1 if x == 1 else 8*(x - 1)
corners = lambda l : [largest_number(l) - 2*(l-1)*i for i in range(4)]

def distance(x):
    if x == 1:
        return 1

    l = level_of(x)
    distance_to_level = l - 1
    distance_in_level = l - min([abs(x - c) for c in corners(l)])

    return distance_to_level + distance_in_level - 1


def pad_with_zeros(A):

    dtype = A.dtype

    right_vec = np.zeros((A.shape[0], 1), dtype=dtype)
    top_vec = np.zeros((1, A.shape[1] + 1), dtype=dtype)
    left_vec = np.zeros((A.shape[0] + 1, 1), dtype=dtype)
    bot_vec = np.zeros((1, A.shape[1] + 2), dtype=dtype)

    A = np.append(A, right_vec, axis=1)
    A = np.append(top_vec, A, axis=0)
    A = np.append(left_vec, A, axis=1)
    A = np.append(A, bot_vec, axis=0)
    return A


def first_larger_than(k):

    mat = np.ones((1, 1), dtype=np.int64)
    i = 0
    j = 0
    mat[j,i] = 1
    direction = [1, 0]

    while True:

        oob = j-1 < 0 or j > mat.shape[0] or i-1 < 0 or i > mat.shape[1]
        if oob:
            mat = pad_with_zeros(mat)
            i += 1
            j += 1

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

# Main
if __name__=="__main__":
    start = time.time()
    print(distance(361527))
    print(first_larger_than(361527))
    end = time.time()
    print("%f s." % (end - start))


