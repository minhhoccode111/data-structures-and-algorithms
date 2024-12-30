# python3


# given a list of error-prone reads, perform the task of genome assembly using
# de bruijn graphs and return the circular genome from which they came


from collections import deque, defaultdict


class EulerianCycle:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges
        self.m = len(self.edges)

    def find_path(self):
        if not self._cycle_exists():
            return None

        adj_list = [[] for _ in range(self.n)]
        for i, edge in enumerate(self.edges):
            v_start = edge[0]
            adj_list[v_start].append(i)

        m_explored = 0
        explored_edge = [False] * self.m
        prev_not_explored_v = 0
        cycles = []

        while m_explored < self.m:
            for i in range(prev_not_explored_v, self.n):
                if adj_list[i]:
                    edge_id = adj_list[i].pop()
                    explored_edge[edge_id] = True
                    m_explored += 1
                    prev_not_explored_v = i
                    break

            v_start, v_next = self.edges[edge_id]
            cycle = [v_start]
            while v_next != v_start:
                cycle.append(v_next)
                edge_id = adj_list[v_next].pop()
                explored_edge[edge_id] = True
                m_explored += 1
                v_next = self.edges[edge_id][1]
            cycles.append(cycle)

        cycles_sets = []
        for i, cycle in enumerate(cycles):
            cycles_sets.append(set(cycle))
            cycles[i] = deque(cycle)

        visited_cycles = [False] * len(cycles)
        path = []
        path_stack = deque(list(cycles[0]))
        visited_cycles[0] = True

        while path_stack:
            cur_v = path_stack.popleft()
            for i, cycle_set in enumerate(cycles_sets):
                if visited_cycles[i]:
                    continue
                if cur_v in cycle_set:
                    while cycles[i][-1] != cur_v:
                        cycles[i].rotate(1)
                    for v in reversed(cycles[i]):
                        path_stack.appendleft(v)
                    visited_cycles[i] = True
            path.append(cur_v)
        return path

    def _cycle_exists(self):
        in_degree = [0] * self.n
        out_degree = [0] * self.n
        for v1, v2 in self.edges:
            out_degree[v1] += 1
            in_degree[v2] += 1
        return all(d1 == d2 for d1, d2 in zip(in_degree, out_degree))


