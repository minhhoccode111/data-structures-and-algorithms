# python3


# computer the minimum number of gas tank refills to get from a city to another

from sys import stdin


def min_refills(distance, tank, stops):
    # final destination (distance) is also a stop
    stops.append(distance)

    # init refill count
    count = 0
    # init current position
    last_position = 0
    # init current stop index
    index = 0

    # while the destination is not reachable with the current fuel
    while last_position + tank < distance:
        # set current position to be the last position
        current_position = last_position
        # while current index (next stop index) is < the number of stops
        # and its value is <= the current position + tank (within reach)
        # NOTE: note that we only increase index and current position but not
        # last position, because we want to check whether we can move more than
        # 1 stop at a time with last position + tank (1 tank from last position)
        # only
        while index < len(stops) and stops[index] <= last_position + tank:
            # make current position the next stop
            current_position = stops[index]
            # increase the next stop index
            index += 1

        # if current position is the same as the last position
        # which mean we are not moving at all
        if current_position == last_position:
            # destination is not reachable
            return -1

        # last position will be updated to current position
        last_position = current_position
        # increase refill count
        count += 1

    # number of refills
    return count


if __name__ == "__main__":
    # get distance, tank capacity, and stops input
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
