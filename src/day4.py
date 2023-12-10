def main(input) -> tuple[int, int]:
    total_score = 0
    total_cards = 0
    copies_won = {}
    card_id = 0

    for line in input:
        card_id += 1
        copies_won[card_id] = copies_won.get(card_id, 0) + 1
        
        card, numbers = line.split("|")
        card = card.split(":")[-1]
        
        winning_numbers = set()
        matching_numbers = 0
        current_number = 0
        score = 0

        for char in card:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            else:
                if current_number > 0:
                    winning_numbers.add(current_number)
                current_number = 0

        for char in numbers:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            else:
                if current_number > 0 and current_number in winning_numbers:
                    score = score * 2 if score != 0 else 1
                    matching_numbers += 1
                current_number = 0
        
        for i in range(matching_numbers):
            copies_won[card_id+i+1] = copies_won.get(card_id+i+1, 0) + copies_won[card_id]
        
        total_score += score
    
    for id, copies in copies_won.items():
        if id <= card_id:
            total_cards += copies

    return total_score, total_cards

if __name__ == "__main__":
    import sys
    part1, part2 = main(sys.stdin)
    print("Part 1:", part1)
    print("Part 2:", part2)

