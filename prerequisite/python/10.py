# python has first class functions
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_10 = create_adder(10)
add_10(3)  # 13


# closures in nested functions
# we can use the nonlocal keyword to work with variables in nested scope which shouldn't be declared in the inner functions
def create_avg():
    total = 0
    count = 0

    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total / count

    return avg


avg = create_avg()
avg(3)  # 3
avg(5)  # (3+5)/2 = 4.0
avg(7)  # (3+5+7)/3 = 5.0

# there are also anonymous functions
(lambda x: x > 2)(3)  # true
(lambda x, y: x**2 + y**2)(2, 3)  # 13

# there are built-in higher order functions
list(map(add_10, [1, 2, 3]))  # [11,12,13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # [4,2,3]

list(filter(lambda x: x > 5, [3, 4, 5, 6, 7]))  # [6,7]

# we can use list comprehensions for nice maps and filters
# list comprehension stores the output as a list (which itself may be nested)
[add_10(i) for i in [1, 2, 3]]  # [11,12,13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # [6,7]

# you can construct set and dict comprehensions as well
{x for x in "abcddeef" if x not in "abc"}  # {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
