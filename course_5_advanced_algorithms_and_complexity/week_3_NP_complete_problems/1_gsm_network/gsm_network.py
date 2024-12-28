# python3


# this is a graph coloring problem where you need to color vertices (towers)
# with 3 colors (frequencies) so that no connected vertices share the same color


import itertools


def varnum(i, j):
    return i + (j - 1) * n


def exactly_one_of(literals):
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])


def printEquisatisfiableSatFormula():
    print(n * 4 + m * 3, n * 3)
    for i in clauses:
        for j in range(len(i)):
            print(i[j], end=" ")
        print(0)


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    clauses = []
    digits = range(1, 4)
    for i in range(n):
        exactly_one_of([varnum(i + 1, j) for j in digits])
    for j in edges:
        for r in digits:
            clauses.append([-varnum(j[0], r), -varnum(j[1], r)])
    printEquisatisfiableSatFormula()
