import re, time


def create_str(places, constraint):
    s = "_"*places[0]
    i = 1
    for c in constraint:
        s += c
        s += "_"*places[i]
        i += 1
    return s


def comb(places, k, i, constraint, config, res):
    if i == len(places):
        if sum(places) == k and 0 not in places[1:-1]:
            candidate = create_str(places, constraint)
            if re.match(config.replace(".","_").replace("?", "."), candidate):
                res.add(candidate)
    else:
        for j in range(0, k + 1):
            places[i] = j
            comb(places, k, i + 1, constraint, config, res)


def solution_part1(n: list):
    s = 0
    for i in range(len(n)):
        line = n[i].split(" ")
        configuration = line[0]
        constraint = [int(x) for x in line[1].split(",")]
        k = len(configuration) - sum(constraint)
        places = [0]*(len(constraint)+1)
        res = set()
        comb(places, k, 0, ["#"*x for x in constraint], configuration, res)
        s += len(res)
    return s


def solution_part2(n: list):
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
    n = read_input("input.txt")
    start = time.time()
    res1 = solution_part1(n)
    end = time.time()
    # res2 = solution_part2(n)
    print(res1, f"time {round(end-start, 2)}s")
