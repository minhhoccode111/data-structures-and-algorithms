# 4. functions


def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y  # return values with a return statement


# calling functions with parameters
add(5, 6)  # print out "x is 5 and y is 6" and return 11

# another way to call functions is with keyword arguments
add(y=6, x=5)  # keyword argument can arrive in any order


# you can define functions that take a variable number of positional arguments
def varargs(*args):
    return args


varargs(1, 2, 3)  # (1,2,3)


# you can define functions that take a variable number of keyword arguments, as well
def keyword_args(**kwargs):
    return kwargs


# let's call it to set what happends
keyword_args(big="foot", loch="ness")  # {"big": "foot", "loch": "ness"}


# you can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)


"""
all_the_args(1,2,a=3,b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# when calling functions, you can do the opposite of args/kwargs
# use * to expand args (tuples) and use ** to expand kwargs (dictionaries)

args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}

all_the_args(*args)  # equivalent: all_the_args(1,2,3,4)
all_the_args(**kwargs)  # equivalent: all_the_args(a=3,b=4)
all_the_args(*args, **kwargs)  # equivalent: all_the_args(1,2,3,4,a=3,b=4)


# returing multiple values (with tuple assignments)
def swap(x, y):
    return y, x  # return multiple values as a tuple without the parenthesis
    # note: parenthesis have been excluded but can be included


x = 1
y = 2
x, y = swap(x, y)  # x = 2, y = 1
# (x, y) = swap(x, y) # again the use of parenthesis is optional

# global scope
x = 5


def set_x(num):
    # local scope begins here
    # local var x not the same as global var x
    x = num  # 43
    print(x)  # 43


def set_global_x(num):
    # global indicates that particular var lives in the global scope
    global x
    print(x)  # 5
    x = num  # global var x is now set to num
    print(x)  # num


set_x(43)
set_global_x(6)
"""
prints:
    43
    5
    6
"""
