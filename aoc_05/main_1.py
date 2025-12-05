intervals: list[tuple[int, int]] = []
ids: list[int] = []
with open("./aoc_05/input.txt") as file:
    content = file.read()
    (raw_intervals, raw_ids) = content.split('\n\n')

    for raw_interval in raw_intervals.rstrip().split('\n'):
        parts = list(map(int, raw_interval.split('-')))
        intervals.append((parts[0], parts[1]))

    for raw_id in raw_ids.rstrip().split('\n'):
        ids.append(int(raw_id))

sum: int = 0
for id in ids:
    for interval in intervals:
        if id >= interval[0] and id <= interval[1]:
            sum += 1
            break

print(sum)
