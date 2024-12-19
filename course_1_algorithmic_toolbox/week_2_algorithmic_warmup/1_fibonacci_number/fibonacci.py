# python3

# Compute the nth Fibonacci number


# efficient
# bigO (n)
def fibonacci(n):
    # 2 base cases
    arr = [0, 1]

    # loop from 2 to n
    for i in range(2, n + 1):
        # can't because python doesn't support dynamic arrays like javascript
        # arr[n] = arr[i - 1] + arr[i - 2]
        arr.append(arr[i - 1] + arr[i - 2])

    # return the last element in the array
    return arr[n]


if __name__ == "__main__":
    input_n = int(input())
    print(fibonacci(input_n))
