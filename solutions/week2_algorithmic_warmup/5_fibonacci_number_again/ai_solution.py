def get_pisano_period(m):
    """Calculate the Pisano period for modulo m."""
    if m <= 1:
        return 1

    previous, current = 0, 1
    period = 0

    while True:
        previous, current = current, (previous + current) % m
        period += 1
        if previous == 0 and current == 1:
            return period


def fibonacci_huge_optimized(n, m):
    """Calculate Fibonacci(n) mod m efficiently using Pisano period."""
    if m <= 1:
        return n % m
    if n <= 1:
        return n

    # Find the Pisano period
    pisano_period = get_pisano_period(m)

    # Use the remainder of n divided by pisano_period
    n = n % pisano_period

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_huge_optimized(n, m))
