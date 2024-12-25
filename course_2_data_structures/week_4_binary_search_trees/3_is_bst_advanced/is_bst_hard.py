# python3


# test whether a binary search tree data structure from some programming
# language library was impelemented correctly, allowed duplicates


import sys, threading

sys.setrecursionlimit(10**9)
threading.stack_size(2**29)


def is_bst_util(tree, node, min_key, max_key):
    if node == -1:
        return True
    key, left, right = tree[node]
    if not (min_key <= key <= max_key):
        return False
    return is_bst_util(tree, left, min_key, key - 1) and is_bst_util(
        tree, right, key, max_key
    )


def IsBinarySearchTree(tree):
    if not tree:
        return True
    return is_bst_util(tree, 0, float("-inf"), float("inf"))


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
