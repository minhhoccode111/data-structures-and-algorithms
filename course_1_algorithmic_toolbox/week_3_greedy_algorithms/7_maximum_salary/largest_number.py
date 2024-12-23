# python3

# compile the largest integer by concatenating the given integers

# convert the custom comparison function into a key for sorting
from functools import cmp_to_key


def largest_number(numbers):
    # Convert the list of integers to strings for string operations
    numbers = list(map(str, numbers))

    # function to decide 2 numbers' order
    def is_greater_or_equal(num1, num2):
        # convert to strings
        str1, str2 = str(num1), str(num2)
        # compare string concatenated results to decide their order
        return int(str1 + str2) >= int(str2 + str1)

    # define a custom comparison function for sorting
    def compare(x, y):
        # if x should come before y in the final result
        if is_greater_or_equal(x, y):
            # x is "greater" in terms of concatenation order
            # return -1 to indicate x should come before y
            return -1
        # y is "greater" if the above condition is not satisfied
        # return 1 to indicate x should come after y
        return 1

    # Sort numbers based on the custom comparison logic
    numbers.sort(key=cmp_to_key(compare))

    # edge case: if the largest number in sorted order is "0",
    # it means all numbers are zeros, so the result should be "0"
    if numbers[0] == "0":
        return "0"

    # concatenate all sorted numbers to form the largest number
    return "".join(numbers)


if __name__ == "__main__":
    _ = input()  # ignore first line
    numbers = list(map(int, input().split()))
    print(largest_number(numbers))
