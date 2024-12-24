# python3


# given a sequence a₁, ..., aₙ of integers and an integer m ≤ n, find the
# maximum among {aᵢ, ..., aᵢ₊ₘ₋₁} for every 1 ≤ i ≤ n - m + 1. A naive O(nm)
# algorithm for solving this problem scans each window separately. Your goal
# is to design an O(n) algorithm


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i : i + m]))

    return maximums


if __name__ == "__main__":
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
