#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv

def op(s):
    if s == 'inc':
        return lambda x,y : x + y
    if s == 'dec':
        return lambda x,y : x - y
    if s == '>':
        return lambda x,y : x > y
    if s == '<':
        return lambda x,y : x < y
    if s == '>=':
        return lambda x,y : x >= y
    if s == '<=':
        return lambda x,y : x <= y
    if s == '==':
        return lambda x,y : x == y
    if s == '!=':
        return lambda x,y : x != y


# Main
if __name__=="__main__":

    registers = {}
    maxval = 0

    with open("input.txt", 'r') as f:
        for line in f:
            values = line.split()
            reg1, op1, val1 = values[:3]
            reg2, op2, val2 = values[4:]

            val1, val2 = map(int, (val1, val2))

#            print(reg1, op1, val1)
#            print(reg2, op2, val2)
#            quit()

            if reg1 not in registers.keys():
                registers[reg1] = 0
            if reg2 not in registers.keys():
                registers[reg2] = 0

            f2 = op(op2)
            if f2(registers[reg2], val2):
                f1 = op(op1)
                registers[reg1] = f1(registers[reg1], val1)

            if max(registers.values()) > maxval:
                maxval = max(registers.values())

    print(max(registers.values()))
    print(maxval)



