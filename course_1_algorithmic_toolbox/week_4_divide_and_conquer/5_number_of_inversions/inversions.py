# python3

# compute the number of inversions in a sequence of integers


# helper function to merge and count at the same time
def merge_and_count(left, right):
    # list to store merged elements
    merged = []
    # inversions count
    inversions = 0
    # 2 starting pointers
    i, j = 0, 0

    # loop through 2 lists to merge them
    while i < len(left) and j < len(right):
        # if current of left less that current of right
        if left[i] <= right[j]:
            # add left[i] to merged list
            merged.append(left[i])
            # increase i pointer
            i += 1
        else:
            # add right[j] to merged list
            merged.append(right[j])
            # if left[i] > right[j], then all remaining elements in left
            # starting from i form inversions with right[j]
            inversions += len(left) - i
            # increase j pointer
            j += 1

    # add remaining elements
    # no matter which one remains, we add both from the last index (when exist
    # the while loop), make sure the remaining elements are added in the correct
    # order
    merged.extend(left[i:])
    merged.extend(right[j:])

    # return the merged list and number of inversions
    return merged, inversions


def sort_and_count_inversions(arr):
    # base case of merge sort
    if len(arr) <= 1:
        return arr, 0

    # divide list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # recursively sort and count inversions in left and right halves
    left, left_inversions = sort_and_count_inversions(left)
    right, right_inversions = sort_and_count_inversions(right)

    # merge the sorted halves and count split inversions
    merged, split_inversions = merge_and_count(left, right)

    # the total inversions will be left + right + split
    total_inversions = left_inversions + right_inversions + split_inversions
    # return the merged list first, then the total count of inversions
    return merged, total_inversions


if __name__ == "__main__":
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    # ignore the first output
    _, inversions = sort_and_count_inversions(elements)
    print(inversions)
