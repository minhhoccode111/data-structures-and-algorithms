# python3


# given an directed graph with possibly negative edge weights and with n vertices
# and m edges check whether it contains a negative cycle


import sys
import math


def negative_cycle(adj, cost):
    n = len(adj)
    dist = [math.inf] * n

    for start in range(n):
        dist[start] = 0
        for _ in range(n):
            updated = False
            for u in range(n):
                for idx, v in enumerate(adj[u]):
                    if dist[u] + cost[u][idx] < dist[v]:
                        dist[v] = dist[u] + cost[u][idx]
                        updated = True
            if not updated:
                break

        for u in range(n):
            for idx, v in enumerate(adj[u]):
                if dist[u] + cost[u][idx] < dist[v]:
                    return 1

        dist = [math.inf] * n  # Reset for the next starting point

    return 0


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
    print(negative_cycle(adj, cost))
