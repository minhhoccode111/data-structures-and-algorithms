# python3


# given a set of points and a set of segments on a line, compute, for each point,
# the number of segments it is contained in

from sys import stdin
from collections import namedtuple

# Event tuple type
Event = namedtuple("Event", ["coordinate", "event_type", "index"])
START = 1
END = -1
POINT = 0


def points_cover_fast(starts, ends, points):
    # init events list
    events = []

    # pair starts list and ends list and iterate through it
    for i, (start, end) in enumerate(zip(starts, ends)):
        # create Event object and add to events list
        # with the 'coordinate' to 'start' and 'end'
        # and the event type 'START' and 'END'
        # and the index will be 'i'
        events.append(Event(start, START, i))
        events.append(Event(end, END, i))

    # then loop through every given points input list
    for i, point in enumerate(points):
        # then also add it to the events list with the point 'coordinate'
        # the 'POINT' event_type and the 'i' index
        events.append(Event(point, POINT, i))

    # sort events by coordinate
    # if coordinates are equal, process ends before points before starts
    # because their values are END: -1, POINT: 0, START: 1
    # this ensures that
    # we process ends first (to close any active segments at that coordinate)
    # the process points events (to count the segments that contain the points)
    # finally process starts events (to open new segments at that coordinate)
    events.sort(key=lambda x: (x.coordinate, -x.event_type))

    # process events
    # tracks the current number of open segments
    # (segments whose start has been processed but whose end has not yet been reached)
    active_segments = 0
    # the result list will have the same length as points, init to 0 for every query point
    # this will store the number of segments covering each query point
    result = [0] * len(points)

    # loop through every item in events list
    for event in events:
        # the 'START' event type indicatas the beginning of a segment
        if event.event_type == START:
            # increase active_segments, because we're opening a new segment
            active_segments += 1
            # example: if we encounter 'START' at coordinate 3, we add 1 to active_segments
        # the 'END' event type indicatas the end of a segment
        elif event.event_type == END:
            # decrease active_segments, because the segment is no longer active
            active_segments -= 1
            # example: if we encounter 'END' at coordinate 5, we subtract 1 from active_segments
        else:  # 'POINT'
            # a 'POINT' event represents a query point
            # the current value of `active_segments` at this point tell us how
            # many segments are covering the point
            # update the result list at the index corresponding to this query
            # point
            result[event.index] = active_segments
            # example: if we encounter 'POINT' at coordinate 4, and active_segments is 2
            # it means 2 segments cover this point

    # return the result list
    return result


if __name__ == "__main__":
    # get input string and split by spaces
    data = list(map(int, stdin.read().split()))
    # the first 2 items will be n and m
    n, m = data[0], data[1]
    # starts input will be even items, ends input will be odd items (skip the first 2 items)
    # the remaining items from 2 * n + 2 will be points input
    # so the input starts and input ends must stop before it
    input_starts, input_ends = data[2 : 2 * n + 2 : 2], data[3 : 2 * n + 2 : 2]
    input_points = data[2 * n + 2 :]

    output_count = points_cover_fast(input_starts, input_ends, input_points)
    # print every item in the list instead of the list itself
    print(*output_count)
