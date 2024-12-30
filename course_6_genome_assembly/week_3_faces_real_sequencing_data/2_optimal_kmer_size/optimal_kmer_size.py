# python3


# given a set of error-free dna reads, find the optimal k-mer size that produces
# a de bruijn graph with a single eulerian cycle


import sys


class DeBruijnGraphAnalyzer:
    def __init__(self, sequences):
        self.dna_sequences = sequences

    def find_optimal_k(self):
        left_bound = 3
        right_bound = len(self.dna_sequences[0])

        while left_bound <= right_bound:
            current_k = (left_bound + right_bound) // 2

            kmer_collection = set()
            for sequence in self.dna_sequences:
                sequence_str = "".join(sequence)
                for pos in range(len(sequence) - current_k + 1):
                    kmer_collection.add(sequence_str[pos : (pos + current_k)])
            kmer_collection = tuple(kmer_collection)

            submer_collection = set()
            for kmer in kmer_collection:
                submer_collection.add(kmer[:-1])
                submer_collection.add(kmer[1:])
            submer_collection = tuple(submer_collection)

            graph_edges = self.construct_graph(kmer_collection, submer_collection)

            if not self.has_eulerian_cycle(len(submer_collection), graph_edges):
                right_bound = current_k - 1
            else:
                left_bound = current_k + 1

        return right_bound

    @staticmethod
    def construct_graph(kmers, submers):
        vertex_mapping = {}
        for vertex_id, submer in enumerate(submers):
            vertex_mapping[submer] = vertex_id

        edge_list = []
        for kmer in kmers:
            start_vertex = vertex_mapping[kmer[:-1]]
            end_vertex = vertex_mapping[kmer[1:]]
            edge_list.append((start_vertex, end_vertex))

        return tuple(edge_list)

    @staticmethod
    def has_eulerian_cycle(vertex_count, edge_list):
        incoming_edges = [0] * vertex_count
        outgoing_edges = [0] * vertex_count

        for start, end in edge_list:
            outgoing_edges[start] += 1
            incoming_edges[end] += 1

        for in_deg, out_deg in zip(incoming_edges, outgoing_edges):
            if in_deg != out_deg:
                return False
        return True


def main():
    dna_sequences = [line.strip() for line in sys.stdin if line.strip()]
    dna_sequences = tuple(dna_sequences)
    analyzer = DeBruijnGraphAnalyzer(dna_sequences)
    result = analyzer.find_optimal_k()
    print(result)


if __name__ == "__main__":
    main()
