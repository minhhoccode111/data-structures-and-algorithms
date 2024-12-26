# python3

# given an undirected graph with n vertices and m edges check whether it is bipartite

import sys
import queue


def bipartite(adj):
    n = len(adj)
    colors = [-1] * n

    for start in range(n):
        if colors[start] == -1:
            colors[start] = 0
            q = queue.Queue()
            q.put(start)

            while not q.empty():
                u = q.get()
                for v in adj[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        q.put(v)
                    elif colors[v] == colors[u]:
                        return 0
    return 1


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
