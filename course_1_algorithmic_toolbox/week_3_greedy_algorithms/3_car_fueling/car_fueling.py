from sys import stdin


def min_refills(distance, tank, stops):
    # Add the final destination as the last stop
    stops.append(distance)

    # Initialize the refill count to 0
    count = 0
    # initial position
    last_position = 0
    # Index to traverse the stops
    index = 0

    # While the destination is not reachable with the current fuel
    while last_position + tank < distance:
        # Set the current position as the last position
        current_position = last_position
        # Find the farthest reachable stop
        while index < len(stops) and stops[index] <= last_position + tank:
            # Update the current position to this stop
            current_position = stops[index]
            # Move to the next stop
            index += 1

        # If no stop is reachable from the last position
        if current_position == last_position:
            # destination is not reachable
            return -1

        # Update the last position to the current position
        last_position = current_position
        count += 1

    return count


if __name__ == "__main__":
    # distance, tank capacity, and stops
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
