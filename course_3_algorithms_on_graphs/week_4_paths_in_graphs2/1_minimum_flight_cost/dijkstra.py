# python3


# Given an directed graph with positive edge weights and with n vertices and m
# edges as well as two vertices u and v, compute the weight of a shortest path
# between u and v (that is, the minimum total weight of a path from u to v)

import sys
import queue


def distance(adj, cost, s, t):
    dist = [float("inf")] * len(adj)
    dist[s] = 0
    pq = queue.PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        _, u = pq.get()

        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                pq.put((dist[v], v))

    return dist[t] if dist[t] != float("inf") else -1


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0 : (3 * m) : 3], data[1 : (3 * m) : 3]), data[2 : (3 * m) : 3])
    )
    data = data[3 * m :]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for (a, b), w in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
