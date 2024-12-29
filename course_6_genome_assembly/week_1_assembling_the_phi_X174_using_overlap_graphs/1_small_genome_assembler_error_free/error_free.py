# python3


# performing genome assembly on a simulated error-free sequencing dataset


class Assembler:
    READ_LENGTH = 100

    def __init__(self, sequences):
        self.sequences = sequences
        self.size = len(sequences)

    def process(self):
        edges = [(0, None) for _ in range(self.size)]

        for i in range(self.size - 1):
            seq1 = self.sequences[i]
            for j in range(i + 1, self.size):
                seq2 = self.sequences[j]
                curr_overlap_i, _ = edges[i]
                curr_overlap_j, _ = edges[j]

                new_overlap_i = self._get_max_overlap(seq1, seq2, curr_overlap_i)
                new_overlap_j = self._get_max_overlap(seq2, seq1, curr_overlap_j)

                if new_overlap_i:
                    edges[i] = (new_overlap_i, j)
                if new_overlap_j:
                    edges[j] = (new_overlap_j, i)

        result = [self.sequences[0]]
        overlap, current = edges[0]

        while current != 0:
            result.append(self.sequences[current][overlap:])
            overlap, current = edges[current]

        genome = "".join(result)
        return genome[:-overlap]

    @staticmethod
    def _get_max_overlap(s1, s2, current_overlap):
        for size in range(Assembler.READ_LENGTH - 1, current_overlap, -1):
            if s2.startswith(s1[Assembler.READ_LENGTH - size :]):
                return size
        return None


if __name__ == "__main__":
    data = [input().strip()]
    for _ in range(1617):
        data.append(input().strip())
    print(Assembler(data).process())
