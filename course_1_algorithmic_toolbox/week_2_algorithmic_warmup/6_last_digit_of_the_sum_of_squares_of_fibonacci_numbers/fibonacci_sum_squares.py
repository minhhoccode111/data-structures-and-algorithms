# python3


def fibonacci_sum_squares(n):
    if n < 2:
        return n

    f0, f1 = 0, 1
    sum_squares = f0 * f0 + f1 * f1

    seen = {(0, 1): sum_squares}
    sequence = [sum_squares % 10]

    for i in range(2, n + 1):
        f_next = (f0 + f1) % 10
        sum_squares = (sum_squares + f_next * f_next) % 10

        state = (f1, f_next)
        if state in seen:
            cycle_start = list(seen.values()).index(seen[state])
            cycle_length = len(seen) - cycle_start
            remaining = (n - i + 1) % cycle_length
            return sequence[cycle_start + remaining - 1]

        seen[state] = sum_squares
        sequence.append(sum_squares)

        f0, f1 = f1, f_next

    return sum_squares


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum_squares(n))
