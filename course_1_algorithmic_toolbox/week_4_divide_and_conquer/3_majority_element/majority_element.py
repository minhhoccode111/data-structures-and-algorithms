# python3

# check whethera given sequence of numbers contains an element that appears more
# than half of the times


# NOTE: this solution is not done in a divide-and-conquer way
def major_ele(elements):
    # create a dict to count unique items
    dict = {}
    # loop through every elements to count
    for n in elements:
        dict[n] = dict[n] + 1 if n in dict else 0

    threshold = len(elements) // 2

    # loop through dict to find the major
    for _, value in dict.items():
        if value >= threshold:
            return 1

    # return 0 if there is no majority element (depending on requirements)
    return 0


if __name__ == "__main__":
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(major_ele(input_elements))
