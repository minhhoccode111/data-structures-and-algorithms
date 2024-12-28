# python3


# design a single layer of an integrated circuit with modules and connections. wires can only bend once, either left or right. determine the bending direction for each wire to avoid intersections


import sys
import threading

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
n, m = map(int, input().split())
clauses = [list(map(int, input().split())) for i in range(m)]
count = 0


def isSatisfiable():
    global count

    def dfs1(i):
        visited[i] = True
        for j in gV[i]:
            if not visited[j]:
                dfs1(j)
        postvisit.append(i)

    def dfs2(x):
        global count
        CCS[x] = count
        for j in gReverseV[x]:
            if CCS[j] == -1:
                dfs2(j)

    g = []
    for i in clauses:
        g.append([-i[0], i[1]])
        g.append([-i[1], i[0]])
    lst = list(range(-n, 0)) + list(range(1, n + 1))
    gReverseEdges = []
    gReverseV = {i: [] for i in lst}
    gV = {i: [] for i in lst}
    for i in g:
        gReverseEdges.append([i[1], i[0]])
    for i in gReverseEdges:
        gReverseV[i[0]] += [i[1]]
    gV = {i: [] for i in lst}
    for i in g:
        gV[i[0]] += [i[1]]
    CCS = {i: -1 for i in lst}
    postvisit = []
    visited = {i: False for i in lst}
    for i in lst:
        if not visited[i]:
            dfs1(i)
    postvisit.reverse()
    for i in postvisit:
        if CCS[i] == -1:
            dfs2(i)
            count += 1
    for i in range(1, n + 1):
        if CCS[i] == CCS[-i]:
            return
    result = {i: -1 for i in lst}
    for i in postvisit:
        if result[i] == -1:
            result[i] = 1
            result[-i] = 0
    return result


def main():
    result = isSatisfiable()
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        for i in range(1, n + 1):
            if result.get(i) == 1:
                print(-i, end=" ")
            else:
                print(i, end=" ")


threading.Thread(target=main).start()
