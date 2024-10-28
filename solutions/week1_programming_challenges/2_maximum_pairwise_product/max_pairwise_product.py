# # starter solution
# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product, numbers[first] * numbers[second])
#     return max_product


def max_pairwise_product(numbers):
    index1 = 0
    for i1, val1 in enumerate(numbers):
        if val1 > numbers[index1]:
            index1 = i1

    # in case index1 is 0
    index2 = 1 if index1 == 0 else 0
    for i2, val2 in enumerate(numbers):
        if val2 > numbers[index2] and i2 != index1:
            index2 = i2

    return numbers[index1] * numbers[index2]


if __name__ == "__main__":
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
