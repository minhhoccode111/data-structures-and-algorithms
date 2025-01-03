# python3


# find all text locations where distance from pattern is sufficiently small


import sys
from functools import lru_cache


class Solver:
    multiplier = 1234
    prime = 1000000009

    def __init__(self, text, pattern, num_mismatches):
        self.t = text
        self.p = pattern
        self.k = num_mismatches
        self.len_ = len(self.p)

        self.hashes_t = self._precompute_hashes(self.t, self.prime)
        self.hashes_p = self._precompute_hashes(self.p, self.prime)

    def _precompute_hashes(self, string, prime):
        hashes = [0 for _ in range(len(string) + 1)]
        for i in range(1, len(string) + 1):
            hashes[i] = (self.multiplier * hashes[i - 1] + ord(string[i - 1])) % prime
        return hashes

    @staticmethod
    def _modular_exponentitation(a, b, n):
        d = 1
        b = str(bin(b))[2:]
        for i in range(len(b)):
            d = (d * d) % n
            if int(b[i]) == 1:
                d = (d * a) % n
        return d

    @lru_cache(maxsize=1024 * 4)
    def _calc_substring_hash(self, hash_type, prime, start, length):
        if hash_type == "t":
            hashes = self.hashes_t
        else:
            hashes = self.hashes_p

        y = self._modular_exponentitation(self.multiplier, length, prime)
        substring_hash = (hashes[start + length] - y * hashes[start]) % prime
        return substring_hash

    def solve(self):
        res = []

        for i in range(len(self.t) - self.len_ + 1):
            k_i = 0
            a = i
            base_b = i + self.len_ - 1
            b = base_b
            while k_i <= self.k:
                mismatch = -1
                while a <= b:
                    mid = (a + b) // 2

                    t_s_hash = self._calc_substring_hash(
                        "t", self.prime, a, mid - a + 1
                    )
                    p_s_hash = self._calc_substring_hash(
                        "p", self.prime, a - i, mid - a + 1
                    )

                    if t_s_hash == p_s_hash:
                        a = mid + 1
                    else:
                        mismatch = mid
                        b = mid - 1

                if mismatch != -1:
                    k_i += 1
                    a = mismatch + 1
                    b = base_b
                else:
                    res.append(i)
                    break
        return res

    def solve_naive(self):
        res = []

        for i in range(len(self.t) - self.len_ + 1):
            mismatches = 0
            for j in range(self.len_):
                if self.t[i + j] != self.p[j]:
                    mismatches += 1

            if mismatches > self.k:
                continue
            res.append(i)

        return res


def main():
    for line in sys.stdin.readlines():
        num_mismatches, text, pattern = line.split()
        ans = Solver(text, pattern, int(num_mismatches)).solve()
        print(len(ans), *ans)


if __name__ == "__main__":
    main()
