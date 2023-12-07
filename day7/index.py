from p1Hand import Hand
from p2Hand import HandPart2


def solution_part1(n: list):
    hands = sorted([Hand(x) for x in n])
    winnings = 0
    for i, hand in enumerate(hands):
        winnings += (i+1)*hand.bid
    return winnings


def solution_part2(n: list):
    hands = sorted([HandPart2(x) for x in n])
    winnings = 0
    for i, hand in enumerate(hands):
        winnings += (i+1)*hand.bid
    return winnings


def read_input(path: str, as_matrix=False):
    lines = []
    with open(path) as f:
        while True:
            line = f.readline()
            if not line:
                break
            hand, bid = line.strip().split(" ")
            lines.append((hand, int(bid)))
    if as_matrix:
        for i, line in enumerate(lines):
            lines[i] = [*line]
    return lines


if __name__ == "__main__":
    n = read_input("input.txt")
    res1 = solution_part1(n)
    res2 = solution_part2(n)
    print(res1, res2)
