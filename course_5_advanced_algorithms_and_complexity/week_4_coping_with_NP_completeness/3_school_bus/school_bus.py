# python3


# determine the fastest route for a school bux to start from the depot, vist all
# the children's homes, get them to school and return back to depot


from itertools import permutations, combinations
from collections import defaultdict
import random
import sys


class TSP:
    INF = 10**12

    def __init__(self, graph):
        self.graph = graph
        self.n = len(self.graph)

    def optimal_path_dp(self):
        shortest_path_len = dict()

        shortest_path_len[(1, 0)] = 0

        set_size_to_k = defaultdict(list)
        for k in range(1, 2**self.n):
            k_bin = format(k, "b")

            if k_bin[-1] != "1":
                continue

            count_one = 0
            for i in k_bin:
                if i == "1":
                    count_one += 1
            set_size_to_k[count_one].append(k)

        for k in set_size_to_k[2]:
            i = 0
            k_bin = format(k, "b")
            for j, c in enumerate(reversed(k_bin[:-1])):
                if c == "1":
                    i = j + 1
                    break

            shortest_path_len[(k, i)] = self.graph[0][i]

        for set_size in range(3, self.n + 1):
            for k in set_size_to_k[set_size]:
                shortest_path_len[(k, 0)] = TSP.INF
                cur_set_min_len = TSP.INF
                k_bin = format(k, "b")

                for i, c1 in enumerate(reversed(k_bin)):
                    if (i == 0) or (c1 == "0"):
                        continue

                    shortest_path_len[(k, i)] = TSP.INF

                    for j, c2 in enumerate(reversed(k_bin)):
                        if (j == i) or (j == 0) or (c2 == "0"):
                            continue

                        k_wo_i = k ^ (1 << i)

                        cur_len = shortest_path_len[(k, i)]
                        new_len = shortest_path_len[(k_wo_i, j)] + self.graph[i][j]
                        if new_len < cur_len:
                            shortest_path_len[(k, i)] = new_len

                            if new_len < cur_set_min_len:
                                cur_set_min_len = new_len

        path_len = TSP.INF
        k = set_size_to_k[self.n][0]
        last_i = None
        for i in range(1, self.n):
            new_len = shortest_path_len[(k, i)] + self.graph[i][0]
            if new_len < path_len:
                path_len = new_len
                last_i = i

        if path_len == TSP.INF:
            path_len = -1
            path = []
            return path_len, path

        path = [1, last_i + 1]
        k = set_size_to_k[self.n][0] ^ (1 << last_i)
        cur_len = shortest_path_len[(set_size_to_k[self.n][0], last_i)]
        cur_size = self.n - 1
        while k != 1:
            k_bin = format(k, "b")
            for i, c in enumerate(reversed(k_bin)):
                if (i == 0) or (c == "0"):
                    continue
                new_len = shortest_path_len[(k, i)] + self.graph[i][last_i]
                if new_len == cur_len:
                    cur_len = shortest_path_len[(k, i)]
                    k = k ^ (1 << i)
                    last_i = i
                    path.append(i + 1)
                    break
        path.append(1)
        return path_len, path

    def optimal_path_dp_naive(self):
        shortest_path_len = dict()

        shortest_path_len[((1,), 1)] = 0

        for cur_set in combinations(range(1, self.n + 1), 2):
            if cur_set[0] != 1:
                continue
            shortest_path_len[(cur_set, cur_set[1])] = self.graph[1 - 1][cur_set[1] - 1]

        for set_size in range(3, self.n + 1):
            for cur_set in combinations(range(1, self.n + 1), set_size):
                if cur_set[0] != 1:
                    continue

                shortest_path_len[(cur_set, 1)] = TSP.INF

                cur_set_min_len = TSP.INF

                for i in cur_set:
                    if i == 1:
                        continue

                    shortest_path_len[(cur_set, i)] = TSP.INF

                    for j in cur_set[1:]:
                        if j == i:
                            continue

                        cur_set_wo_i = []
                        for k in cur_set:
                            if k != i:
                                cur_set_wo_i.append(k)
                        cur_set_wo_i = tuple(cur_set_wo_i)

                        cur_len = shortest_path_len[(cur_set, i)]
                        new_len = (
                            shortest_path_len[(cur_set_wo_i, j)]
                            + self.graph[i - 1][j - 1]
                        )
                        if new_len < cur_len:
                            shortest_path_len[(cur_set, i)] = new_len

                            if new_len < cur_set_min_len:
                                cur_set_min_len = new_len

        final_path_len = TSP.INF
        prev_set = [i for i in range(1, self.n + 1)]
        final_set = prev_set.copy()
        final_set.append(1)
        prev_set = tuple(prev_set)
        final_set = tuple(final_set)
        for j in range(2, self.n):
            cur_len = final_path_len
            new_len = shortest_path_len[(prev_set, j)] + self.graph[j - 1][1 - 1]
            if new_len < cur_len:
                final_path_len = new_len

        if final_path_len == TSP.INF:
            final_path_len = -1
            path = []
            return final_path_len, path

        path = []
        return final_path_len, path

    def optimal_path_brute_force(self):
        n = len(self.graph)
        best_ans = TSP.INF
        best_path = []

        for p in permutations(range(n)):
            cur_sum = 0
            for i in range(1, n):
                if self.graph[p[i - 1]][p[i]] == TSP.INF:
                    break
                cur_sum += self.graph[p[i - 1]][p[i]]
            else:
                if self.graph[p[-1]][p[0]] == TSP.INF:
                    continue
                cur_sum += self.graph[p[-1]][p[0]]
                if cur_sum < best_ans:
                    best_ans = cur_sum
                    best_path = list(p)

        if best_ans == TSP.INF:
            return -1, []
        return best_ans, [x + 1 for x in best_path]


def stress_test():
    n_vertices = 4
    max_n_edges = int(n_vertices * (n_vertices - 1) / 2)
    max_weight = 5

    i = 0
    while True:
        print(i)

        n_edges = random.randint(1, max_n_edges)
        graph = [[TSP.INF] * n_vertices for _ in range(n_vertices)]
        for _ in range(n_edges):
            u = random.choice(range(n_vertices))
            other = list(range(n_vertices))
            other.remove(u)
            v = random.choice(other)
            graph[u][v] = graph[v][u] = random.randint(1, max_weight)

        tsp = TSP(graph)
        path_len1, path1 = tsp.optimal_path_brute_force()
        path_len2, path2 = tsp.optimal_path_dp()

        if path_len1 != path_len2:
            for row in tsp.graph:
                print(row)
            break

        if path1 != path2[:-1]:
            for row in tsp.graph:
                print(row)
            break

        i += 1


def main():
    lines = sys.stdin.readlines()
    if not lines:
        return
    n_vertices, n_edges = map(int, lines[0].split())
    graph = [[TSP.INF] * n_vertices for _ in range(n_vertices)]
    for i in range(n_edges):
        if i + 1 >= len(lines):
            return
        u_, v_, weight = map(int, lines[i + 1].split())
        u, v = u_ - 1, v_ - 1
        graph[u][v] = graph[v][u] = weight
    tsp = TSP(graph)
    path_len, path = tsp.optimal_path_dp()
    print(path_len)
    if path_len == -1:
        return
    print(" ".join(map(str, path[:-1])))


if __name__ == "__main__":
    main()
