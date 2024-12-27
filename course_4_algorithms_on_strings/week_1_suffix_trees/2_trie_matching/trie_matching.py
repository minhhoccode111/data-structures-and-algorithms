# python3


# find all occurrences of a collection of pattern in a text

import sys

NA = -1


class Node:
    def __init__(self):
        self.next = [NA] * 4
        self.is_pattern_end = False


def char_to_index(char):
    if char == "A":
        return 0
    elif char == "C":
        return 1
    elif char == "G":
        return 2
    elif char == "T":
        return 3
    return NA


def build_trie(patterns):
    root = Node()
    for pattern in patterns:
        current = root
        for char in pattern:
            index = char_to_index(char)
            if current.next[index] == NA:
                current.next[index] = Node()
            current = current.next[index]
        current.is_pattern_end = True
    return root


def find_pattern(text, index, root, pattern_length):
    current = root
    for i in range(index, min(index + pattern_length, len(text))):
        char_index = char_to_index(text[i])
        if char_index == NA or current.next[char_index] == NA:
            return False
        current = current.next[char_index]
        if current.is_pattern_end:
            return True
    return False


def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    max_pattern_length = max(len(p) for p in patterns)
    for i in range(len(text)):
        if find_pattern(text, i, trie, max_pattern_length):
            result.append(i)
    return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]
ans = solve(text, n, patterns)
sys.stdout.write(" ".join(map(str, ans)) + "\n")
