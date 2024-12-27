# python3


# construct a suffix array of a string


import sys


def build_suffix_array(text):
    suffixes = []
    for i in range(len(text)):
        suffixes.append((text[i:], i))

    suffixes.sort()
    result = []
    for suffix, index in suffixes:
        result.append(index)

    return result


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
