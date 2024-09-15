# ------------- PART 2 --------------------
import re

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
number_lengths = {num: len(num) for num in numbers}
number_to_index = {num: str(index + 1) for index, num in enumerate(numbers)}

def parse_line(line):
    min_index = float('inf')
    max_index = -1
    first_found = None
    last_found = None
    
    i = 0
    while i < len(line):
        found = False
        for num, length in number_lengths.items():
            if line[i:i + length] == num:
                if i < min_index:
                    min_index = i
                    first_found = number_to_index[num]
                if i > max_index:
                    max_index = i
                    last_found = number_to_index[num]
                i += length - 2
                found = True
                break
        if not found:
            if line[i].isdigit():
                digit_str = line[i]
                if i < min_index:
                    min_index = i
                    first_found = digit_str
                if i > max_index:
                    max_index = i
                    last_found = digit_str
        i += 1

    if first_found is None or last_found is None:
        return ''
    return first_found + last_found

# Test data
# test = [
#     'two1nine',
#     'eightwothree',
#     'abcone2threexyz',
#     'xtwone3four',
#     '4nineeightseven2',
#     'zoneight234',
#     '7pqrstsixteen'
# ]

file_path = 'Day_1\input.txt'

total = 0

with open(file_path, 'r') as file:
    for line in file:
        total += int(parse_line(line))

print(f'Total: {total}')
