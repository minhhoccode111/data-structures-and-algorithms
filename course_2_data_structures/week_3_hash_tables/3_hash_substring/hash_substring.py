# python3


# implement the Rabin-Karp's algorithm


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(" ".join(map(str, output)))


def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans


def precompute_hashes(text, pattern_len, prime, x):
    H = [0] * (len(text) - pattern_len + 1)
    S = text[len(text) - pattern_len :]
    H[len(text) - pattern_len] = poly_hash(S, prime, x)
    y = 1
    for i in range(pattern_len):
        y = (y * x) % prime
    for i in range(len(text) - pattern_len - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])) % prime
    return H


def get_occurrences(pattern, text):
    p = 1000000007
    x = 263
    result = []
    pattern_hash = poly_hash(pattern, p, x)
    H = precompute_hashes(text, len(pattern), p, x)

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == H[i]:
            if text[i : i + len(pattern)] == pattern:
                result.append(i)
    return result


if __name__ == "__main__":
    print_occurrences(get_occurrences(*read_input()))
