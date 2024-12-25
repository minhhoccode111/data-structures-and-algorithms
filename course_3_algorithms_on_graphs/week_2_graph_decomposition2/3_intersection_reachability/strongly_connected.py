# python3


# compute the number of strongly connected components of a given directed graph
# with 'n' vertices and 'm' edges


import sys

sys.setrecursionlimit(200000)


def dfs(adj, used, order, x):
    used[x] = True
    for v in adj[x]:
        if not used[v]:
            dfs(adj, used, order, v)
    order.append(x)


def explore(adj, used, x):
    used[x] = True
    for v in adj[x]:
        if not used[v]:
            explore(adj, used, v)


def reverse_graph(adj):
    rev_adj = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for j in adj[i]:
            rev_adj[j].append(i)
    return rev_adj


def number_of_strongly_connected_components(adj):
    result = 0
    used = [False] * len(adj)
    order = []

    for v in range(len(adj)):
        if not used[v]:
            dfs(adj, used, order, v)

    rev_adj = reverse_graph(adj)
    used = [False] * len(adj)

    for v in reversed(order):
        if not used[v]:
            explore(rev_adj, used, v)
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
    print(number_of_strongly_connected_components(adj))
