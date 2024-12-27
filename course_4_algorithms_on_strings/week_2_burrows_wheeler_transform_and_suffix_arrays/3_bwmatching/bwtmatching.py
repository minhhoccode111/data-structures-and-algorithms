# python3


# construct the Burrows-Wheeler Transform of a string


import sys


def PreprocessBWT(bwt):
    chars = set(bwt)
    starts = {char: 0 for char in chars}
    occ_count_before = {char: [0] * (len(bwt) + 1) for char in chars}

    sorted_chars = sorted(list(bwt))
    for i, char in enumerate(sorted_chars):
        if i == 0 or char != sorted_chars[i - 1]:
            starts[char] = i

    for i, char in enumerate(bwt):
        for c in chars:
            occ_count_before[c][i + 1] = occ_count_before[c][i]
        occ_count_before[char][i + 1] += 1

    return starts, occ_count_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    top = 0
    bottom = len(bwt) - 1

    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]

            if symbol not in starts:
                return 0

            matches_before_top = (
                occ_counts_before[symbol][top] if symbol in occ_counts_before else 0
            )
            matches_before_bottom = (
                occ_counts_before[symbol][bottom + 1]
                if symbol in occ_counts_before
                else 0
            )

            if matches_before_bottom > matches_before_top:
                top = starts[symbol] + matches_before_top
                bottom = starts[symbol] + matches_before_bottom - 1
            else:
                return 0
        else:
            return bottom - top + 1

    return 0


if __name__ == "__main__":
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()

    starts, occ_counts_before = PreprocessBWT(bwt)
    occurrence_counts = []

    for pattern in patterns:
        occurrence_counts.append(
            CountOccurrences(pattern, bwt, starts, occ_counts_before)
        )

    print(" ".join(map(str, occurrence_counts)))
