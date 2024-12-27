# python3


# construct a trie from a collection of patterns

import sys


def build_trie(patterns):
    tree = {0: {}}
    node_count = 1

    for pattern in patterns:
        current = 0
        for c in pattern:
            if c in tree[current]:
                current = tree[current][c]
            else:
                tree[current][c] = node_count
                tree[node_count] = {}
                current = node_count
                node_count += 1
    return tree


if __name__ == "__main__":
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
