# 3. control flow and iterables

# let's just make a variable
some_var = 5

# here is an if statement. indentation is signicant in python
# convertion is to use four spaces, not tabs
# this prints "some_var is smaller than 10"

if some_var > 10:
    print("some_var is totally bigger than 10")
elif some_var < 10:  # this elif clause is optional
    print("some_var is smaller than 10")
else:  # this is optional too
    print("some_var is indeed 10")


"""
for loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # you can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

"""
"ranger(number)" returns an iterable of numbers
from zero up to (but excluding) the given number
prints: 
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower,upper)" returns an iterable of numbers
from the lower number to the upper number
prints:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)
"""
"range(lower,upper,step)" returns an iterable of numbers
from the lower number to the upper number, while incrementing
by step. If step is not indicated, the default value is 1
prints:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)

"""
Loop over a list to retrieve both the index and the value of each list item:
    0 dog
    1 cat
    2 mouse
"""
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

"""
While loops go until a condition is no longer met.
prints: 
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1  # shorthand for x = x + 1
