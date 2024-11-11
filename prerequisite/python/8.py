# handle exceptions with a try/except block
try:
    # use 'raise' to raise an error
    raise IndexError("this is an index error")
except IndexError as e:
    pass  # refrain from this, provide a recovery (next example)
except (TypeError, NameError):
    pass  # multiple exceptions can be processed jointly
else:  # optional  clause to the try/except block. must follow all except blocks
    print("all good!")  # runs only if the code in try raises no exception
finally:  # execute under all circumstances
    print("we can clean up resources here")

# instead of try/finally to cleanup resources you can use a with statement
with open("myfile.txt") as f:
    for line in f:
        print(line)

# writing to a file
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w") as file:
    file.write(str(contents))  # writes a string to a file

import json

with open("myfile2.txt", "w") as file:
    file.write(json.dumps(contents))  # writes an object to a file

# reading from a file
with open("myfile1.txt") as file:
    contents = file.read()
print(contents)  # print: {"aa": 12, "bb": 21}

# python offers a fundametal abstraction called the iterable
# an iterable is an object that can be treated as a sequence
# the object returned by the range function, is an iterable

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(
    our_iterable
)  # dict_keys(['one', 'two', 'three']). this is an object that implements our iterable interface

# we can loop over it
for i in our_iterable:
    print(i)  # prints one, two, three

# however we cannot address elements by index
our_iterable[1]  # raises a TypeError

# an iterable is an object that knows how to create an interator
our_iterable = iter(our_iterable)

# our iterator is an object that can remember the state as we traverse through it
#  we get the next object with 'next()'
next(our_iterable)  # one

# it maintain state as we iterate
next(our_iterable)  # two
next(our_iterable)  # three

# after the iterator has returned all of its data, it raises a StopIteration exception
next(our_iterable)  # raises StopIteration

# we can also loop over it, in fact, 'for' does this implicitly
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)  # prints one, two, three

# you can grab all the elements of an iterable or iterator by call of list()
list(our_iterable)  # return ["one", "two", "three"]
list(our_iterator)  # return [] because state is saved
