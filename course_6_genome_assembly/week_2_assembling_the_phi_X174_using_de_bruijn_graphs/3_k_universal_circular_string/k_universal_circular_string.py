# python3


# given an integer k, find a circular binary string that contains all possible
# binary strings of length k as substrings


from collections import deque, defaultdict


class EulerianCycle:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.m = len(edges)

    def find_path(self):
        if not self.cycle_exists():
            return None

        adj_list = [[] for _ in range(self.n)]
        for i, edge in enumerate(self.edges):
            adj_list[edge[0]].append(i)

        m_explored = 0
        explored = [False] * self.m
        prev_unexplored = 0
        cycles = []

        while m_explored < self.m:
            for i in range(prev_unexplored, self.n):
                if adj_list[i]:
                    edge_id = adj_list[i].pop()
                    explored[edge_id] = True
                    m_explored += 1
                    prev_unexplored = i
                    break

            start, next_v = self.edges[edge_id]
            cycle = [start, next_v]
            while next_v != start:
                edge_id = adj_list[next_v].pop()
                explored[edge_id] = True
                m_explored += 1
                next_v = self.edges[edge_id][1]
                cycle.append(next_v)
            cycles.append(cycle)

        cycle_map = defaultdict(list)
        for i, cycle in enumerate(cycles):
            cycle_map[cycle[0]].append(i)

        path = []
        stack = deque([cycles[0][0]])

        while stack:
            current = stack.popleft()
            if current in cycle_map and cycle_map[current]:
                cycle_id = cycle_map[current].pop()
                for v in reversed(cycles[cycle_id][1:]):
                    stack.appendleft(v)
            path.append(current)
        return path

    def cycle_exists(self):
        in_degree = [0] * self.n
        out_degree = [0] * self.n

        for v1, v2 in self.edges:
            out_degree[v1] += 1
            in_degree[v2] += 1

        for d1, d2 in zip(in_degree, out_degree):
            if d1 != d2:
                return False
        return True


class KUniCircStr:
    def __init__(self, k):
        self.k = k

    def solve(self):
        k_mers = [format(i, "0{}b".format(self.k)) for i in range(2**self.k)]
        k_minus_1_mers = [
            format(i, "0{}b".format(self.k - 1)) for i in range(2 ** (self.k - 1))
        ]

        edges = self.de_bruijn_graph(k_mers, k_minus_1_mers)
        ec = EulerianCycle(len(k_minus_1_mers), edges)
        path = ec.find_path()

        sequence = [k_minus_1_mers[path[0]][-1:]]
        for i in path[1:-1]:
            sequence.append(k_minus_1_mers[i][-1:])
        return "".join(sequence)

    def de_bruijn_graph(self, k_mers, k_minus_1_mers):
        index_map = {mer: idx for idx, mer in enumerate(k_minus_1_mers)}
        edges = {(index_map[mer[:-1]], index_map[mer[1:]]) for mer in k_mers}
        return tuple(edges)


def main():
    k = int(input())
    result = KUniCircStr(k).solve()
    print(result)


if __name__ == "__main__":
    main()
