def is_engine_part(engine, gears, i, j) -> bool:
    def check_neighbor(i, j) -> bool:
        if i < 0 or i >= len(engine) or j < 0 or j >= len(engine[i]):
            return False
        if engine[i][j] == "*":
            gears.add((i, j))

        return not engine[i][j].isdigit() and engine[i][j] != "."
    
    return (check_neighbor(i, j-1)
            or check_neighbor(i, j+1)
            or check_neighbor(i-1, j) 
            or check_neighbor(i+1, j)
            or check_neighbor(i-1, j-1) 
            or check_neighbor(i-1, j+1) 
            or check_neighbor(i+1, j-1) 
            or check_neighbor(i+1, j+1))
 

def main(input) -> tuple[int, int]:
    lines = input.readlines()
    n = len(lines)
    m = len(lines[0].strip())
    engine = [list(line.strip()) for line in lines]
    gears_to_parts = {}

    gears = set()
    parts = 0
    ratios = 0
    contains_engine_part = False
    
    part = 0
    for i in range(n):
        for j in range(m):
            if engine[i][j].isdigit():
                part = part * 10 + int(engine[i][j])
                if is_engine_part(engine, gears, i, j):
                    contains_engine_part = True
            else:
                if part > 0 and contains_engine_part:
                    parts += part
                    for gear in gears:
                        gears_to_parts.setdefault(gear, []).append(part)
                gears = set()
                part = 0
                contains_engine_part = False
    
    for gear, nums in gears_to_parts.items():
        if len(nums) == 2:
            ratios += nums[0] * nums[1]
    return parts, ratios

if __name__ == "__main__":
    import sys
    p1, p2 = main(sys.stdin)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")

