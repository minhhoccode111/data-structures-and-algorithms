# python3


# given a sequence a₁, ..., aₙ of integers and an integer m ≤ n, find the
# maximum among {aᵢ, ..., aᵢ₊ₘ₋₁} for every 1 ≤ i ≤ n - m + 1. A naive O(nm)
# algorithm for solving this problem scans each window separately. Your goal
# is to design an O(n) algorithm


from collections import deque


def max_sliding_window(sequence, m):
    result = []
    window = deque()

    for i in range(m):
        while window and sequence[window[-1]] <= sequence[i]:
            window.pop()
        window.append(i)

    for i in range(m, len(sequence)):
        result.append(sequence[window[0]])

        while window and window[0] <= i - m:
            window.popleft()

        while window and sequence[window[-1]] <= sequence[i]:
            window.pop()

        window.append(i)

    if window:
        result.append(sequence[window[0]])

    return result


if __name__ == "__main__":
    n = int(input())
    sequence = [int(i) for i in input().split()]
    assert len(sequence) == n
    m = int(input())
    print(*max_sliding_window(sequence, m))
