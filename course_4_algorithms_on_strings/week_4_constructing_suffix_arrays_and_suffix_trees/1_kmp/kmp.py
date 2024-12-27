# python3


import sys


def compute_prefix_function(p):
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
