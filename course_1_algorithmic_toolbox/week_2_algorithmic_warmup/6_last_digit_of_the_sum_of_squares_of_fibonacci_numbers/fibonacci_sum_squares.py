# python3


def fibonacci_sum_squares(n):
    # Since we only need the last digit, we can use modulo 10 throughout
    # to keep numbers small
    if n < 2:
        return n

    # Initialize first two Fibonacci numbers
    f0, f1 = 0, 1
    # Initialize sum of squares
    sum_squares = f0 * f0 + f1 * f1

    # Find pattern in last digit
    # Store seen sums to detect cycle
    seen = {(0, 1): sum_squares}
    sequence = [sum_squares % 10]

    # Generate Fibonacci numbers and their squares
    for i in range(2, n + 1):
        # Calculate next Fibonacci number (keeping only last digit)
        f_next = (f0 + f1) % 10
        # Add its square to sum (only keep last digit of sum)
        sum_squares = (sum_squares + f_next * f_next) % 10

        # Store state
        state = (f1, f_next)
        if state in seen:
            # Found a cycle
            cycle_start = list(seen.values()).index(seen[state])
            cycle_length = len(seen) - cycle_start
            # Find position in cycle
            remaining = (n - i + 1) % cycle_length
            return sequence[cycle_start + remaining - 1]

        seen[state] = sum_squares
        sequence.append(sum_squares)

        # Update Fibonacci numbers
        f0, f1 = f1, f_next

    return sum_squares


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum_squares(n))
