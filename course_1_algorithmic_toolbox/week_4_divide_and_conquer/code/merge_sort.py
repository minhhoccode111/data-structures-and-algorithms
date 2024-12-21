# python3


from test_array import test_array


def merge(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    if arr1[0] < arr2[0]:
        return arr1[:1] + merge(arr1[1:], arr2)
    return arr2[:1] + merge(arr1, arr2[1:])


def merge_sort(arr):
    l = len(arr)
    mid = l // 2
    if l < 2:
        return arr
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid + 1 :]))


if __name__ == "__main__":
    print(merge_sort(test_array(2000)))
