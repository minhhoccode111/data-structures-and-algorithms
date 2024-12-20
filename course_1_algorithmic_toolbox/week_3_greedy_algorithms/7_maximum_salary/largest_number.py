# python3

# Compile the largest integer by concatenating the given integers

from functools import (
    cmp_to_key,
)  # Used to convert the custom comparison function into a key for sorting


def is_greater_or_equal(num1, num2):
    # Convert numbers to strings for concatenation
    str1, str2 = str(num1), str(num2)
    # Compare concatenated results to decide their order
    return int(str1 + str2) >= int(str2 + str1)


def largest_number(numbers):
    # Convert the list of integers to strings for string operations
    numbers = list(map(str, numbers))

    # Define a custom comparison function for sorting
    def compare(x, y):
        # If x should come before y in the final result
        if is_greater_or_equal(x, y):
            # x is "greater" in terms of concatenation order
            return -1
        # y is "greater" if the above condition is not satisfied
        return 1

    # Sort numbers based on the custom comparison logic
    numbers.sort(key=cmp_to_key(compare))

    # Special case: if the largest number in sorted order is "0",
    # it means all numbers are zeros, so the result should be "0"
    if numbers[0] == "0":
        return "0"

    # Concatenate all sorted numbers to form the largest number
    return "".join(numbers)


def main():
    n = int(input())  # Number of integers (not directly used in the logic)
    numbers = input().split()  # Read the list of numbers as strings
    numbers = [int(x) for x in numbers]  # Convert the strings to integers
    print(largest_number(numbers))  # Call the function and print the result


if __name__ == "__main__":
    main()  # Run the program when executed directly
