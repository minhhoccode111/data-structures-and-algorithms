# python3


# given a list of error-prone reads, two integers k and t, construct a de bruijn
# graph from the k-mers created from the reads and perform the task of bubble
# detection on this de bruijn graph with a path length threshold of t


from collections import defaultdict
import sys


class BubbleDetection:
    def __init__(self, k, threshold, reads):
        self.k = k
        self.threshold = threshold
        self.reads = reads
        self.visited_stack = None
        self.vertex_counts = None

    def find_bubbles(self):
        kmers = self._extract_kmers()
        k_minus_1_mers = self._get_k_minus_1_mers(kmers)

        vertex_count = len(k_minus_1_mers)
        graph_edges = self._build_de_bruijn_graph(kmers, k_minus_1_mers)
        adjacency_list = self._create_adjacency_list(vertex_count, graph_edges)

        bubble_count = 0
        for start_vertex in range(vertex_count):
            raw_paths = self._find_paths_with_threshold(start_vertex, adjacency_list)

            endpoint_paths = defaultdict(list)
            for path in raw_paths:
                endpoint_paths[path[-1]].append(path)

            for paths in endpoint_paths.values():
                if len(paths) <= 1:
                    continue

                bubble_count += self._count_valid_bubble_pairs(paths)

        return bubble_count

    def _find_paths_with_threshold(self, start_vertex, adjacency_list):
        if not self.vertex_counts:
            self.vertex_counts = [0] * len(adjacency_list)
        if not self.visited_stack:
            self.visited_stack = [False] * len(adjacency_list)

        paths = set()
        vertex_stack = [start_vertex]
        self.visited_stack[start_vertex] = True

        while vertex_stack:
            if len(vertex_stack) > 1:
                paths.add(tuple(vertex_stack))

            current_vertex = vertex_stack[-1]
            current_count = self.vertex_counts[current_vertex]

            if current_count < len(adjacency_list[current_vertex]):
                next_vertex = adjacency_list[current_vertex][current_count]
                self.vertex_counts[current_vertex] += 1

                if not self.visited_stack[next_vertex]:
                    vertex_stack.append(next_vertex)
                    self.visited_stack[next_vertex] = True
            else:
                self.vertex_counts[current_vertex] = 0
                self.visited_stack[current_vertex] = False
                vertex_stack.pop()

            if len(vertex_stack) == self.threshold + 1:
                paths.add(tuple(vertex_stack))
                last_vertex = vertex_stack.pop()
                self.visited_stack[last_vertex] = False
                self.vertex_counts[last_vertex] = 0

        return paths

    def _extract_kmers(self):
        kmers = set()
        for read in self.reads:
            read_str = "".join(read)
            for i in range(len(read_str) - self.k + 1):
                kmers.add(read_str[i : i + self.k])
        return tuple(kmers)

    def _get_k_minus_1_mers(self, kmers):
        k_minus_1_mers = set()
        for kmer in kmers:
            k_minus_1_mers.add(kmer[:-1])
            k_minus_1_mers.add(kmer[1:])
        return tuple(k_minus_1_mers)

    def _build_de_bruijn_graph(self, kmers, k_minus_1_mers):
        vertex_mapping = {kmer: idx for idx, kmer in enumerate(k_minus_1_mers)}
        edges = [
            (vertex_mapping[kmer[:-1]], vertex_mapping[kmer[1:]]) for kmer in kmers
        ]
        return tuple(edges)

    def _create_adjacency_list(self, vertex_count, edges):
        adjacency_list = [[] for _ in range(vertex_count)]
        for source, target in edges:
            adjacency_list[source].append(target)
        return adjacency_list

    def _count_valid_bubble_pairs(self, paths):
        bubble_count = 0
        for i in range(len(paths) - 1):
            path_i_internal = set(paths[i][1:-1])
            for j in range(i + 1, len(paths)):
                path_j_internal = set(paths[j][1:-1])
                if not path_i_internal.intersection(path_j_internal):
                    bubble_count += 1
        return bubble_count


def main():
    input_data = [line.strip() for line in sys.stdin if line.strip()]
    k, threshold = map(int, input_data[0].split())
    reads = input_data[1:]
    detector = BubbleDetection(k, threshold, reads)
    print(detector.find_bubbles())


if __name__ == "__main__":
    main()
