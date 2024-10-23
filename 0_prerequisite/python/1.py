# Single line comments start with a number symbol.

""" Multiline strings can be written
    using three "s, and are often used
    as documentation.
"""

####################################################
## 1. Primitive Datatypes and Operators
####################################################

# You have numbers
3  # => 3

# Math is what you would expect
1 + 1  # => 2
8 - 1  # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# Floor division rounds towards negative infinity
5 // 3  # => 1
-5 // 3  # => -2
5.0 // 3.0  # => 1.0  # works on floats too
-5.0 // 3.0  # => -2.0

# The result of division is always a float
10.0 / 3  # => 3.3333333333333335

# Modulo operation
7 % 3  # => 1
# i % j have the same sign as j, unlike C
-7 % 3  # => 2 # weird

# Exponentiation (x**y, x to the yth power)
2**3  # => 8

# Enforce precedence with parentheses
1 + 3 * 2  # => 7
(1 + 3) * 2  # => 8

# Boolean values are primitives (Note: the capitalization)
True  # => True
False  # => False

# negate with not
not True  # => False
not False  # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False or True  # => True

# True and False are actually 1 and 0 but with different keywords
True + True  # => 2
True * 8  # => 8
False - 5  # => -5

# Comparison operators look at the numerical value of True and False
0 == False  # => True
2 > True  # => True
2 == True  # => False
-5 != False  # => True
