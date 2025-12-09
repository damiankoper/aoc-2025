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
edges: list[tuple[Point, Point]] = []


def contains(a: Point, b: Point) -> bool:
    rect_left = min(a.x, b.x)
    rect_right = max(a.x, b.x)
    rect_top = min(a.y, b.y)
    rect_bottom = max(a.y, b.y)

    for edge in edges:
        edge_left = min(edge[0].x, edge[1].x)
        edge_right = max(edge[0].x, edge[1].x)
        edge_top = min(edge[0].y, edge[1].y)
        edge_bottom = max(edge[0].y, edge[1].y)

        if rect_left < edge_right and rect_right > edge_left and rect_top < edge_bottom and rect_bottom > edge_top:
            return True

    return False


with open("./aoc_09/input.txt") as file:
    content = file.read()
    points_raw = content.split('\n')
    for box_raw in points_raw:
        coords = box_raw.split(',')
        point = Point(int(coords[0]), int(coords[1]))
        points.append(point)

for i in range(len(points)-1):
    edges.append((points[i], points[i+1]))
edges.append((points[-1], points[0]))


max_area = 0
for i in range(len(points)):
    point = points[i]
    for j in range(i + 1, len(points)):
        point_cmp = points[j]
        if (not contains(point, point_cmp)):
            max_area = max(max_area, point.area(point_cmp))


pprint(max_area)
