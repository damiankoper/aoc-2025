from re import split
from pprint import pprint
from functools import reduce


class Problem:
    def __init__(self):
        self.operands_raw: list[str] = []
        self.operands: list[int] = []
        self.operator: str = ""


problems: list[Problem] = []

with open("./aoc_06/input.txt") as file:
    content = file.read()
    lines = content.split('\n')

    k = 0
    while k <= len(lines[0])-1:
        problem = Problem()
        for i in range(k, len(lines[0])):
            operand = ""
            for line in lines:
                if (line[i] == "*" or line[i] == "+"):
                    problem.operator = line[i]
                elif line[i] != " ":
                    operand += line[i]

            if (len(operand) > 0):
                problem.operands.append(int(operand))
            if i >= len(lines[0])-1 or len(operand) == 0:
                problems.append(problem)
                k = i+1
                break

sum = 0
for problem in problems:
    if (problem.operator == "*"):
        sum += reduce(lambda x, y: x * y, problem.operands, 1)
    if (problem.operator == "+"):
        sum += reduce(lambda x, y: x + y, problem.operands, 0)

print(problems)
print(sum)
