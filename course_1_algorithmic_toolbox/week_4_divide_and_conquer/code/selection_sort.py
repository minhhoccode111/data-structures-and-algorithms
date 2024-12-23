# python3


from test_array import test_array


def selection_sort(arr):
    leng = len(arr)
    for i in range(leng):
        minIndex = i
        for j in range(i + 1, leng):
            if arr[j] < arr[minIndex]:
                # swap
                arr[j], arr[minIndex] = arr[minIndex], arr[j]

    return arr


print(selection_sort(test_array(10)))
print(selection_sort(test_array(20)))
