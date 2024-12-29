# python3


# given a directed graph, find and output an eulerian cycle (a path that visits
# every edge exactly once) if one exists, or output 0 if not


from collections import deque, defaultdict


class EulerianCycle:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.m = len(self.edges)

    def find_path(self):
        if not self.cycle_exists():
            return None

        adj_list = [[] for _ in range(self.n)]
        for i, edge in enumerate(self.edges):
            adj_list[edge[0]].append(i)

        m_explored = 0
        explored_edge = [False] * self.m
        prev_unexplored = 0
        cycles = []

        while m_explored < self.m:
            for i in range(prev_unexplored, self.n):
                if adj_list[i]:
                    edge_id = adj_list[i].pop()
                    explored_edge[edge_id] = True
                    m_explored += 1
                    prev_unexplored = i
                    break

            v_start, v_next = self.edges[edge_id]
            cycle = [v_start, v_next]
            while v_next != v_start:
                edge_id = adj_list[v_next].pop()
                explored_edge[edge_id] = True
                m_explored += 1
                v_next = self.edges[edge_id][1]
                cycle.append(v_next)
            cycles.append(cycle)

        cycle_starts = defaultdict(list)
        for i, cycle in enumerate(cycles):
            cycle_starts[cycle[0]].append(i)

        path = []
        stack = deque([cycles[0][0]])

        while stack:
            cur_v = stack.popleft()
            if cur_v in cycle_starts and cycle_starts[cur_v]:
                cycle_id = cycle_starts[cur_v].pop()
                for v in cycles[cycle_id][1:][::-1]:
                    stack.appendleft(v)
            path.append(cur_v)
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


def main():
    num_vertices, num_edges = map(int, input().split())
    edges = [
        (int(v1) - 1, int(v2) - 1)
        for _ in range(num_edges)
        for v1, v2 in [input().split()]
    ]

    ec = EulerianCycle(num_vertices, edges)
    path = ec.find_path()

    if path is None:
        print(0)
    else:
        print(1)
        print(" ".join(map(lambda x: str(x + 1), path[:-1])))


if __name__ == "__main__":
    main()
