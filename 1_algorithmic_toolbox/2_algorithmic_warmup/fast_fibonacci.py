# base on lesson, this can be used with array, but we can skip it to reduce O(n) space complexity
def fibonacci(n):
    if n <= 1:
        return n

    a = 0
    b = 1
    i = n - 2

    while i > 0:
        i -= 1
        c = a + b
        a = b
        b = c

    return a + b


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
    # print(fibonacci(100)) # 354224848179261915075
    # print(fibonacci(n)) # 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125
