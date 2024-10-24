# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product, numbers[first] * numbers[second])
#     return max_product

from typing import Dict


def max_pairwise_product(numbers):
    index1 = 0
    index2 = 0
    # TODO:
    return


if __name__ == "__main__":
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
