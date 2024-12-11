# python3
import sys

"""

diff <(python3 kmp.py < test/1) <(cat test/1.a)
diff <(python3 kmp.py < test/2) <(cat test/2.a)
diff <(python3 kmp.py < test/3) <(cat test/3.a)

"""


import sys


def compute_prefix_function(p):
    """compute the prefix function for the pattern."""
    s = [0] * len(p)
    border = 0

    for j in range(1, len(p)):
        while border > 0 and p[j] != p[border]:
            border = s[border - 1]
        if p[j] == p[border]:
            border += 1
        else:
            border = 0
        s[j] = border

    return s


def find_pattern(pattern, text):
    """find all occurrences of the pattern in the text."""
    S = pattern + "$" + text
    s = compute_prefix_function(S)
    result = []

    for i in range(len(pattern) + 1, len(S)):
        if s[i] == len(pattern):
            result.append(i - 2 * len(pattern))

    return result


if __name__ == "__main__":
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))
