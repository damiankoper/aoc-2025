from pprint import pprint
from functools import reduce, lru_cache
from math import sqrt, prod
from collections import Counter


class Box:
    def __init__(self, x, y, z):
        self.x: int = x
        self.y: int = y
        self.z: int = z
        self.circuit = 0
        self.add_counter = 0

    def dist_squared(self, box):
        return (self.x - box.x) ** 2 + (self.y - box.y) ** 2 + (self.z - box.z) ** 2

    def __repr__(self) -> str:
        return f"{ str(self.x).rjust(5)},{str(self.y).rjust(5)},{str(self.z).rjust(5)} |{str(self.circuit).rjust(5)}"


class DisjoinedSet:
    def __init__(self, boxes: list[Box]):
        self.parent = {box: box for box in boxes}
        self.size = len(boxes)

    def find(self, box: Box) -> Box:
        if self.parent[box] != box:
            self.parent[box] = self.find(self.parent[box])
        return self.parent[box]

    def union(self, a: Box, b: Box) -> bool:
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB
            self.size -= 1
            return True
        return False


circuit = 0
boxes: list[Box] = []
distances: list[tuple[Box, Box, int]] = []

with open("./aoc_08/input.txt") as file:
    content = file.read()
    boxes_raw = content.split('\n')
    for box_raw in boxes_raw:
        coords = box_raw.split(',')
        box = Box(int(coords[0]), int(coords[1]), int(coords[2]))
        boxes.append(box)

for i in range(len(boxes)):
    box = boxes[i]
    for j in range(i+1, len(boxes)):
        box_cmp = boxes[j]
        d = box.dist_squared(box_cmp)
        distances.append((box, box_cmp, d))

distances = sorted(distances, key=lambda x: x[2])[:1000]

union = DisjoinedSet(boxes)

for distance in distances:
    (a, b, k) = distance
    union.union(a, b)

counter = Counter()
for box in boxes:
    b = union.find(box)
    counter[b] += 1

d = counter.most_common(3)

pprint(d[0][1]*d[1][1]*d[2][1])
