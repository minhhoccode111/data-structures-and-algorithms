#!/usr/bin/python3


# compute the length of the shortest path starting in the depot, visiting each
# store at least once and returning to the depot

# Passed small local tests. But not the grader. Need optimization


import sys
import queue
from itertools import combinations, permutations

maxlen = 2 * 10**6
INF = 10**9


class DistPreprocessLarge:
    def __init__(self, n, adj, cost):
        self.n = n
        self.INFINITY = n * maxlen
        self.adj = adj
        self.cost = cost
        self.bidistance = [[self.INFINITY] * n, [self.INFINITY] * n]
        self.visited = [False] * n  # Fixed: Initialize visited array properly
        self.visited_vertices = []  # Renamed for clarity
        self.q = queue.PriorityQueue()
        self.level = [0] * n
        self.rank = [0] * n

    def mark_visited(self, x):
        if not self.visited[x]:
            self.visited[x] = True
            self.visited_vertices.append(x)

    def add_arc(self, u, v, c):
        def update(adj, cost, u, v, c):
            for i in range(len(adj[u])):
                if adj[u][i] == v:
                    cost[u][i] = min(cost[u][i], c)
                    return
            adj[u].append(v)
            cost[u].append(c)

        update(self.adj[0], self.cost[0], u, v, c)
        update(self.adj[1], self.cost[1], v, u, c)

    def shortcut(self, v):
        shortcut_count = len(self.adj[0][v]) * len(self.adj[1][v])
        neighbors = len(self.adj[0][v]) + len(self.adj[1][v])
        shortcuts = []

        for u in self.adj[1][v]:
            for w in self.adj[0][v]:
                if u != w:
                    uv_cost = self.cost[1][self.adj[1][v].index(u)]
                    vw_cost = self.cost[0][self.adj[0][v].index(w)]
                    shortcuts.append((u, w, uv_cost + vw_cost))

        importance = shortcut_count + neighbors + len(shortcuts) + self.level[v]
        return importance, shortcuts, self.level[v]

    def clear(self):
        for v in self.visited_vertices:
            self.bidistance[0][v] = self.bidistance[1][v] = self.INFINITY
            self.visited[v] = False
        self.visited_vertices.clear()
        while not self.q.empty():
            self.q.get()

    def visit(self, side, v, dist):
        if self.bidistance[side][v] > dist:
            self.q.put((dist, v))
            self.bidistance[side][v] = dist
            self.mark_visited(v)

    def query(self, s, t):
        self.clear()
        self.visit(0, s, 0)

        while not self.q.empty():
            dist, v = self.q.get()
            if v == t:
                return dist

            for i, u in enumerate(self.adj[0][v]):
                if not self.visited[u]:
                    self.visit(0, u, dist + self.cost[0][v][i])

        return -1


def make_graph(ch, vertices):
    n = next(vertices)
    vertices = list(vertices)
    assert n == len(vertices)
    graph = [[INF] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            l = ch.query(vertices[i] - 1, vertices[j] - 1)
            graph[i][j] = l if l != -1 else INF
    return graph


def optimal_path(graph):
    n = len(graph)
    if n <= 1:
        return 0

    dp = {}
    all_vertices = (1 << n) - 1

    def solve(mask, pos):
        if mask == all_vertices:
            return graph[pos][0] if graph[pos][0] != INF else INF

        state = (mask, pos)
        if state in dp:
            return dp[state]

        ans = INF
        for next_pos in range(n):
            if (mask & (1 << next_pos)) == 0 and graph[pos][next_pos] != INF:
                result = solve(mask | (1 << next_pos), next_pos)
                if result != INF:
                    ans = min(ans, graph[pos][next_pos] + result)

        dp[state] = ans
        return ans

    result = solve(1, 0)
    return result if result != INF else -1


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

    ch = DistPreprocessLarge(n, adj, cost)
    print("Ready")
    sys.stdout.flush()

    (t,) = readl()
    for i in range(t):
        print(optimal_path(make_graph(ch, readl())))
