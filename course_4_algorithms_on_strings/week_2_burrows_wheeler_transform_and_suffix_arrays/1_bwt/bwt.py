# python3


import sys


def BWT(text):
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    rotations.sort()
    result = "".join(rotation[-1] for rotation in rotations)
    return result


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    print(BWT(text))
