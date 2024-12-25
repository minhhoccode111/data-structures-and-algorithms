# python3


# Given an undirected graph with n vertices and m edges, compute the number of
# connected components in it


import sys


def explore(adj, visited, v):
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            explore(adj, visited, w)


def number_of_components(adj):
    result = 0
    n = len(adj)
    visited = [False] * n

    for v in range(n):
        if not visited[v]:
            explore(adj, visited, v)
            result += 1

    return result


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
    print(number_of_components(adj))
