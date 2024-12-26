#!/usr/bin/python3


# compute the distance between several pairs of nodes in the network


# Passed small local tests. But not the grader. Need optimization


import sys
import heapq
from typing import List, Set

maxlen = 2 * 10**6


class DistPreprocessSmall:
    def __init__(self, n: int, adj: List[List[List[int]]], cost: List[List[List[int]]]):
        self.n = n
        self.INFINITY = float("inf")
        self.adj = adj
        self.cost = cost
        self.dist = [self.INFINITY] * n
        self.visited = set()
        self.workset = []

    def clear(self):
        for v in self.workset:
            self.dist[v] = self.INFINITY
        self.visited.clear()
        self.workset.clear()

    def dijkstra(self, s: int, t: int) -> int:
        self.clear()
        self.dist[s] = 0
        h = [(0, s)]

        while h:
            d, u = heapq.heappop(h)
            if u == t:
                return d
            if u in self.visited:
                continue

            self.visited.add(u)
            self.workset.append(u)

            for i, v in enumerate(self.adj[0][u]):
                if v not in self.visited:
                    new_dist = d + self.cost[0][u][i]
                    if new_dist < self.dist[v]:
                        self.dist[v] = new_dist
                        heapq.heappush(h, (new_dist, v))

        return -1

    def query(self, s: int, t: int) -> int:
        if s == t:
            return 0
        return self.dijkstra(s, t)


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == "__main__":
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for _ in range(m):
        u, v, c = readl()
        adj[0][u - 1].append(v - 1)
        cost[0][u - 1].append(c)
        adj[1][v - 1].append(u - 1)
        cost[1][v - 1].append(c)

    ch = DistPreprocessSmall(n, adj, cost)
    print("Ready")
    sys.stdout.flush()
    (t,) = readl()
    for _ in range(t):
        s, t = readl()
        print(ch.query(s - 1, t - 1))
