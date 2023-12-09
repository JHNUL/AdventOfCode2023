import math


def solution_part1(n: list):
    movements = n[0].strip()
    graph = {}
    for i in range(2, len(n)):
        bits = n[i].split("=")
        node = bits[0].strip()
        neighbours = bits[1].replace("(", "").replace(")", "").replace(" ", "").split(",")
        graph[node] = neighbours
    node = "AAA"
    steps = 0
    m = 0
    while node != "ZZZ":
        steps += 1
        if movements[m] == "R":
            node = graph[node][1]
        elif movements[m] == "L":
            node = graph[node][0]
        m = m + 1 if m < len(movements) - 1 else 0
    return steps

def _run_loop(graph, start_node, movements):
    m = 0
    steps = 0
    node = start_node
    targets = set()
    loop_counter = 0
    first_encounter = 0
    while True:
        steps += 1
        if len(targets) > 0:
            loop_counter += 1
        if movements[m] == "R":
            node = graph[node][1]
        elif movements[m] == "L":
            node = graph[node][0]
        if node in targets:
            return steps - first_encounter
        if node.endswith("Z"):
            first_encounter = steps
            targets.add(node)
        m = m + 1 if m < len(movements) - 1 else 0


def solution_part2(n: list):
    movements = n[0].strip()
    entry = set()
    graph = {}
    for i in range(2, len(n)):
        bits = n[i].split("=")
        node = bits[0].strip()
        if node.endswith("A"):
            entry.add(node)
        graph[node] = bits[1].replace("(", "").replace(")", "").replace(" ", "").split(",")
    loop_sizes = []
    for node in entry:
        loop_sizes.append(_run_loop(graph, node, movements))
    return math.lcm(*loop_sizes)

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
