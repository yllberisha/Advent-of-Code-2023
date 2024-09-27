from functools import cmp_to_key
from collections import defaultdict

file_path = "Day_7/input.txt"

with open(file_path) as file:
    raw_lines = file.read().strip().split("\n")

labels = "AKQJT98765432"

def determine_hand_type(hand):
    count_dict = defaultdict(int)
    for card in hand:
        count_dict[card] += 1

    counts = sorted(count_dict.values())
    if counts == [5]:
        return 5
    elif counts == [1, 4]:
        return 4
    elif counts == [2, 3]:
        return 3.5
    elif counts == [1, 1, 3]:
        return 3
    elif counts == [1, 2, 2]:
        return 2.5
    elif counts == [1, 1, 1, 2]:
        return 2
    else:
        return 1

def compare_hands(hand1, hand2):
    rank1 = (determine_hand_type(hand1), hand1)
    rank2 = (determine_hand_type(hand2), hand2)
    
    if rank1[0] == rank2[0]:
        if hand1 == hand2:
            return 0
        for card1, card2 in zip(hand1, hand2):
            if labels.index(card1) < labels.index(card2):
                return 1
            elif labels.index(card1) > labels.index(card2):
                return -1
        return -1
    return 1 if rank1[0] > rank2[0] else -1

lines = [(line.split()[0], int(line.split()[1])) for line in raw_lines]

sorted_lines = sorted(lines, key=cmp_to_key(lambda x, y: compare_hands(x[0], y[0])))

total_score = sum((index + 1) * line[1] for index, line in enumerate(sorted_lines))

print(total_score)
