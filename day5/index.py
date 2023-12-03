def solution_part1(line: str):
    pass


def solution_part2(line: str):
    pass


def solution(path: str, part=1):
    with open(path) as f:
        while True:
            line = f.readline()
            if not line:
                break
            if part == 1:
                res = solution_part1(line)
            else:
                res = solution_part2(line)


if __name__ == "__main__":
    res1 = solution("input.txt", 1)
    res2 = solution("input.txt", 2)
    print(res1, res2)
