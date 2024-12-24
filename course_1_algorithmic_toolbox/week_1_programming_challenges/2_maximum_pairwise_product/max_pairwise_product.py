# python3

# find the maximum product of two distinct numbers in a sequence of non-negative integers


# efficient because only need 1 loop
# bigO (n)
def max_pairwise_product(n):
    # store the two largest numbers
    max1, max2 = 0, 0

    # loop through each item in list
    for num in n:
        # if item greater than max1
        if num > max1:
            # shift the current largest to second largest
            max2 = max1
            # update the largest number
            max1 = num
        # else item greater than max2
        elif num > max2:
            # update the second largest
            max2 = num

    return max1 * max2


if __name__ == "__main__":
    # ignore the size of the input
    _ = int(input())
    # split the string to array of numbers
    input_numbers = list(map(int, input().split()))
    # print the result
    print(max_pairwise_product(input_numbers))
