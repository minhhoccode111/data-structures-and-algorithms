# python3

# use hashing to solve longest common substring problem in linear time


import sys
from collections import namedtuple

Answer = namedtuple("answer_type", "i j len")


class Solver:
    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.s_len = len(s)
        self.t_len = len(t)
        self.m1 = 1000000007
        self.m2 = 1000000009
        self.x = 263

    def _compute_hashes(self, string, length):
        h1 = [0] * (len(string) - length + 1)
        h2 = [0] * (len(string) - length + 1)
        x_power1 = pow(self.x, length, self.m1)
        x_power2 = pow(self.x, length, self.m2)

        current_hash1 = 0
        current_hash2 = 0
        for i in range(length):
            current_hash1 = (current_hash1 * self.x + ord(string[i])) % self.m1
            current_hash2 = (current_hash2 * self.x + ord(string[i])) % self.m2
        h1[0] = current_hash1
        h2[0] = current_hash2

        for i in range(1, len(string) - length + 1):
            current_hash1 = (
                (
                    current_hash1 * self.x
                    - ord(string[i - 1]) * x_power1
                    + ord(string[i + length - 1])
                )
                % self.m1
                + self.m1
            ) % self.m1
            current_hash2 = (
                (
                    current_hash2 * self.x
                    - ord(string[i - 1]) * x_power2
                    + ord(string[i + length - 1])
                )
                % self.m2
                + self.m2
            ) % self.m2
            h1[i] = current_hash1
            h2[i] = current_hash2
        return h1, h2

    def _check_length(self, length):
        if length == 0:
            return Answer(0, 0, 0)

        s_hashes1, s_hashes2 = self._compute_hashes(self.s, length)
        t_hashes1, t_hashes2 = self._compute_hashes(self.t, length)

        hash_dict = {}
        for i in range(len(s_hashes1)):
            hash_dict[(s_hashes1[i], s_hashes2[i])] = i

        for j in range(len(t_hashes1)):
            h = (t_hashes1[j], t_hashes2[j])
            if h in hash_dict:
                return Answer(hash_dict[h], j, length)
        return None

    def solve(self):
        left, right = 0, min(self.s_len, self.t_len) + 1
        last_valid = Answer(0, 0, 0)

        while left + 1 < right:
            mid = (left + right) // 2
            result = self._check_length(mid)

            if result is not None:
                left = mid
                last_valid = result
            else:
                right = mid

        return last_valid


def solve(s, t):
    solver = Solver(s, t)
    return solver.solve()


if __name__ == "__main__":
    for line in sys.stdin.readlines():
        s, t = line.split()
        ans = solve(s, t)
        print(ans.i, ans.j, ans.len)
