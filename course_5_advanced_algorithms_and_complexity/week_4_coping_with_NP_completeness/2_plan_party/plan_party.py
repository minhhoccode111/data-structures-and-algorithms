# python3


#  planning a company party and want to invite the coolest people (with assigned
# "fun factors"). To avoid awkwardness, you can't invite both an employee and
# their direct boss. Find the maximum total fun factor of a party under this
# constraint


import sys
import threading


sys.setrecursionlimit(10**6)
threading.stack_size(2**26)


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree


def funParty(vertex, parent):
    global D
    if D[vertex] == 10**9:
        if tree[vertex].children == [parent]:
            D[vertex] = tree[vertex].weight
        else:
            m = tree[vertex].weight
            for u in tree[vertex].children:
                if u != parent:
                    for w in tree[u].children:
                        if D[w] != 10**9:
                            m += D[w]
            m2 = 0
            for u in tree[vertex].children:
                if u != parent:
                    m2 += D[u]
            D[vertex] = max(m, m2)
    return D[vertex]


def dfs(tree, vertex, parent):
    global visited
    visited[vertex] = True
    for child in tree[vertex].children:
        if not visited[child] and child != parent:
            dfs(tree, child, vertex)
    funParty(vertex, parent)


def MaxWeightIndependentTreeSubset(tree):
    dfs(tree, 0, -1)
    return D[0]


def main():
    weight = MaxWeightIndependentTreeSubset(tree)
    print(weight)


tree = ReadTree()
size = len(tree)
D = [10**9 for i in range(size)]
visited = [False for i in range(size)]
threading.Thread(target=main).start()
