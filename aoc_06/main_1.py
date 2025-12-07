from re import split
from pprint import pprint
from functools import reduce


class Problem:

    def __init__(self):
        self.operands: list[int] = []
        self.operator: str = ""


problems: list[Problem] = []

with open("./aoc_06/input.txt") as file:
    content = file.read()
    lines = content.split('\n')

    for line in lines:
        tokens = line.split()

        i = 0
        for token in tokens:
            if len(problems) <= i:
                problem = Problem()
                problems.append(problem)

            if token == "*" or token == "+":
                problems[i].operator = token
            else:
                problems[i].operands.append(int(token))
            i += 1

sum = 0
for problem in problems:
    if (problem.operator == "*"):
        sum += reduce(lambda x, y: x * y, problem.operands, 1)
    if (problem.operator == "+"):
        sum += reduce(lambda x, y: x + y, problem.operands, 0)

print(problems)
print(sum)
