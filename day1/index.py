def solution_part1(x: str):
    s = 0
    with open(x) as f:
        while True:
            # line by line, don't read whole thing into memory
            line = f.readline().strip()
            if not line:
                break
            left = 0
            right = len(line) - 1
            first = None
            second = None
            while not first or not second:
                if not first and line[left].isdigit():
                    first = line[left]
                if not second and line[right].isdigit():
                    second = line[right]
                if not first:
                    left += 1
                if not second:
                    right -= 1
                # in case there are no digits in the string
                if left > right:
                    first = "0"
                    second = "0"
            s += int(f"{first}{second}")
    return s


def solution_part2(x: str):
    s = 0
    words = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    with open(x) as f:
        s = 0
        while True:
            line = f.readline().strip()
            if not line:
                break
            nums = []
            for i in range(len(line)):
                if line[i].isdigit():
                    nums.append(int(line[i]))
                else:
                    if i - 4 >= 0 and line[i-4:i+1] in words:
                        nums.append(words[line[i-4:i+1]])
                    if i - 3 >= 0 and line[i-3:i+1] in words:
                        nums.append(words[line[i-3:i+1]])
                    if i - 2 >= 0 and line[i-2:i+1] in words:
                        nums.append(words[line[i-2:i+1]])
            s += (nums[0]*10 + nums[-1])
    return s


if __name__ == "__main__":
    res1 = solution_part1("input.txt")
    res2 = solution_part2("input.txt")
    print(res1, res2)
