from re import split
from pprint import pprint
from functools import reduce


rows: list[str] = []

with open("./aoc_07/input.txt") as file:
    content = file.read()
    rows = content.split('\n')

sum = 0
for y in range(1, len(rows)):
    for x in range(len(rows[0])):
        char = rows[y][x]
        char_up = rows[y-1][x]
        char_left = None if x == 0 else rows[y][x-1]
        char_right = None if x == len(rows[0])-1 else rows[y][x+1]
        char_up_right = None if x == len(rows[0])-1 else rows[y-1][x+1]
        char_up_left = None if x == 0 else rows[y-1][x-1]
        if char_up == "S" and char == ".":
            rows[y] = rows[y][:x] + "|" + rows[y][x+1:]
        if char_up == "|" and char == ".":
            rows[y] = rows[y][:x] + "|" + rows[y][x+1:]

        if char_right == "^" and char_up_right == "|" and char == ".":
            rows[y] = rows[y][:x] + "|" + rows[y][x+1:]
        if char_left == "^" and char_up_left == "|" and char == ".":
            rows[y] = rows[y][:x] + "|" + rows[y][x+1:]

        if char == "^" and char_up == "|":
            sum += 1

print(sum)
