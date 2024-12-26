# python3


# given *n* points on a plane and an integer *k*, compute the largest possible
# value of *d* such that the given points can be partitioned into *k* non-empty
# subsets in such a way that the distance between any two points from different
# subsets is at least *d*

import sys
import math


def clustering(x, y, k):
    n = len(x)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            edges.append((dist, i, j))
    edges.sort()

    parent = list(range(n))
    rank = [0] * n

    def find(v):
        if v != parent[v]:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v
                if rank[root_u] == rank[root_v]:
                    rank[root_v] += 1

    num_clusters = n
    for dist, u, v in edges:
        if find(u) != find(v):
            if num_clusters == k:
                return dist
            union(u, v)
            num_clusters -= 1

    return -1.0


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0 : 2 * n : 2]
    y = data[1 : 2 * n : 2]
    data = data[2 * n :]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
