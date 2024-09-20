file_path = 'Day_4/input.txt'

sum = 0
with open(file_path, 'r') as file:
    for line in file:
        numbers_part = line.split(':')[1].strip()
        before_pipe, after_pipe = numbers_part.split('|')

        before_numbers = before_pipe.split()
        after_numbers = after_pipe.split()

        before_set = set(before_numbers)
        after_set = set(after_numbers)

        common_numbers = before_set.intersection(after_set)

        common_count = len(common_numbers)

        if common_count != 0:
            sum += 2**(common_count-1)

print(sum)