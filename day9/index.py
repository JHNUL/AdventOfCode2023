def get_continuation(line: str):
    nums = [int(x) for x in line.strip().split(" ")]
    diff = nums
    stack = [diff[-1]]
    while True:
        new = []
        for i in range(1, len(diff)):
            new.append(diff[i]-diff[i-1])
        stack.append(new[-1])
        if len(set(new)) == 1:
            break
        else:
            diff = new
    while len(stack) > 1:
        to_add = stack.pop()
        stack[-1] = stack[-1] + to_add
    return stack.pop()


def get_prefix(line: str):
    nums = [int(x) for x in line.strip().split(" ")]
    diff = nums
    stack = [diff[0]]
    while True:
        new = []
        for i in range(1, len(diff)):
            new.append(diff[i]-diff[i-1])
        stack.append(new[0])
        if len(set(new)) == 1:
            break
        else:
            diff = new
    while len(stack) > 1:
        to_add = stack.pop()
        stack[-1] = stack[-1] - to_add
    return stack.pop()


def solution_part1(n: list):
    s = 0
    for line in n:
        s += get_continuation(line)
    return s


def solution_part2(n: list):
    s = 0
    for line in n:
        s += get_prefix(line)
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
    n = read_input("input.txt")
    res1 = solution_part1(n)
    res2 = solution_part2(n)
    print(res1, res2)