class GenomeAssembler:
    def __init__(self, reads):
        self.reads = reads
        self._adj_list_cnt = None
        self._in_stack = None

    def solve(self, k):
        k_mers = self._k_mers(k)
        k_min_1_mers = self._k_min_1_mers(k_mers)
        edges = self._de_bruijn_graph(k_mers, k_min_1_mers)
        edges = self._remove_bubbles(len(k_min_1_mers), edges, k_mers, k_min_1_mers)
        edges = self._remove_tips(len(k_min_1_mers), edges)
        k_min_1_mers, edges = self._shrink_graph(k_min_1_mers, edges)

        path = EulerianCycle(len(k_min_1_mers), edges).find_path()
        return self._construct_genome(k_min_1_mers, path) if path else None

    def _k_mers(self, k):
        k_mers = set()
        for read in self.reads:
            for i in range(len(read) - k + 1):
                k_mers.add(read[i : i + k])
        return tuple(k_mers)

    def _k_min_1_mers(self, k_mers):
        k_min_1_mers = set()
        for k_mer in k_mers:
            k_min_1_mers.add(k_mer[:-1])
            k_min_1_mers.add(k_mer[1:])
        return tuple(k_min_1_mers)

    def _k_mers_coverage(self, k_mers):
        k = len(k_mers[0])
        coverage_raw = defaultdict(int)
        for read in self.reads:
            for i in range(len(read) - k + 1):
                coverage_raw[read[i : i + k]] += 1
        return [coverage_raw[k_mer] for k_mer in k_mers]

    def _remove_bubbles(self, n, edges, k_mers, k_min_1_mers):
        k_mers_coverage = self._k_mers_coverage(k_mers)
        adj_list = self._edges_to_adj_list(n, edges)

        for v_start in range(n):
            paths_raw = self._dfs_threshold_paths(v_start, adj_list, len(k_mers[0]))
            paths = defaultdict(list)
            for path in paths_raw:
                paths[path[-1]].append(path)

            for paths_cur in paths.values():
                if len(paths_cur) <= 1:
                    continue

                bubble_pairs = []
                for i in range(len(paths_cur) - 1):
                    path_i_inner = set(paths_cur[i][1:-1])
                    for j in range(i + 1, len(paths_cur)):
                        path_j_inner = set(paths_cur[j][1:-1])
                        if len(path_i_inner.intersection(path_j_inner)) == 0:
                            bubble_pairs.append((i, j))

                path_removed = [False] * len(paths_cur)
                for p1, p2 in bubble_pairs:
                    if not path_removed[p1] and not path_removed[p2]:
                        path_1 = paths_cur[p1]
                        coverage_p1 = self._path_coverage(
                            path_1, k_mers, k_min_1_mers, k_mers_coverage
                        )
                        path_2 = paths_cur[p2]
                        coverage_p2 = self._path_coverage(
                            path_2, k_mers, k_min_1_mers, k_mers_coverage
                        )

                        if coverage_p1 < coverage_p2:
                            edges_to_del = {
                                (path_1[i], path_1[i + 1])
                                for i in range(len(path_1) - 1)
                            }
                            edges = [edge for edge in edges if edge not in edges_to_del]
                            path_removed[p1] = True
                        else:
                            edges_to_del = {
                                (path_2[i], path_2[i + 1])
                                for i in range(len(path_2) - 1)
                            }
                            edges = [edge for edge in edges if edge not in edges_to_del]
                            path_removed[p2] = True

                        adj_list = self._edges_to_adj_list(n, edges)
        return edges

    def _path_coverage(self, path, k_mers, k_min_1_mers, k_mers_coverage):
        coverage = 0
        for i in range(len(path) - 1):
            k_mer = k_min_1_mers[path[i]] + k_min_1_mers[path[i + 1]][-1]
            coverage += k_mers_coverage[k_mers.index(k_mer)]
        return coverage / (len(path) - 1)

    def _shrink_graph(self, k_min_1_mers, edges):
        k_min_1_mers_new = set()
        for v1, v2 in edges:
            k_min_1_mers_new.add(k_min_1_mers[v1])
            k_min_1_mers_new.add(k_min_1_mers[v2])

        new_mers = []
        old_to_new = [0] * len(k_min_1_mers)
        j = 0
        for i, mer in enumerate(k_min_1_mers):
            if mer in k_min_1_mers_new:
                new_mers.append(mer)
                old_to_new[i] = j
                j += 1

        new_edges = [(old_to_new[v1], old_to_new[v2]) for v1, v2 in edges]
        return tuple(new_mers), tuple(new_edges)

    def _remove_tips(self, n, edges):
        while True:
            adj_list, adj_list_r = self._edges_to_adj_lists(n, edges)
            edges_to_del = set()
            for i, (v1, v2) in enumerate(edges):
                if (len(adj_list[v2]) == 0) or (len(adj_list_r[v1]) == 0):
                    edges_to_del.add(i)
            if not edges_to_del:
                break
            edges = [edge for i, edge in enumerate(edges) if i not in edges_to_del]
        return edges

    def _edges_to_adj_list(self, n, edges):
        adj_list = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj_list[v1].append(v2)
        return adj_list

    def _edges_to_adj_lists(self, n, edges):
        adj_list = [[] for _ in range(n)]
        adj_list_r = [[] for _ in range(n)]
        for v1, v2 in edges:
            adj_list[v1].append(v2)
            adj_list_r[v2].append(v1)
        return adj_list, adj_list_r

    def _de_bruijn_graph(self, k_mers, k_min_1_mers):
        k_min_1_mer_to_id = {mer: i for i, mer in enumerate(k_min_1_mers)}
        edges = [
            (k_min_1_mer_to_id[k_mer[:-1]], k_min_1_mer_to_id[k_mer[1:]])
            for k_mer in k_mers
        ]
        return tuple(edges)

    def _dfs_threshold_paths(self, v_start, adj_list, threshold):
        if self._adj_list_cnt is None:
            self._adj_list_cnt = [0] * len(adj_list)
        if self._in_stack is None:
            self._in_stack = [False] * len(adj_list)

        paths = set()
        stack = [v_start]
        self._in_stack[v_start] = True

        while stack:
            if len(stack) > 1:
                paths.add(tuple(stack))

            v_last = stack[-1]
            adj_list_i = self._adj_list_cnt[v_last]
            while adj_list_i < len(adj_list[v_last]):
                v_next = adj_list[v_last][adj_list_i]
                adj_list_i += 1
                if not self._in_stack[v_next]:
                    self._adj_list_cnt[v_last] = adj_list_i
                    stack.append(v_next)
                    self._in_stack[v_next] = True
                    break
            else:
                stack.pop()
                self._in_stack[v_last] = False
                self._adj_list_cnt[v_last] = 0

            if len(stack) == (threshold + 1):
                paths.add(tuple(stack))
                v_last = stack.pop()
                self._in_stack[v_last] = False
                self._adj_list_cnt[v_last] = 0
        return paths

    def _construct_genome(self, k_min_1_mers, path):
        return "".join(k_min_1_mers[i][-1] for i in path)


def main():
    reads = tuple(input().strip() for _ in range(1618))
    print(GenomeAssembler(reads).solve(20))


if __name__ == "__main__":
    main()
