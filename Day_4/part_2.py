def process_card(card_index, card_data, memo):
    if card_index >= len(card_data):
        return 0

    if card_index in memo:
        return memo[card_index]

    before, after = card_data[card_index]
    matches = len(set(before).intersection(after))

    if matches == 0:
        memo[card_index] = 1
        return 1

    total_wins = 1 + sum(process_card(card_index + i, card_data, memo) for i in range(1, matches + 1))

    memo[card_index] = total_wins
    return total_wins

def calculate_total_scratchcards(file_path):
    with open(file_path, 'r') as file:
        card_data = [
            [part.strip().split() for part in line.split(':')[1].split('|')]
            for line in file
        ]

    memo = {}
    return sum(process_card(i, card_data, memo) for i in range(len(card_data)))

file_path = 'Day_4/input.txt'
total_scratchcards = calculate_total_scratchcards(file_path)
print(total_scratchcards)
