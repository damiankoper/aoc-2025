rows: list[str] = []
with open("./aoc_03/input.txt") as file:
    rows = [line.rstrip() for line in file]


sum: int = 0
for row in rows:
    first: str = row[0]
    first_i: int = 0
    second: str = ""

    i = 0
    for i in range(1, len(row)-1):
        char = row[i]
        if first < char:
            first = char
            first_i = i

    for j in range(first_i+1, len(row)):
        char = row[j]
        if second < char:
            second = char

    sum += int(f"{first}{second}")
    print(f"{first}{second}")

print(sum)
