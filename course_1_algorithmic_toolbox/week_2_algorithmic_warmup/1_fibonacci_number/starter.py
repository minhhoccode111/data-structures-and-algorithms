# naive
# bigO (2^n)
def naive(n):
    if n <= 1:
        return n

    return naive(n - 1) + naive(n - 2)


if __name__ == "__main__":
    input_n = int(input())
    print(naive(input_n))
