#!/usr/bin/python3


# compute the distance between several pairs of nodes in the network


import sys
import queue


class BiDij:
    def __init__(self, n):
        self.n = n
        self.inf = n * 10**6
        self.d = [[self.inf] * n, [self.inf] * n]
        self.visited = [False] * n
        self.workset = []

    def clear(self):
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visited[v] = False
        del self.workset[0 : len(self.workset)]

    def visit(self, q, side, v, dist):
        if self.d[side][v] > dist:
            self.d[side][v] = dist
            q[side].put((dist, v))
            self.workset.append(v)

    def query(self, adj, cost, s, t):
        self.clear()
        if s == t:
            return 0

        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.visit(q, 0, s, 0)
        self.visit(q, 1, t, 0)

        proc = [set(), set()]

        while not q[0].empty() or not q[1].empty():
            for side in [0, 1]:
                if q[side].empty():
                    continue

                dist, u = q[side].get()
                if u in proc[side]:
                    continue

                proc[side].add(u)

                if u in proc[1 - side]:
                    shortest = self.inf
                    for u_proc in self.workset:
                        candidate = self.d[0][u_proc] + self.d[1][u_proc]
                        shortest = min(shortest, candidate)
                    return shortest if shortest != self.inf else -1

                for v_idx, v in enumerate(adj[side][u]):
                    if v not in proc[side]:
                        self.visit(q, side, v, dist + cost[side][u][v_idx])

        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == "__main__":
    n, m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u, v, c = readl()
        adj[0][u - 1].append(v - 1)
        cost[0][u - 1].append(c)
        adj[1][v - 1].append(u - 1)
        cost[1][v - 1].append(c)
    (t,) = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s - 1, t - 1))
