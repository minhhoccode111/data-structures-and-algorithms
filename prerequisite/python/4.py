# none is an object
None  # None

# don't use the equality "==" symbol to compare objects to None
# use 'is' instead. This checks for equality of object identity
"etc" is None  # false
None is None  # true

# 2. Variables and collections

# python has a print function
print("I'm python. Nice to meet you!")  # I'm python. Nice to meet you!

# by default the print function also prints out a new line at the end
# use the optional argument end to change the end string
print("Hello, world", end="!")  # Hello, world!

# simple way to get input data from console
input_string_var = input("enter some data: ")  # return the data as a string

# there are no declarations, only assignments
# convention in naming variables is snake_case style
some_var = 5
some_var  # 5

# accessing a previously unassigned variable in an exception
# see control flow to learn more about exception handling
some_unknown_var  # raises a NameError

# if can be used as an expression
# equivalent of C's '?:' ternary operator
"yay!" if 0 > 1 else "nay!"  # nay!

# lists store sequences
li = []
# you can start with a prefilled list
other_li = [4, 5, 6]

# add stuff to the end of a list with append
li.append(1)  # li is now [1]
li.append(2)  # li is now [1,2]
li.append(4)  # li is now [1,2,4]
li.append(3)  # li is now [1,2,4,3]

# remove from the end with pop
li.pop()  # 3 and li is now [1,2,4]
# let's put it back
li.append(3)  # li is now [1,2,4,3] again

# access a list like you would any array
li[0]  # 1
# look at the last element
li[-1]  # 3

# looking out of bounds is an IndexError
li[4]  # raises an IndexError

# you can look at ranges with slice syntax
# the start index is included, the end index is not
# it's a closed/open range for you mathy types
li[1:3]  # return list from index 1 to 3 => [2,4]
li[2:]  # return list starting from index 2 => [4,3]
li[:3]  # return list from beginning until index 3 => [1,2,4]
li[::2]  # return list selecting elements with a step size of 2 => [1,4]
li[::-1]  # return list in reverse order => [3,4,2,1]
# use any combination of these to make advanced slices
# li[start:end:step]


# make a one layer deep copy using slices
li2 = li[:]  # li2 = [1,2,4,3] but (li2 is li) will result in false

# remove arbitrary elements from a list with 'del'
del li[2]  # lit is now [1,2,3]


# remove first occurrence of a value
li.remove(2)  # li is now [1,3]
li.remove(2)  # raises a ValueError as 2 is not in the list

# insert an element at a specific index
li.insert(1, 2)  # li is now [1,2,3] again

# get the index of the first item found matching the argument
li.index(2)  # 1
li.index(4)  # raise a ValueError as 4 is not in the list

# you can add lists
# note: values for li and for other_li are not modified
li + other_li  # [1,2,3,4,5,6]

# concatenate lists with "extend()"
li.extend(other_li)  # now li is [1,2,3,4,5,6]

# check for existence in a list with 'in'
1 in li  # true

# examine the length with "len()"
len(li)  # 6
