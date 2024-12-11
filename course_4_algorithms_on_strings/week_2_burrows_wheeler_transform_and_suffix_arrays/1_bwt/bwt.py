import sys


"""

diff <(python3 bwt.py < test/1) <(cat test/1.a)
diff <(python3 bwt.py < test/2) <(cat test/2.a)

"""


import sys


def BWT(text):
    # Generate all rotations of the text
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    # Sort the rotations lexicographically
    rotations.sort()
    # Construct the result by taking the last character of each rotation
    result = "".join(rotation[-1] for rotation in rotations)
    return result


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    print(BWT(text))

