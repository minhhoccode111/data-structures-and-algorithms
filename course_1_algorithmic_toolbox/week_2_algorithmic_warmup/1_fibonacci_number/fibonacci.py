# python3

# Compute the nth Fibonacci number


def fibonacci(n):
    arr = [0, 1]
    for i in range(2, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])
    return arr[n]


if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci(input_n))
