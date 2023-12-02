def solution_part1(x: str):
    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    with open(x) as f:
        s = 0
        while True:
            line = f.readline()
            if not line:
                break
            parts = line.split(":")
            game_id = int(parts[0].split(" ")[1])
            subsets = parts[1].split(";")
            possible = True
            for subset in subsets:
                draws = subset.split(",")
                for draw in draws:
                    details = draw.strip().split(" ")
                    amount = int(details[0])
                    color = details[1]
                    if constraints[color] < amount:
                        possible = False
            if possible:
                s += game_id
        return s


def solution_part2(x: str):
    with open(x) as f:
        s = 0
        while True:
            line = f.readline()
            if not line:
                break
            parts = line.split(":")
            game_id = int(parts[0].split(" ")[1])
            subsets = parts[1].split(";")
            minimums = {
                "red": -1,
                "green": -1,
                "blue": -1
            }
            for subset in subsets:
                draws = subset.split(",")
                for draw in draws:
                    details = draw.strip().split(" ")
                    amount = int(details[0])
                    color = details[1]
                    if amount > minimums[color]:
                        minimums[color] = amount
            s += (minimums["red"]*minimums["green"]*minimums["blue"])
        return s


if __name__ == "__main__":
    res1 = solution_part1("input.txt")
    res2 = solution_part2("input.txt")
    print(res1, res2)
