def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    n = int(input())
    print(fib(n))
