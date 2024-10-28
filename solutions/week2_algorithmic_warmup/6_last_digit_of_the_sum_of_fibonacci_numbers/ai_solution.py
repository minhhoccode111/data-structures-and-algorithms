def fibonacci_sum_optimized(n):
    if n <= 1:
        return n

    # the last digit of fibonacci number have a period of 60
    # which mean that they repeat after 60 numbers
    n = n % 60

    if n <= 1:
        return n

    # Calculate up to n
    previous, current = 0, 1
    _sum = 1  # Initialize sum with F(1)

    for i in range(2, n + 1):
        # Calculate next Fibonacci number's last digit
        previous, current = current, (previous + current) % 10
        # Add it to sum
        _sum = (_sum + current) % 10

    return _sum


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum_optimized(n))
