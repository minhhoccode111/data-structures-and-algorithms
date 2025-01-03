# python3


# find all occurrences of a collection of pattern in a text and will be able to
# handle cases when one of the patterns is a prefix of another pattern

# python3
import sys


class Node:
    def __init__(self):
        self.next = [None] * 4
        self.patternEnd = False


def char_to_index(char):
    if char == "A":
        return 0
    elif char == "C":
        return 1
    elif char == "G":
        return 2
    elif char == "T":
        return 3
    return -1


def build_trie(patterns):
    root = Node()
    for pattern in patterns:
        current = root
        for char in pattern:
            index = char_to_index(char)
            if current.next[index] is None:
                current.next[index] = Node()
            current = current.next[index]
        current.patternEnd = True
    return root


def find_patterns(text, index, root):
    current = root
    i = index
    while i < len(text):
        char_index = char_to_index(text[i])
        if char_index == -1 or current.next[char_index] is None:
            break
        current = current.next[char_index]
        if current.patternEnd:
            return True
        i += 1
    return False


def solve(text, n, patterns):
    result = set()
    trie = build_trie(patterns)
    for i in range(len(text)):
        if find_patterns(text, i, trie):
            result.add(i)
    return sorted(list(result))


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]
ans = solve(text, n, patterns)
sys.stdout.write(" ".join(map(str, ans)) + "\n")
