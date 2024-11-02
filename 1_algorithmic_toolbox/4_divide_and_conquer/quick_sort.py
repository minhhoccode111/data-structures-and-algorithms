#

from random import randint

from test_array import test_array

# NOTE: in python, arrays are being passed to function by ref


def part(array, left, right):
    # first element is pivot
    pivot = array[left]
    # slow pointer also start at the beginning
    slow = left

    # move from the next element to the end with fast pointer
    for fast in range(left + 1, right + 1):
        # if we find an element that less than or equal to pivot (first element)
        if array[fast] <= pivot:
            # then we increase the slow pointer by 1
            slow += 1
            # and swap the values of slow and fast pointer
            # (the slow pointer itself and elements to the left will always less than or equal to pivot)
            array[slow], array[fast] = (
                array[fast],
                array[slow],
            )

    # last, swap the pivot with slow pointer to make pivot center of the array
    array[left], array[slow] = array[slow], array[left]

    # return the index of pivot
    return slow


def quick(array, l, r):
    if r <= l:
        return array

    # find pivot in the right position
    pivot = part(array, l, r)
    # NOTE: catch if pivot out of bounds
    # recursive call with the left part
    quick(array, l, pivot - 1)
    # recursive call with the right part
    quick(array, pivot + 1, r)

    return array


# Example usage
if __name__ == "__main__":
    arr1 = test_array(10)
    arr2 = test_array(20)
    print(quick(arr1, 0, len(arr1) - 1))
    print(quick(arr2, 0, len(arr2) - 1))
