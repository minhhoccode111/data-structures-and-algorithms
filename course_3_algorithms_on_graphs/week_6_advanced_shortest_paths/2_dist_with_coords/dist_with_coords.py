#!/usr/bin/python3


# compute the distance between several pairs of nodes in the network


import sys
import queue
import math


class AStar:
    def __init__(self, n, adj, cost, x, y):
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n * 10**6
        self.d = [self.inf] * n
        self.visited = [False] * n
        self.workset = []
        self.x = x
        self.y = y
        self.p = [None] * n

    def clear(self):
        for v in self.workset:
            self.d[v] = self.inf
            self.visited[v] = False
            self.p[v] = None
        del self.workset[0 : len(self.workset)]

    def potential(self, u, t):
        return math.sqrt((self.x[u] - self.x[t]) ** 2 + (self.y[u] - self.y[t]) ** 2)

    def visit(self, q, p, v, dist, t):
        if self.d[v] > dist:
            self.d[v] = dist
            q.put((dist + self.potential(v, t), v))
            self.workset.append(v)

    def query(self, s, t):
        self.clear()
        if s == t:
            return 0

        q = queue.PriorityQueue()
        self.visit(q, 0, s, 0, t)

        while not q.empty():
            _, u = q.get()

            if u == t:
                return self.d[t]

            if self.visited[u]:
                continue

            self.visited[u] = True

            for v, w in zip(self.adj[u], self.cost[u]):
                if not self.visited[v]:
                    potential_dist = self.d[u] + w
                    if potential_dist < self.d[v]:
                        self.d[v] = potential_dist
                        self.p[v] = u
                        q.put((potential_dist + self.potential(v, t), v))
                        self.workset.append(v)

        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == "__main__":
    n, m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u, v, c = readl()
        adj[u - 1].append(v - 1)
        cost[u - 1].append(c)
    (t,) = readl()
    astar = AStar(n, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        print(astar.query(s - 1, t - 1))
