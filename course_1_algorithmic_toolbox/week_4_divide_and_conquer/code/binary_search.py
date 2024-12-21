# python3


def binary_search_rec(arr, low, high, key):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid

    if arr[mid] > key:
        return binary_search_rec(arr, low, mid - 1, key)

    return binary_search_rec(arr, mid + 1, high, key)


def binary_search_it(arr, low, high, key):
    mid = (low + high) // 2

    while not low > high:
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
        mid = (low + high) // 2

    return -1


if __name__ == "__main__":
    n = int(input())
    print(binary_search_it([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10, n))
    print(binary_search_rec([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10, n))
