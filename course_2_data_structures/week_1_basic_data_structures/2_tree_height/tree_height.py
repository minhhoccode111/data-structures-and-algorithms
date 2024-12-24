# python3

# read a description of tree from the input, implement the tree data structure,
# store the tree and compute its height


import sys
import threading


def compute_height(n, parents):
    tree = [[] for _ in range(n)]
    root = None

    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            tree[parent].append(i)

    def dfs(node):
        if not tree[node]:
            return 1
        return 1 + max(dfs(child) for child in tree[node])

    return dfs(root)


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()
