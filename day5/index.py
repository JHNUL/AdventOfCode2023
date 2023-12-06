import re


class Node:
    def __init__(self, name: str):
        self.name = name
        self.ranges = []
        self.nxt = None
        self.prev = None

    def add_range(self, range):
        nums = [int(x) for x in range.replace("  ", " ").strip().split(" ")]
        self.ranges.append(nums)

    def get_dest(self, n):
        for rng in self.ranges:
            if rng[1] <= n and n < rng[1]+rng[2]:
                return rng[0]+(n-rng[1])
        return n

    def get_src(self, d):
        for rng in self.ranges:
            if rng[0] <= d and d < rng[0]+rng[2]:
                return rng[1]+(d-rng[0])
        return d

    def __repr__(self) -> str:
        return f"{self.ranges}"


def parse_maps(l: list):
    link = None
    head = None
    for line in l:
        if re.match(".+-.+-.+map:", line):
            new = Node(line.split(" ")[0].strip())
            if link is not None:
                link.nxt = new
                new.prev = link
            else:
                head = new
            link = new
        elif re.match("\d+ \d+ \d+", line):
            link.add_range(line)
    return (head, link)


def solution_part1(head, seeds):
    res = float("inf")
    for seed in seeds:
        node = head
        num = seed
        while node is not None:
            num = node.get_dest(num)
            node = node.nxt
        res = min(res, num)
    return res


def fits_range(seeds, n):
    for i in range(0, len(seeds), 2):
        if seeds[i] <= n and n < (seeds[i]+seeds[i+1]):
            return True
    return False


def solution_part2(tail, seeds):
    loc = 0
    while True:
        node = tail
        num = loc
        while node is not None:
            num = node.get_src(num)
            node = node.prev
        if fits_range(seeds, num):
            return loc
        loc += 1


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
    head, tail = parse_maps(n)
    seeds = [int(x) for x in n[0].split(":")[1].strip().split(" ")]
    res1 = solution_part1(head, seeds)
    print(res1)
    # Takes around 20 sec
    # res2 = solution_part2(tail, seeds)
    # print(res2)
