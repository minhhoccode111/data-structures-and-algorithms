# python3

# find the maximum product of two distinct numbers in a sequence of non-negative integers


def max_pairwise_product(n):
    max1, max2 = 0, 0
    for num in n:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return max1 * max2


if __name__ == "__main__":
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
