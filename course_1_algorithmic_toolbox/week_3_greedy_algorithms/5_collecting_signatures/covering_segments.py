# python3

# find the minimum number of points needed to cover all given segments on a line

from sys import stdin
from collections import namedtuple

# define a named tuple called 'Segment' to represent a segment with a 'start' and 'end' point
# namedtuple: returns a new subclass of tuple with named fields.
Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    # sort segments by their end points, from closest to farthest endpoint
    segments.sort(key=lambda x: x.end)
    # list to store the points that cover all segments
    points = []

    # while there are uncovered segments
    while segments:
        # select the end point of the first segment in the sorted list
        current_point = segments[0].end
        # add the end point to the points list
        points.append(current_point)
        # remove all element covered by the current point by
        # create a new list where every segment start point is greater than
        # the current end point
        segments = [s for s in segments if s.start > current_point]

    # return the list of points
    return points


if __name__ == "__main__":
    input = stdin.read()

    # first number is n, the remaining numbers are data
    n, *data = map(int, input.split())

    # convert flat list data into a list of Segment objects
    # list: create a list object (collection) which is ordered and changeable
    # map: executes a specified function for each item in an iterable
    # zip: group numbers into tuples
    # data[::2]: every even element in data
    # data[1::2]: every odd element in data
    # example:
    # data[::2] = [0, 2, 4]
    # data[1::2] = [1, 3, 5]
    # zip(data[::2], data[1::2]) = [(0, 1), (2, 3), (4, 5)]
    # map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])) = [Segment(0, 1), Segment(2, 3), Segment(4, 5)]
    # then pass to `list()` to convert to a list
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))

    points = optimal_points(segments)

    print(len(points))
    # print the elements of the list instead of the list itself
    print(*points)
