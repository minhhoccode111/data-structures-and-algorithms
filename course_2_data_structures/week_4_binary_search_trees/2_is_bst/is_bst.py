#!/usr/bin/env python3


# test whether a binary search tree data structure from some programming
# language library was impelemented correctly

import sys, threading

# increase those if the submission send signal 11
sys.setrecursionlimit(10**9)  # max depth of recursion
threading.stack_size(2**29)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    def is_bst(node, min_key, max_key):
        if node == -1:
            return True
        key, left, right = tree[node]
        if not (min_key < key < max_key):
            return False
        return is_bst(left, min_key, key) and is_bst(right, key, max_key)

    if not tree:
        return True
    return is_bst(0, float("-inf"), float("inf"))


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
