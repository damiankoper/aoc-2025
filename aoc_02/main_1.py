id_ranges: list[str] = []
with open("./aoc_02/input.txt") as file:
    id_ranges = file.readline().split(",")


def is_invalid(id: int) -> bool:
    id_str = str(id)
    id_str_len = len(id_str)
    id_str_len_div = divmod(id_str_len, 2)
    if (id_str_len_div[1] == 1):
        return False
    else:
        return id_str[0:id_str_len_div[0]] == id_str[id_str_len_div[0]:]


sum: int = 0
for id_range in id_ranges:
    (lower, upper) = map(int, id_range.split("-"))

    for id in range(lower, upper+1):
        if (is_invalid(id)):
            sum += id

print(sum)
