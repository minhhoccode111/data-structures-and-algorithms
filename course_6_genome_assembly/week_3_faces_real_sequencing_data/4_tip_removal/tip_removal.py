# python3


# given a list of error-prone reads, construct a de bruijn graph from the
# 15-mers created from the reads and perform the task of tip removal on this de
# bruijn graph


import sys


class TipRemoval:
    def __init__(self, reads, k):
        self.reads = reads
        self.k = k

    def process_tips(self):
        kmers = self._extract_kmers()
        k_minus_1_mers = self._get_k_minus_1_mers(kmers)
        vertex_count = len(k_minus_1_mers)
        edges = self._build_de_bruijn_graph(kmers, k_minus_1_mers)

        return self._remove_tips(edges, vertex_count)

    def _remove_tips(self, edges, vertex_count):
        tip_count = 0

        while True:
            forward_adj, reverse_adj = self._create_adjacency_lists(vertex_count, edges)
            edges_to_remove = self._find_tip_edges(edges, forward_adj, reverse_adj)

            if not edges_to_remove:
                break

            tip_count += len(edges_to_remove)
            edges = [edge for i, edge in enumerate(edges) if i not in edges_to_remove]

        return tip_count

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

    def _create_adjacency_lists(self, vertex_count, edges):
        forward_adj = [[] for _ in range(vertex_count)]
        reverse_adj = [[] for _ in range(vertex_count)]

        for source, target in edges:
            forward_adj[source].append(target)
            reverse_adj[target].append(source)

        return forward_adj, reverse_adj

    def _find_tip_edges(self, edges, forward_adj, reverse_adj):
        tip_edges = set()
        for i, (v1, v2) in enumerate(edges):
            if not forward_adj[v2] or not reverse_adj[v1]:
                tip_edges.add(i)
        return tip_edges


def main():
    reads = []
    for line in sys.stdin:
        reads.append(line.strip())
    reads = tuple(reads)
    tip_detector = TipRemoval(reads, k=15)
    print(tip_detector.process_tips())


if __name__ == "__main__":
    main()
