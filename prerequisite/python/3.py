# strings are created with " or '

"This is a string"
"This is also a string"

# strings can be added too
"hello " + "world!"  # hello world!
# string literals (but not variables) can be concatenated without using '+'
"hello " "world!"  # hello world!

# a string can be treated like a list of characters
"hello world!"[0]  # "H"

# you can find the length of a string
len("this is a string")  # 16

# since python 3.6, you can use f-strings or formatted string literals
name = "reiko"
f"she said her name is {name}."  # she said her name is reiko
# any valid python expression inside these braces is returned to the string
f"{name} is {len(name)} characters long."  # reiko is 5 characters long
