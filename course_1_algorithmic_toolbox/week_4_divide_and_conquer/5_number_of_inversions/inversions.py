# python3

# compute the number of inversions in a sequence of integers


def merge_and_count(left, right):
    merged = []
    inversions = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            inversions += len(left) - i
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, inversions


def sort_and_count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left, left_inversions = sort_and_count_inversions(left)
    right, right_inversions = sort_and_count_inversions(right)

    merged, split_inversions = merge_and_count(left, right)

    total_inversions = left_inversions + right_inversions + split_inversions
    return merged, total_inversions


if __name__ == "__main__":
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    _, inversions = sort_and_count_inversions(elements)
    print(inversions)
