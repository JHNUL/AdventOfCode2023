import re


def is_adjacent(matrix, y, x):
    for row in range(max(y - 1, 0), min(y+2, len(matrix))):
        for col in range(max(x - 1, 0), min(x + 2, len(matrix[row]))):
            if not re.match("\.|\d", matrix[row][col]):
                return True
    return False


def get_gear_ratio(matrix, y, x):
    s = set()
    for row in range(max(y - 1, 0), min(y+2, len(matrix))):
        for col in range(max(x - 1, 0), min(x + 2, len(matrix[row]))):
            if re.match("\d.*", matrix[row][col]):
                s.add(matrix[row][col])
    if len(s) != 2:
        return 0
    l = [int(entry.split(" ")[0]) for entry in s]
    return l[0]*l[1]


def solution_part1(matrix: list):
    s = set()
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if re.match("\d", matrix[y][x]) and is_adjacent(matrix, y, x):
                s.add(matrix[y][x])
    return sum([int(entry.split(" ")[0]) for entry in s])


def solution_part2(matrix: list):
    s = 0
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if re.match("\*", matrix[y][x]):
                s += get_gear_ratio(matrix, y, x)
    return s


def create_matrix(path: str):
    with open(path) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            l = []
            the_line = line.strip()
            j = 0
            while j < len(the_line):
                symbol = the_line[j]
                new_symbol = symbol
                if re.match("\d", symbol):
                    # iterate forward until we have the whole number
                    m = j + 1
                    while m < len(the_line) and re.match("\d", the_line[m]):
                        new_symbol += the_line[m]
                        m += 1
                    j = m - 1
                    new_symbol += f" ({i},{j})"
                for k in range(len(new_symbol.split(" ")[0])):
                    l.append(new_symbol)
                j += 1
            lines[i] = l
        return lines


if __name__ == "__main__":
    m = create_matrix("input.txt")
    res1 = solution_part1(m)
    res2 = solution_part2(m)
    print(res1, res2)
