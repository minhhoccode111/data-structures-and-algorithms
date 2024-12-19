def fib(n):
    arr = [0, 1]

    for i in range(2, n + 1):
        arr.append(arr[i - 1] + arr[i - 2])

    return arr[n]


if __name__ == "__main__":
    input_n = int(input())
    print(fib(input_n))
