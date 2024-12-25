# python3


# check if there is a path between x and y

import sys


def reach(adj, x, y):
    visited = [False] * len(adj)
    stack = [x]
    visited[x] = True

    while stack:
        vertex = stack.pop()
        if vertex == y:
            return 1

        for neighbor in adj[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    x, y = data[2 * m :]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
