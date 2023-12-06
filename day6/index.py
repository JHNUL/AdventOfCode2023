def solution_part1(n: list):
    times = n[0]
    distances = n[1]
    while "  " in times or "  " in distances:
        times = times.replace("  ", " ")
        distances = distances.replace("  ", " ")
    times = [int(z) for z in times.split(":")[1].strip().split(" ")]
    distances = [int(y) for y in distances.split(":")[1].strip().split(" ")]
    race_results = zip(times, distances)
    m = 1
    for time_limit, distance in race_results:
        ways = 0
        for i in range(1, time_limit):
            time_pressed = time_limit-i
            result = time_pressed*i
            if result > distance:
                ways += 1
        m *= ways
    return m


def solution_part2(n: list):
    times = n[0]
    distances = n[1]
    times = times.replace(" ", "")
    distances = distances.replace(" ", "")
    time_limit = int(times.split(":")[1])
    distance = int(distances.split(":")[1])
    ways = 0
    for i in range(1, time_limit):
        time_pressed = time_limit-i
        result = time_pressed*i
        if result > distance:
            ways += 1
    return ways


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
