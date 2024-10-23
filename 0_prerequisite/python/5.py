# tuples are like lists but are immutable
tup = (1, 2, 3)
tup[0]  # 1
# tup[0] = 3  # Raises a TypeError

# note that a tuple of length one has to have a comma after the last element but tuples of other lengths, even zero, do not
type((1))  # <class 'int'>
type((1,))  # <class 'tuple'>
type(())  # <class 'tuple'>

# you can do most of the list operations on tuples too
len(tup)  # 3
tup + (4, 5, 6)  # (1,2,3,4,5,6)
tup[:2]  # (1,2)
2 in tup  # True

# you can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # now a == 1, b == 2, c == 3
# you can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # now a == 1, b == [2,3], c == 4
# tuples are created by default if you leave out the parentheses
d, e, f = (
    4,
    5,
    6,
)  # tuple 4,5,6 is unpacked into variables d,e,f respectively such that d = 4, e = 5, f = 6
# now look how easy it is to swap two values
e, d = d, e  # d = 5, e = 4

# dictionaries store mappings from keys to values
empty_dict = {}
# here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# note keys for dictionaries have to be immutable types. This is to ensure that the key can be converted to a constant hash value for quick look-ups
# immutable types include ints, floats, strings, tuples
# invalid_dict = {[1, 2, 3]: "123"}  # yield a TypeError: unhashable type: 'list'
valid_dict = {(1, 2, 3): [1, 2, 3]}  # values can be of any type, however

# look up values with []
filled_dict["one"]  # 1

# get all keys as an iterable with 'keys()'. we need to wrap the call in list() to turn it into a list. we'll talk about those later. note - for python versions < 3.7, dictionary key ordering is not guaranteed. your results might not match the example below exactly. however, as of python 3.7, dictionary items maintain the order at which they are inserted into the dictionary
list(filled_dict.keys())  # ["three", "two", "one"] in python < 3.7
list(filled_dict.keys())  # ["one", "two", "three"] in python 3.7+

# get all keys as an iterable with "values()". once again we need to wrap it in list() to get it out of the iterable. note - same as above regarding key ordering
list(filled_dict.values())  # [3,2,1] in python < 3.7
list(filled_dict.values())  # [1,2,3] in python 3.7+

# check for existence of keys in a dict with 'in'
"one" in filled_dict  # true
1 in filled_dict  # false

# looking up a non-existing key is a KeyError
filled_dict["four"]  # KeyError

# use 'get()' method to avoid the KeyError
filled_dict.get("one")  # 1
filled_dict.get("four")  # None
# the get method supports a default argument when the values is missing
filled_dict.get("one", 4)  # 1
filled_dict.get("four", 4)  # 4

# 'setdefault()' inserts into a dict only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

# adding to a dict
filled_dict.update({"four": 4})  # {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4  # another way to add to dict

# remove keys from a dict with del
del filled_dict["one"]  # remove the key "one" from filled_dict

# from python 3.5 you can also use the additional unpacking options
{"a": 1, **{"b": 2}}  # {'a': 1, 'b': 2}
{"a": 1, **{"a": 2}}  # {'a': 2}
