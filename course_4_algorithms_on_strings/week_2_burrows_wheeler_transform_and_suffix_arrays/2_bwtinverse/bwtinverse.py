# python3

"""

diff <(python3 bwtinverse.py < test/1) <(cat test/1.a)
diff <(python3 bwtinverse.py < test/2) <(cat test/2.a)

"""

import sys


def get_index_in_symbols(s):
    """map a character to an index based on the symbol."""
    if s == "A":
        return 0
    elif s == "C":
        return 1
    elif s == "G":
        return 2
    elif s == "T":
        return 3
    else:
        return 4


def get_index_in_right_column(sm, s, cnt):
    """calculate the index in the right column based on the symbol counts."""
    if s == "A":
        return cnt
    elif s == "C":
        return sm[0] + cnt
    elif s == "G":
        return sm[1] + sm[0] + cnt
    elif s == "T":
        return sm[2] + sm[1] + sm[0] + cnt
    else:
        return 0


def InverseBWT(bwt):
    if len(bwt) == 1:
        return bwt

    symbols = [0] * 5  # to store counts for a, c, g, t, $
    indexes = [0] * len(bwt)

    # count occurrences of each character
    for i, char in enumerate(bwt):
        indexes[i] = symbols[get_index_in_symbols(char)] + 1
        symbols[get_index_in_symbols(char)] += 1

    # prepare for reconstruction
    rsize = len(bwt)
    r = ["$"] * rsize

    s = bwt[0]
    j = indexes[0]
    k = rsize - 1

    r[k] = "$"
    r[k - 1] = s
    k -= 2

    # reconstruct the original string
    for _ in range(2, rsize):
        index_in_right_column = get_index_in_right_column(symbols, s, j)
        r[k] = bwt[index_in_right_column]
        j = indexes[index_in_right_column]
        s = r[k]
        k -= 1

    return "".join(r)


if __name__ == "__main__":
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
