#


def linear_search_rec(arr, low, high, key):
    if high < low:
        return None
    if arr[low] == key:
        return low
    return linear_search_rec(arr, low + 1, high, key)


def linear_search_it(arr, low, high, key):
    for i in range(low, high + 1):
        if arr[i] == key:
            return i
    return None
