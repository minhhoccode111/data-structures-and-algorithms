# python3


import sys

ALPHABET_SIZE = 5


def get_index(c):
    if c == "A":
        return 1
    elif c == "C":
        return 2
    elif c == "G":
        return 3
    elif c == "T":
        return 4
    else:
        return 0


def counting_characters_sort(s):
    order = [0] * len(s)
    count = [0] * ALPHABET_SIZE

    for c in s:
        count[get_index(c)] += 1

    for j in range(1, ALPHABET_SIZE):
        count[j] += count[j - 1]

    for i in range(len(s) - 1, -1, -1):
        c = s[i]
        count[get_index(c)] -= 1
        order[count[get_index(c)]] = i

    return order


def compute_character_classes(s, order):
    cclass = [0] * len(s)

    for i in range(1, len(s)):
        if s[order[i]] != s[order[i - 1]]:
            cclass[order[i]] = cclass[order[i - 1]] + 1
        else:
            cclass[order[i]] = cclass[order[i - 1]]

    return cclass


def sort_doubled(s, L, order, cclass):
    count = [0] * len(s)
    new_order = [0] * len(s)

    for cl in cclass:
        count[cl] += 1

    for j in range(1, len(s)):
        count[j] += count[j - 1]

    for i in range(len(s) - 1, -1, -1):
        start = (order[i] - L + len(s)) % len(s)
        cl = cclass[start]
        count[cl] -= 1
        new_order[count[cl]] = start

    return new_order


def update_classes(new_order, cclass, L):
    n = len(new_order)
    new_cclass = [0] * n

    for i in range(1, n):
        cur, prev = new_order[i], new_order[i - 1]
        mid, mid_prev = (cur + L) % n, (prev + L) % n

        if cclass[cur] != cclass[prev] or cclass[mid] != cclass[mid_prev]:
            new_cclass[cur] = new_cclass[prev] + 1
        else:
            new_cclass[cur] = new_cclass[prev]

    return new_cclass


def build_suffix_array(text):
    order = counting_characters_sort(text)
    cclass = compute_character_classes(text, order)
    L = 1

    while L < len(text):
        order = sort_doubled(text, L, order, cclass)
        cclass = update_classes(order, cclass, L)
        L *= 2

    return order


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
