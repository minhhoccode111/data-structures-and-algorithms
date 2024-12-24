# python3


# convert an array of integers into a heap


def sift_down(data, i, size, swaps):
    min_index = i
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    if left < size and data[left] < data[min_index]:
        min_index = left

    if right < size and data[right] < data[min_index]:
        min_index = right

    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]

        sift_down(data, min_index, size, swaps)


def build_heap(data):
    """
    Build a min heap from an array inplace.
    Returns a sequence of swaps performed by the algorithm.
    """
    n = len(data)
    swaps = []

    for i in range(n // 2 - 1, -1, -1):
        sift_down(data, i, n, swaps)

    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))

    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
