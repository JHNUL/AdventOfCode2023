def solution(x: str):
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


if __name__ == "__main__":
    result = solution("input.txt")
    print(result)
