from sys import stdin
from collections import namedtuple

# Define a named tuple called 'Segment' to represent a segment with a start and end point
Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    # sort segments by their end points
    segments.sort(key=lambda x: x.end)
    points = []  # List to store the points that cover all segments

    # while there are uncovered segments
    while segments:
        # select the end point of the first segment in the sorted list
        current_point = segments[0].end
        points.append(current_point)
        # remove all element covered by the current point
        segments = [s for s in segments if s.start > current_point]

    # Return the list of points
    return points


if __name__ == "__main__":
    input = stdin.read()

    # Parse the first number as the count of segments (n), and the remaining numbers as segment data
    n, *data = map(int, input.split())

    # Convert the flat list of segment data into a list of Segment objects
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))

    points = optimal_points(segments)

    print(len(points))
    print(*points)
