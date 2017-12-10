#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Author: Akke Viitanen

# Imports
from sys import argv

# A node has the following parts
# (name, weight, parent, children, weight)


def read_input(fname):
    programs = {}
    with open(fname, 'r') as f:
        for line in f:
            elements = line.split()

            name = elements[0]
            weight = int(elements[1][1:len(elements[1])-1])
            children = None
            if len(elements) > 2:
                # Avoid the "->" sign and read the rest of the children
                children = []
                for child in elements[3:]:
                    children.append(child.replace(',',''))
            programs[name] = [name, weight, None, children, None]
    return programs


def find_parents(programs):
    for k, v in programs.items():
        # Case: no children
        if v[3] is None:
            continue

        # Assign this parent to all of the children
        for child in v[3]:
            programs[child][2] = k
    return programs


def find_root(programs):
    for k, v in programs.items():
        # If no parent is found, then this is the root
        if v[2] is None:
            return k
    return None


def get_tree(programs, root):

    tree = programs[root]


    if tree[3] is not None:
        children = [get_tree(programs, c) for c in tree[3]]
        tree[3] = children
    return tree


def get_weight(tree):

    if tree[3] is None:
        return tree[1]

    s = sum([get_weight(c) for c in tree[3]])
    return tree[1] + s


def set_weights(tree):

    tree[4] = get_weight(tree)
    if tree[3] is not None:
        for c in tree[3]:
            c = set_weights(c)
    return tree


def get_at_depth(programs, program, depth):

    get = []
    if depth == 0:
        get.append(programs[program])

    if programs[program][3] is not None:
        for child in programs[program][3]:
            get.append(get_at_depth(programs, child, depth-1))
    return get



def find_inbalance(tree, ref=None):

    if tree[3] is None:
        return tree[1]

    children = tree[3]
    weights = [c[4] for c in children]

    # If children are balanced, this one must be inbalanced
    if len(set(weights)) == 1:
        return tree[1] - abs((tree[4] - ref[4]))

    # Find the one that differs
    children.sort(key=lambda k : k[4])

    # Take note of the reference value
    ref = diff = None
    if children[0][4] == children[1][4]:
        ref = children[0]
        diff = children[-1]
    else:
        ref = children[-1]
        diff = children[0]

    # Find the inbalance there
    return find_inbalance(diff, ref)


def circus(fname):
    programs = read_input(fname)
    programs = find_parents(programs)

    root = find_root(programs)
    tree = get_tree(programs, root)
    tree = set_weights(tree)
    print(root)
    print(find_inbalance(tree))


# Main
if __name__=="__main__":
    circus("test_input.txt")
    circus("input.txt")
