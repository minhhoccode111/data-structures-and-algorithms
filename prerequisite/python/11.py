# 5. modules

# you can import modules
import math

print(math.sqrt(16))  # 4.0

# you can get specific functions from a module
from math import ceil, floor

print(ceil(3.7))  # 4
print(floor(3.7))  # 3

# you can import all functions from a module
# warning: this is not recommended
# from math import * # not allowed

# you can shorten module names
import math as m

math.sqrt(16) == m.sqrt(16)  # true

# python modules are just ordinary python files. you can write your own, and import them. the name of the module is the same as the name of the file

# you can find out which functions and attributes are defined in a module
import math

dir(math)

# if you have a python script named math.py in the same folder as your current script, the file math.py will be loaded instead of the built-in python module.
# this happens because the local folder has priority over python's built-in libraries
