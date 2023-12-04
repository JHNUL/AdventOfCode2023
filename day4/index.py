import re

def solution_part1(n: list):
    s = 0
    for line in n:
        sets = re.sub("Card \d:", "", line.replace("  ", " ")).split("|")
        winning = set(sets[0].strip().split(" "))
        played = set(sets[1].strip().split(" "))
        k = len(played.intersection(winning))
        if k > 0:
            s += (1 << (k-1))
    return s


def solution_part2(n: list):
    cards = [0]*len(n)
    for i, line in enumerate(n):
        sets = re.sub("Card \d:", "", line.replace("  ", " ")).split("|")
        winning = set(sets[0].strip().split(" "))
        played = set(sets[1].strip().split(" "))
        wins = len(played.intersection(winning))
        cards[i] += 1
        for j in range(i+1, i+wins+1):
            cards[j] += cards[i]
    return sum(cards)


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
