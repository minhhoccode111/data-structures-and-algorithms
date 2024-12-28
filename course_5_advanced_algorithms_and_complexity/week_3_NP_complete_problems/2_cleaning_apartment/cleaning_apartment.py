# python3


# this is a hamiltonian path problem where you need to find a route that visits
# each vertex (room) exactly once


import itertools


def varnum(i, j):
    return i + (j - 1) * n


def exactly_one_of(literals):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])


def printEquisatisfiableSatFormula():
    print(len(clauses), n * n)
    for i in clauses:
        for j in range(len(i)):
            print(i[j], end=" ")
        print(0)


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b)
        adj[b - 1].append(a)
    clauses = []
    digits = range(1, n + 1)
    for i in range(n):
        exactly_one_of([varnum(i + 1, j) for j in digits])
    for j in range(n):
        exactly_one_of([varnum(i, j + 1) for i in digits])
    listOfNonAdj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n - 1):
            clauses.append([-varnum(j + 1, i + 1)] + [varnum(j + 2, z) for z in adj[i]])
    printEquisatisfiableSatFormula()
