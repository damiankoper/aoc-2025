import textwrap

id_ranges: list[str] = []
with open("./aoc_02/input.txt") as file:
    id_ranges = file.readline().split(",")


def is_invalid(id: int) -> bool:
    id_str = str(id)

    # NOTE: textwrap.wrap is slow XD
    for n in reversed(range(1, len(id_str)//2+1)):
        splits = textwrap.wrap(id_str, n)
        invalid = splits.count(splits[0]) == len(splits)
        if invalid:
            return True

    return False


sum: int = 0
for id_range in id_ranges:
    (lower, upper) = map(int, id_range.split("-"))

    for id in range(lower, upper+1):
        if (is_invalid(id)):
            sum += id
            print(id)

print(sum)
