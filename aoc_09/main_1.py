from pprint import pprint
from functools import reduce, lru_cache
from math import sqrt, prod
from collections import Counter


class Point:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def area(self, p):
        return (abs(p.x - self.x) + 1) * (abs(p.y - self.y) + 1)

    def __repr__(self) -> str:
        return f"Point({str(self.x).rjust(5)},{str(self.y).rjust(5)})"


points: list[Point] = []

with open("./aoc_09/input.txt") as file:
    content = file.read()
    points_raw = content.split('\n')
    for box_raw in points_raw:
        coords = box_raw.split(',')
        point = Point(int(coords[0]), int(coords[1]))
        points.append(point)

max_area = 0
for i in range(len(points)):
    point = points[i]
    for j in range(i + 1, len(points)):
        point_cmp = points[j]
        max_area = max(max_area, point.area(point_cmp))

pprint(max_area)
