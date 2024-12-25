# python3

# implement Rope - data structure that can store a string and efficiently cut a
# part (a substring) of this string and insert it in a different position

import sys


class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        substr = self.s[i : j + 1]
        remaining = self.s[:i] + self.s[j + 1 :]
        if k == 0:
            self.s = substr + remaining
        else:
            self.s = remaining[:k] + substr + remaining[k:]


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
