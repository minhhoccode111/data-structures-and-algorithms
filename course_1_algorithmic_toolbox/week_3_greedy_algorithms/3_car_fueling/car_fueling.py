from sys import stdin


def min_refills(distance, tank, stops):
    # add the destination as the final stop
    stops.append(distance)

    count = 0
    last_position = 0
    index = 0

    # while last position plus tank is smaller than distance (which mean we still have to move)
    while last_position + tank < distance:
        # find the farthest stop within the tank range
        current_position = last_position
        # keep increase stops index while we still in the range of last position plus tank
        while index < len(stops) and stops[index] <= last_position + tank:
            # update current position
            current_position = stops[index]
            # increase stop index
            index += 1

        # if no further stop is reachable
        if current_position == last_position:
            return -1

        # move to the farthest reachable stop and refual
        last_position = current_position
        count += 1

    return count


if __name__ == "__main__":
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
