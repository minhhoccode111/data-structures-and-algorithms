# python3


# given a directed graph with possibly negative edge weights and with n vertices
# and m edges as well as its vertex s compute the length of the shortest path
# from s to all other vertices of the graph


import sys
import queue


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)
    distance[s] = 0
    reachable[s] = 1

    for _ in range(n - 1):
        for u in range(n):
            for i, v in enumerate(adj[u]):
                if distance[u] != 10**19 and distance[v] > distance[u] + cost[u][i]:
                    distance[v] = distance[u] + cost[u][i]
                    reachable[v] = 1

    negative_cycle = set()
    for _ in range(n):
        for u in range(n):
            for i, v in enumerate(adj[u]):
                if distance[u] != 10**19 and distance[v] > distance[u] + cost[u][i]:
                    distance[v] = distance[u] + cost[u][i]
                    negative_cycle.add(v)
                    shortest[v] = 0

    if negative_cycle:
        q = queue.Queue()
        for v in negative_cycle:
            q.put(v)
            shortest[v] = 0

        while not q.empty():
            u = q.get()
            for v in adj[u]:
                if shortest[v] == 1:
                    shortest[v] = 0
                    q.put(v)


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print("*")
        elif shortest[x] == 0:
            print("-")
        else:
            print(distance[x])
