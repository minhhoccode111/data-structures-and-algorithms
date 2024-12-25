# python3


# find all text locations where distance from pattern is sufficiently small

import sys


def polynomial_hash(s, start, length, x, p):
    ans = 0
    for i in range(length):
        ans = (ans * x + ord(s[start + i])) % p
    return ans


def precompute_hashes(text, pattern_len, x, p):
    H = [0] * (len(text) - pattern_len + 1)
    s = text[len(text) - pattern_len : len(text)]
    H[len(text) - pattern_len] = polynomial_hash(
        text, len(text) - pattern_len, pattern_len, x, p
    )
    y = 1
    for i in range(pattern_len):
        y = (y * x) % p
    for i in range(len(text) - pattern_len - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])) % p
    return H


def count_mismatches_binary(text, pattern, pos, k):
    count = 0
    left = 0
    right = len(pattern)

    while count <= k and left < right:
        if text[pos + left] != pattern[left]:
            count += 1
        left += 1

    return count


def solve(k, text, pattern):
    result = []
    x, p = 263, 1000000007

    if len(pattern) > len(text):
        return []

    pattern_hash = polynomial_hash(pattern, 0, len(pattern), x, p)
    H = precompute_hashes(text, len(pattern), x, p)

    for i in range(len(text) - len(pattern) + 1):
        if H[i] == pattern_hash:
            mismatches = count_mismatches_binary(text, pattern, i, k)
            if mismatches <= k:
                result.append(i)
        else:
            mismatches = count_mismatches_binary(text, pattern, i, k)
            if mismatches <= k:
                result.append(i)

    return result


lines = []
for line in sys.stdin.readlines():
    k, t, p = line.split()
    ans = solve(int(k), t, p)
    if ans:
        lines.append(f"{len(ans)} {' '.join(map(str, ans))}")
    else:
        lines.append("0")

print("\n".join(lines))
