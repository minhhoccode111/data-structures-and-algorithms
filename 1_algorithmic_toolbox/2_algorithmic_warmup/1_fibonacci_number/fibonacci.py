#!/bin/env python3


def fibonacci_number(n):
    if n <= 1:
        return n

    # first 2 numbers in fibonacci sequence
    a = 0
    b = 1
    # use i to count backward
    i = n - 2

    while i > 0:
        i -= 1
        c = a + b
        a = b
        b = c

    return a + b


if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci_number(input_n))
