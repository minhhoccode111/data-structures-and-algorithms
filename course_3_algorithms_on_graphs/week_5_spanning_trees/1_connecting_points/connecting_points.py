# python3


# given n points on a plane, connect them with segments of minimum total length
# such that there is a path between any two points. Recall that the length of a
# segment with endpoints (x1, y1) and (x2, y2) is equal to
# sqrt((x1 - x2)^2 + (y1 - y2)^2)


import sys
import math


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.rank[i_id] > self.rank[j_id]:
            self.parent[j_id] = i_id
        else:
            self.parent[i_id] = j_id
            if self.rank[i_id] == self.rank[j_id]:
                self.rank[j_id] += 1


def minimum_distance(x, y):
    n = len(x)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            distance = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            edges.append((distance, i, j))

    edges.sort()
    result = 0.0
    union_find = UnionFind(n)

    for weight, u, v in edges:
        if union_find.find(u) != union_find.find(v):
            result += weight
            union_find.union(u, v)

    return result


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
