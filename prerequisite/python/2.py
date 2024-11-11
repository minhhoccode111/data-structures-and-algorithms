# none, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False
# all other values are True
bool(0)  # false
bool("")  # false
bool([])  # false
bool({})  # false
bool(())  # false
bool(set())  # false
bool(4)  # true
bool(-6)  # false

# using boolean logical operators on ints casts them to booleans for evaluation, but their non-case value is returned. Don't mix up with bool(ints) and bitwise and/or (&,|)
bool(0)  # => False
bool(2)  # => True
0 and 2  # => 0
bool(-5)  # => True
bool(2)  # => True
-5 or 0  # => -5

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >= 2  # => True

# Seeing whether a value is in a range
1 < 2 and 2 < 3  # => True
2 < 3 and 3 < 2  # => False
# Chaining makes this look nicer
1 < 2 < 3  # => True
2 < 3 < 2  # => False

# `is` vs. `==`
# `is` checks if two variables refer to the same object
# `==` checks if the objects pointed to have the same values
a = [1, 2, 3, 4]  # point a at a new list, [1,2,3,4]
b = a  # point b at what a is pointing to
b is a  # => True, a and b refer to the same object
b == a  # => True, a's and b's objects are equal
b = [1, 2, 3, 4]  # point b at a new list, [1,2,3,4]
b is a  # => False, a and b do not refer to the same object
b == a  # => True, a's and b's objects are equal
