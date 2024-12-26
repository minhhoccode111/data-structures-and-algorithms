# python3

# compile the largest integer by concatenating the given integers

from functools import cmp_to_key


def largest_number(numbers):
    numbers = list(map(str, numbers))

    def is_greater_or_equal(num1, num2):
        str1, str2 = str(num1), str(num2)
        return int(str1 + str2) >= int(str2 + str1)

    def compare(x, y):
        if is_greater_or_equal(x, y):
            return -1
        return 1

    numbers.sort(key=cmp_to_key(compare))

    if numbers[0] == "0":
        return "0"

    return "".join(numbers)


if __name__ == "__main__":
    _ = input()
    numbers = list(map(int, input().split()))
    print(largest_number(numbers))
