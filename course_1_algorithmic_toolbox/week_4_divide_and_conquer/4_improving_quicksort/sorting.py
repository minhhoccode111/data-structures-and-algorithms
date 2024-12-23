# python3

# sort a given sequence of numbers (that may containn duplicates) using a
# modification of RandomizedQuickSort that works in O(n log n) time

from random import randint


def partition3(array, left, right):
    # save pivot value
    pivot = array[left]
    # m1 is the pointer rightmost position of elements < pivot
    # m2 is the pointer rightmost position of elements == pivot
    m1 = left
    m2 = left

    # loop from the next-to-pivot to the end of the virtual array, with pointer i
    for i in range(left + 1, right + 1):
        # if current element is less than pivot
        if array[i] < pivot:
            # then move m2 pointer to the right one (rightmost position of elements == pivot)
            m2 += 1
            # and swap value of i and m2
            array[i], array[m2] = array[m2], array[i]
            # and move m1 pointer to the right one (rightmost position of elements < pivot)
            m1 += 1
            # swap value of m1 and m2
            array[m1], array[m2] = array[m2], array[m1]
        # if current element is equal to pivot
        elif array[i] == pivot:
            # only move m2 pointer to the right one (rightmost position of element == pivot)
            m2 += 1
            array[i], array[m2] = array[m2], array[i]
            # so that the m1 pointer indicate the start of sequence elements == pivot
            # and m2 indicate the end of sequence elements == pivot
        # greater case do nothing because already on the right side anyway

    # Move pivot to its final position, which is m1 (rightmost position of elements < pivot)
    array[left], array[m1] = array[m1], array[left]

    return m1, m2


def randomized_quick_sort(array, left, right):
    # base case if the virtual sub array contains nothing
    # a virtual array = array[left...right]
    if left >= right:
        return
    # a random index between left and right to use as pivot
    k = randint(left, right)
    # swap pivot to the first element (left) to use in partition
    array[left], array[k] = array[k], array[left]
    # call partition3 to return 2 indices, the m1 indicate start of elements
    # equal pivot, the m2 indicate the end of elements equal pivot
    # so there could be one or many ones, and recursively sort elements equal to pivot is not efficient
    m1, m2 = partition3(array, left, right)
    # then recursive call with the remaining left elements
    randomized_quick_sort(array, left, m1 - 1)
    # and right elements
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == "__main__":
    # n first line
    input_n = int(input())
    # list of numbers
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    # in-place sorting
    randomized_quick_sort(elements, 0, input_n - 1)
    # print the elements in the sorted list instead of the list itself
    print(*elements)
