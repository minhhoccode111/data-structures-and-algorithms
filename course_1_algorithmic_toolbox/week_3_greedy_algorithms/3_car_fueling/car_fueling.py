# python3


# computer the minimum number of gas tank refills to get from a city to another

from sys import stdin


def min_refills(distance, tank, stops):
    stops.append(distance)

    count = 0
    last_position = 0
    index = 0

    while last_position + tank < distance:
        current_position = last_position
        while index < len(stops) and stops[index] <= last_position + tank:
            current_position = stops[index]
            index += 1

        if current_position == last_position:
            return -1

        last_position = current_position
        count += 1

    return count


if __name__ == "__main__":
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
