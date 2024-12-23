# python3

# find the closest pair of points in a set of points on a plane

# NOTE: need another recall

from collections import namedtuple
from math import sqrt

# define a point structure with x and y attributes for representing 2d points
Point = namedtuple("Point", "x y")


# calculate the squared euclidean distance between two points
def distance_squared(p1, p2):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


# calculate the euclidean distance between two points using the square root
def distance(p1, p2):
    return sqrt(distance_squared(p1, p2))


# find the minimum distance between points in a vertical strip
def minimum_distance_strip(points_strip, d):
    # sort points in the strip by their y-coordinate
    points_strip.sort(key=lambda p: p.y)

    # initialize the minimum distance in the strip to the given distance
    min_d = d

    # compare each point with the next 7 points in the strip (geometry constraint)
    for i in range(len(points_strip)):
        for j in range(i + 1, min(i + 8, len(points_strip))):
            # update the minimum distance if a smaller distance is found
            min_d = min(min_d, distance(points_strip[i], points_strip[j]))

    # return the minimum distance found in the strip
    return min_d


# recursive function to find the closest pair of points
def minimum_distance_recursive(points_x):
    # get the number of points
    n = len(points_x)

    # base case: if there is one point, return infinity (no pair exists)
    if n <= 1:
        return float("inf")

    # base case: if there are two points, calculate and return their distance
    if n == 2:
        return distance(points_x[0], points_x[1])

    # find the midpoint index
    mid = n // 2

    # get the point at the midpoint
    mid_point = points_x[mid]

    # recursively find the minimum distance in the left half
    d1 = minimum_distance_recursive(points_x[:mid])

    # recursively find the minimum distance in the right half
    d2 = minimum_distance_recursive(points_x[mid:])

    # find the smaller distance between the two halves
    d = min(d1, d2)

    # create a list of points near the dividing line within distance d
    strip_points = []
    for point in points_x:
        if abs(point.x - mid_point.x) < d:
            strip_points.append(point)

    # find the minimum distance in the strip if it is not empty
    if strip_points:
        d = min(d, minimum_distance_strip(strip_points, d))

    # return the overall minimum distance
    return d


# main function to calculate the closest pair distance
def minimum_distance(points):
    # sort points by x-coordinate for the divide-and-conquer algorithm
    points_x = sorted(points, key=lambda p: p.x)

    # call the recursive function to compute the minimum distance
    return minimum_distance_recursive(points_x)


if __name__ == "__main__":
    # read the number of points
    input_n = int(input())

    # initialize a list to store the points
    input_points = []

    # read each point and add it to the list
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    # calculate the minimum distance and print it formatted to 9 decimal places
    print("{0:.9f}".format(minimum_distance(input_points)))
