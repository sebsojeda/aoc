def main(input: list[str]) -> tuple[int,int]:
    p1 = 0
    p2 = 0
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for line in input:
        p1_digits: list[str] = []
        p2_digits: list[str] = []
        for i, c in enumerate(line):
            if c.isdigit():
                p1_digits.append(c)
                p2_digits.append(c)
            for j, num in enumerate(nums):
                if line[i:].startswith(num):
                    p2_digits.append(str(j+1))
        p1 += int(p1_digits[0] + p1_digits[-1])
        p2 += int(p2_digits[0] + p2_digits[-1])
    return p1, p2

if __name__ == "__main__":
    import sys
    p1, p2 = main(sys.stdin)
    print(f'Problem 1: {p1}, Problem 2: {p2}')

