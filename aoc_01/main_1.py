lines: list[str] = []
with open("./aoc_01/input.txt") as file:
    lines = [line.rstrip() for line in file]

sum: int = 50
zeros: int = 0
for line in lines:
    sign = 1 if line[0] == "R" else -1
    value = int(line[1:])
    sum += value*sign
    sum = sum % 100

    if sum == 0:
        zeros += 1

print(zeros)
