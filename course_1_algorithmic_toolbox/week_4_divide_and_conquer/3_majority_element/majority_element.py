# python3

# check whethera given sequence of numbers contains an element that appears more
# than half of the times


def major_ele(elements):
    dict = {}
    for n in elements:
        dict[n] = dict[n] + 1 if n in dict else 0

    threshold = len(elements) // 2

    for _, value in dict.items():
        if value >= threshold:
            return 1

    return 0


if __name__ == "__main__":
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(major_ele(input_elements))
