from functools import cmp_to_key
from collections import defaultdict

file_path = "Day_7/input.txt"

with open(file_path) as file:
    raw_lines = file.read().strip().split("\n")

labels = "AKQT98765432J"

def determine_hand_type(hand):
    counts = defaultdict(int)
    jokers = sum(1 for card in hand if card == "J")
    for card in hand:
        if card != "J":
            counts[card] += 1

    counts = sorted(counts.values())
    if jokers >= 5 or counts[-1] + jokers >= 5:
        return 5
    if jokers >= 4 or counts[-1] + jokers >= 4:
        return 4
    if counts[-1] + jokers >= 3:
        rem_jokers = counts[-1] + jokers - 3
        if len(counts) >= 2 and counts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 3.5
        return 3
    if counts[-1] + jokers >= 2:
        rem_jokers = counts[-1] + jokers - 2
        if len(counts) >= 2 and counts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 2.5
        return 2
    return 1

def compare_hands(hand1, hand2):
    rank1, rank2 = (determine_hand_type(hand1), hand1), (determine_hand_type(hand2), hand2)
    if rank1[0] == rank2[0]:
        return (hand1 > hand2) - (hand1 < hand2) if hand1 != hand2 else 0
    return (rank1[0] > rank2[0]) - (rank1[0] < rank2[0])

lines = [(line.split()[0], int(line.split()[1])) for line in raw_lines]
sorted_lines = sorted(lines, key=cmp_to_key(lambda x, y: compare_hands(x[0], y[0])))
total_score = sum((i + 1) * line[1] for i, line in enumerate(sorted_lines))

print(total_score)
