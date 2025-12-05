from pprint import pprint
from time import sleep
from functools import cmp_to_key
intervals: list[tuple[int, int]] = []
with open("./aoc_05/input.txt") as file:
    content = file.read()
    (raw_intervals, _) = content.split('\n\n')

    for raw_interval in raw_intervals.rstrip().split('\n'):
        parts = list(map(int, raw_interval.split('-')))
        if (parts[0] > parts[1]):
            parts = (parts[1], parts[0])
        intervals.append((parts[0], parts[1]))


def cmp(a: tuple[int, int], b: tuple[int, int]) -> int:
    left = a[0] - b[0]
    right = a[1] - b[1]
    if left == 0:
        return right
    else:
        return left


intervals.sort(key=cmp_to_key(cmp))

i = 0
while i < len(intervals) - 1:
    left = intervals[i]
    right = intervals[i + 1]

    if (left[1] >= right[0]):
        if (right[1] >= left[1]):
            intervals[i] = (left[0], right[1])
        del intervals[i + 1]
    else:
        i += 1


sum: int = 0
for interval in intervals:
    sum += interval[1] - interval[0] + 1

print(sum)
