def solution_part1(matrix: list):
    loc_s = None
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[0])):
            if matrix[row][col] == "S":
                loc_s = (row, col)
    pos = loc_s
    visited = set()
    visited.add(pos)
    while True:
        cell = matrix[pos[0]][pos[1]]
        up = matrix[pos[0]-1][pos[1]] if pos[0]-1 >= 0 else 'nil'
        down = matrix[pos[0]+1][pos[1]] if pos[0]+1 < len(matrix) else 'nil'
        left = matrix[pos[0]][pos[1]-1] if pos[1]-1 >= 0 else 'nil'
        right = matrix[pos[0]][pos[1]+1] if pos[1] + 1 < len(matrix[0]) else 'nil'
        l = len(visited)
        if up in "|F7" and cell in "S|JL" and (pos[0]-1, pos[1]) not in visited:
            pos = (pos[0]-1, pos[1])
        elif down in "|JL" and cell in "S|7F" and (pos[0]+1, pos[1]) not in visited:
            pos = (pos[0]+1, pos[1])
        elif left in "-FL" and cell in "S-7J" and (pos[0], pos[1]-1) not in visited:
            pos = (pos[0], pos[1]-1)
        elif right in "-7J" and cell in "S-FL" and (pos[0], pos[1]+1) not in visited:
            pos = (pos[0], pos[1]+1)
        if pos not in visited:
            visited.add(pos)
        if l == len(visited):
            break
    return len(visited) // 2


def solution_part2(matrix: list):
    pass


def read_input(path: str, as_matrix=False):
    lines = []
    with open(path) as f:
        while True:
            line = f.readline()
            if not line:
                break
            lines.append(line.strip())
    if as_matrix:
        for i, line in enumerate(lines):
            lines[i] = [*line]
    return lines


if __name__ == "__main__":
    n = read_input("input.txt", True)
    res1 = solution_part1(n)
    # res2 = solution_part2(n)
    print(res1)
