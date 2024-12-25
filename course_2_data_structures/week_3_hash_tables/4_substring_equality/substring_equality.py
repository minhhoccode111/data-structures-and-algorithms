# python3


# use hashing to design an algorithm that is able to preprocess a given string
# 's' to answer any query of the form 'are those two substrings of s equal?'
# efficiently


class Solver:
    def __init__(self, s):
        self.s = s
        self.m1 = 1000000007
        self.m2 = 1000000009
        self.x = 263
        self.len_s = len(s)
        self.h1 = [0] * (self.len_s + 1)
        self.h2 = [0] * (self.len_s + 1)
        self._precompute_hashes()

    def _precompute_hashes(self):
        for i in range(1, self.len_s + 1):
            self.h1[i] = (self.x * self.h1[i - 1] + ord(self.s[i - 1])) % self.m1
            self.h2[i] = (self.x * self.h2[i - 1] + ord(self.s[i - 1])) % self.m2

    def _get_hash(self, h, start, length, m):
        y = pow(self.x, length, m)
        hash_value = (h[start + length] - y * h[start]) % m
        return hash_value

    def ask(self, a, b, l):
        hash1_a = self._get_hash(self.h1, a, l, self.m1)
        hash1_b = self._get_hash(self.h1, b, l, self.m1)
        hash2_a = self._get_hash(self.h2, a, l, self.m2)
        hash2_b = self._get_hash(self.h2, b, l, self.m2)
        return hash1_a == hash1_b and hash2_a == hash2_b


if __name__ == "__main__":
    s = input().rstrip()
    q = int(input())
    solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, input().split())
        print("Yes" if solver.ask(a, b, l) else "No")
