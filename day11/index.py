def solution_part1(matrix, multiplier = 1):
    galaxies = []
    empty_rows = [0]*len(matrix)
    empty_cols = [0]*len(matrix[0])
    for i in range(0, len(matrix)):
        if "#" not in matrix[i]:
            empty_rows[i] = 1
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == "#":
                galaxies.append((i, j))
    for j in range(0, len(matrix[0])):
        empty = True
        for i in range(0, len(matrix)):
            if matrix[i][j] == "#":
                empty = False
                break
        if empty:
            empty_cols[j] = 1
    
    s = 0
    for k in range(0, len(galaxies)-1):
        fr = galaxies[k]
        for l in range(k+1, len(galaxies)):
            to = galaxies[l]
            s += abs(fr[0]-to[0]) + abs(fr[1]-to[1])
            min_x = min(fr[0], to[0])
            max_x = max(fr[0], to[0])
            min_y = min(fr[1], to[1])
            max_y = max(fr[1], to[1])
            s += sum(empty_rows[min_x:max_x+1])*multiplier
            s += sum(empty_cols[min_y:max_y+1])*multiplier
    return s

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
    res2 = solution_part1(n, 999999)
    print(res1, res2)
