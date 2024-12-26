# python3


# given a set of points and a set of segments on a line, compute, for each point,
# the number of segments it is contained in

from sys import stdin
from collections import namedtuple

Event = namedtuple("Event", ["coordinate", "event_type", "index"])
START = 1
END = -1
POINT = 0


def points_cover_fast(starts, ends, points):
    events = []

    for i, (start, end) in enumerate(zip(starts, ends)):
        events.append(Event(start, START, i))
        events.append(Event(end, END, i))

    for i, point in enumerate(points):
        events.append(Event(point, POINT, i))

    events.sort(key=lambda x: (x.coordinate, -x.event_type))

    active_segments = 0
    result = [0] * len(points)

    for event in events:
        if event.event_type == START:
            active_segments += 1
        elif event.event_type == END:
            active_segments -= 1
        else:
            result[event.index] = active_segments
    return result


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2 : 2 * n + 2 : 2], data[3 : 2 * n + 2 : 2]
    input_points = data[2 * n + 2 :]

    output_count = points_cover_fast(input_starts, input_ends, input_points)
    print(*output_count)
