lines: list[str] = []
with open("./aoc_01/input.txt") as file:
    lines = [line.rstrip() for line in file]

sum: int = 50
zeros: int = 0
for line in lines:
    sign = 1 if line[0] == "R" else -1
    value = int(line[1:])

    # really stupid solution since modulo is tricky with negative
    for i in range(value):
        sum += sign
        if (sum == 100 or sum == -100):
            sum = 0
        if (sum == 0):
            zeros += 1

print(zeros)
