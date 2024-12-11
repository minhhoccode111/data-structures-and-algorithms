import sys


"""

diff <(python3 trie_matching_extended.py < test/1) <(cat test/1.a)
diff <(python3 trie_matching_extended.py < test/2) <(cat test/2.a)

"""


NA = -1


class Node:
    def __init__(self):
        self.next = [NA] * 4
        self.patternEnd = False


def solve(text, n, patterns):
    result = []

    # write your code here

    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(" ".join(map(str, ans)) + "\n")
