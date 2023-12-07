def main(input) -> tuple[int, int]:
    p1_cubes = { "red": 12, "green": 13, "blue": 14 }
    p1_total = 0
    p2_total = 0
    for line in input:
        p2_cubes = { "red": 0, "green": 0, "blue": 0 }
        game_id, sets = line.strip("\n").split(":")
        sets = sets.split(";")
        is_valid = True
        p2_counts = 1
        for s in sets:
            balls = s.split(",")
            for ball in balls:
                num, color = ball.strip(" ").split(" ")
                if int(num) > p1_cubes[color]:
                    is_valid = False
                p2_cubes[color] = max(p2_cubes[color], int(num))
        if is_valid:
            p1_total += int(game_id.split(" ")[-1])
        for counts in p2_cubes.values():
            p2_counts *= counts
        p2_total += p2_counts
    return p1_total, p2_total

if __name__ == "__main__":
    import sys
    p1_total, p2_total = main(sys.stdin)
    print(f"Part 1: {p1_total}")
    print(f"Part 2: {p2_total}")

