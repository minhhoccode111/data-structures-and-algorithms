# python3

# Represent a positive integer as the sum of the maximum number of pairwise
# distinct positive integers


def optimal_summands(n):
    # list to store number of summands
    summands = []
    # start with 1
    current = 1

    while n > 0:
        # Check if the current number can be safely added
        if n - current > current:
            # add current to summands list
            summands.append(current)
            # decrease n by current
            n -= current
            # increase current by 1
            current += 1
        else:
            # if current is greater than n and can't be subtract
            # add the remainder to make the sum equal to n
            summands.append(n)
            # and break out of the loop
            break

    # return the list of summands
    return summands


if __name__ == "__main__":
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    # print elements in the list instead of the list itself
    print(*summands)
