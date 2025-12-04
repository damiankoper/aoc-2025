rows: list[str] = []
with open("./aoc_04/input.txt") as file:
    rows = [line.rstrip() for line in file]
width = len(rows[0])
height = len(rows)


def accessible(x: int, y: int) -> bool:
    adjacent = 0

    if (y > 0 and x > 0 and rows[y - 1][x - 1] == '@'):
        adjacent += 1
    if (y > 0 and rows[y - 1][x] == '@'):
        adjacent += 1
    if (y > 0 and x < width - 1 and rows[y - 1][x + 1] == '@'):
        adjacent += 1
    if (x > 0 and rows[y][x - 1] == '@'):
        adjacent += 1
    if (x < width - 1 and rows[y][x+1] == '@'):
        adjacent += 1
    if (y < height - 1 and x > 0 and rows[y + 1][x - 1] == '@'):
        adjacent += 1
    if (y < height - 1 and rows[y + 1][x] == '@'):
        adjacent += 1
    if (y < height - 1 and x < width - 1 and rows[y + 1][x + 1] == '@'):
        adjacent += 1

    result = adjacent <= 3

    return result


sum: int = 0
while True:
    removed = False
    for y in range(height):
        for x in range(width):
            if rows[y][x] == "@" and accessible(x, y):
                sum += 1
                rows[y] = rows[y][0:x] + 'x' + rows[y][x+1:]
                removed = True
    if not removed:
        break

print(sum)
