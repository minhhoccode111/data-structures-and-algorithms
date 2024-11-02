from random import randint

from test_array import test_array


def partition3(array, left, right):
    # save pivot value to compare (which is the leftmost)
    pivot = array[left]
    # the first pointer, indicate the end of sequence elements less than pivot
    # which later will be swap with pivot to indicate the start of sequence elements equal to pivot
    p1 = left
    # the second pointer, indicate the end of sequence elements equal to pivot
    p2 = left

    # loop from the second index to the end of the array
    for i in range(left + 1, right + 1):
        # if current element is less than pivot
        if array[i] < pivot:
            # move pointer 2 to the right one
            p2 += 1
            # swap current element with pointer 2 element
            # so p2 right now is an element less than pivot
            array[p2], array[i] = array[i], array[p2]
            # move pointer 1 to the right one
            p1 += 1
            # swap pointer 1 element with pointer 2 element
            # so p1 right now will be an element less than pivot
            # and p2 right now will be an element equal to pivot, maintain our intent
            array[p1], array[p2] = array[p2], array[p1]

        # if current element is equal to pivot
        elif array[i] == pivot:
            # then just increase p2
            p2 += 1
            # then swap with i pointer
            # p2 now will still be equal to pivot
            array[p2], array[i] = array[i], array[p2]

    # swap p1 (indicate the end of sequence elements less than pivot) with pivot
    # to make p1 the start of sequence elements equal to pivot
    array[left], array[p1] = array[p1], array[left]

    return p1, p2


def efficient_quick_sort(array, left, right):
    # no need to sort array length less than 2
    if left >= right:
        return

    # pick random pivot in the array
    # not use the first element to avoid choosing the smallest element in a nearly sorted array
    pivot = randint(left, right)
    # swap pivot value with the first index value
    # to work with the rest easier
    array[left], array[pivot] = array[pivot], array[left]
    # get 2 indicies indicate the start and end of sequence elements equal to pivot
    # in many cases, it could be only one element (which is pivot itself)
    p1, p2 = partition3(array, left, right)
    # recursive call the left part of pivot (smaller elements)
    efficient_quick_sort(array, left, p1 - 1)
    # recursive call the right part of pivot (greater elements)
    efficient_quick_sort(array, p2 + 1, right)


if __name__ == "__main__":
    n = int(input())
    array = test_array(n)
    # before
    print(array)
    left = 0
    right = len(array) - 1
    efficient_quick_sort(array, left, right)
    # after
    print(array)
