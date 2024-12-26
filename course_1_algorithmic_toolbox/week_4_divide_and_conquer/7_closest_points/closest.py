# python3

# find the closest pair of points in a set of points on a plane


from collections import namedtuple
from math import sqrt

Point = namedtuple("Point", "x y")


def distance_squared(p1, p2):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


def distance(p1, p2):
    return sqrt(distance_squared(p1, p2))


def minimum_distance_strip(points_strip, d):
    points_strip.sort(key=lambda p: p.y)

    min_d = d

    for i in range(len(points_strip)):
        for j in range(i + 1, min(i + 8, len(points_strip))):
            min_d = min(min_d, distance(points_strip[i], points_strip[j]))

    return min_d


def minimum_distance_recursive(points_x):
    n = len(points_x)

    if n <= 1:
        return float("inf")

    if n == 2:
        return distance(points_x[0], points_x[1])

    mid = n // 2

    mid_point = points_x[mid]

    d1 = minimum_distance_recursive(points_x[:mid])

    d2 = minimum_distance_recursive(points_x[mid:])

    d = min(d1, d2)

    strip_points = []
    for point in points_x:
        if abs(point.x - mid_point.x) < d:
            strip_points.append(point)

    if strip_points:
        d = min(d, minimum_distance_strip(strip_points, d))

    return d


def minimum_distance(points):
    points_x = sorted(points, key=lambda p: p.x)

    return minimum_distance_recursive(points_x)


if __name__ == "__main__":
    input_n = int(input())

    input_points = []

    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(minimum_distance(input_points)))
