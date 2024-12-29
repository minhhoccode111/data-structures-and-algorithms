# python3


# performing genome assembly on a simulated error-prone sequencing dataset


from collections import defaultdict


class Assembler:
    L = 100
    E = 2

    def __init__(self, data):
        self.data = self._remove_duplicates(data)
        self.size = len(self.data)

    def _remove_duplicates(self, data):
        n = len(data)
        skip = [False] * n

        for i in range(n - 1):
            if skip[i]:
                continue
            s1 = data[i]
            for j in range(i + 1, n):
                if skip[j]:
                    continue
                if self._check_errors(s1, data[j]):
                    skip[j] = True

        return [data[i] for i in range(n) if not skip[i]]

    @staticmethod
    def _check_errors(s1, s2):
        errors = 0
        for i in range(Assembler.L):
            if s1[i] != s2[i]:
                errors += 1
            if errors > Assembler.E:
                return False
        return True

    def solve(self):
        processed = [False] * self.size
        overlap = [0] * self.size
        next_id = [0] * self.size

        i = 0
        for _ in range(self.size - 1):
            s1 = self.data[i]
            processed[i] = True
            for j in range(1, self.size):
                if processed[j]:
                    continue

                new_overlap = self._find_overlap(s1, self.data[j], overlap[i])
                if new_overlap is not None:
                    next_id[i] = j
                    overlap[i] = new_overlap

            i = next_id[i]

        next_id[i] = 0
        overlap[i] = self._find_overlap(self.data[i], self.data[0])
        last_overlap = overlap[i]

        pos = 0
        reads_pos = [(0, pos)]
        curr = 0
        for _ in range(self.size - 1):
            pos += Assembler.L - overlap[curr]
            reads_pos.append((next_id[curr], pos))
            curr = next_id[curr]

        str_len = pos + Assembler.L
        for _ in range(self.size - 1, self.size * 2):
            pos += Assembler.L - overlap[curr]
            reads_pos.append((next_id[curr], pos))
            curr = next_id[curr]

        result = []
        for i in range(str_len):
            counter = defaultdict(int)
            for read_id, start_pos in reads_pos:
                if start_pos <= i < (start_pos + Assembler.L):
                    counter[self.data[read_id][i - start_pos]] += 1

            max_count = 0
            max_char = ""
            for c, count in counter.items():
                if count > max_count:
                    max_char = c
                    max_count = count
            result.append(max_char)

        return "".join(result[last_overlap:])

    @staticmethod
    def _find_overlap(s1, s2, prev_overlap=0):
        for size in range(Assembler.L - 1, prev_overlap, -1):
            errors = 0
            start = Assembler.L - size
            for i in range(size):
                if s1[start + i] != s2[i]:
                    errors += 1
                    if errors > Assembler.E:
                        break
            else:
                return size
        return None


if __name__ == "__main__":
    data = [input().strip()]
    for _ in range(1617):
        data.append(input().strip())
    print(Assembler(data).solve())
