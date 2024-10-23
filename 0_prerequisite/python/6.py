# sets store ... well sets
empty_set = set()

# initialize a set with a bunch of values
some_set = {1, 1, 2, 2, 3, 4}  # some_set is now {1,2,3,4}

# similar to keys of a dictionary, elements of a set have to be immutable
# invalid_set = {[1], 1}  # raises a TypeError: unhashable type: 'list'
valid_set = {(1), 1}

# add one more item to the set
filled_set = some_set
filled_set.add(5)  # filled_set is now {1,2,3,4,5}
# sets do not have duplicate elements
filled_set.add(5)  # it remains as before {1,2,3,4,5}

# do set intersection with &
other_set = {3, 4, 5, 6}
filled_set & other_set  # {3,4,5}

# do set union with |
filled_set | other_set  # {1,2,3,4,5,6}

# do set difference with -
{1, 2, 3, 4} - {2, 3, 5}  # {1,4}

# do set symmetric difference with ^
{1, 2, 3, 4} ^ {2, 3, 5}  # {1,4,5}

# check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3}  # false

# check if set on the left is a subset of set on the right
{1, 2} <= {1, 2, 3}  # true

# check for existence in a set with in
2 in filled_set  # true
10 in filled_set  # false

# make a one layer deep copy
filled_set = some_set.copy()  # filled_set is {1,2,3,4,5}
filled_set is some_set  # false
