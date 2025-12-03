rows: list[str] = []
with open("./aoc_03/input.txt") as file:
    rows = [line.rstrip() for line in file]


def find_char(row: str, start_offset: int, end_offset: int) -> tuple[str, int]:
    first: str = row[start_offset]
    first_i: int = start_offset
    for i in range(start_offset, len(row) - end_offset):
        char = row[i]
        if first < char:
            first = char
            first_i = i

    return (first, first_i)


sum: int = 0
for row in rows:
    result: str = ""
    char = ""
    pos = -1
    for i in range(11, -1, -1):
        (char, pos) = find_char(row, pos + 1, i)
        result += char
    sum += int(result)

print(sum)
