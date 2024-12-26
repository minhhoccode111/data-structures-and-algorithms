# python3

# find the minimum number of points needed to cover all given segments on a line

from sys import stdin
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    segments.sort(key=lambda x: x.end)
    points = []

    while segments:
        current_point = segments[0].end
        points.append(current_point)
        segments = [s for s in segments if s.start > current_point]

    return points


if __name__ == "__main__":
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
