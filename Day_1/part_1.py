# ------------- Part 1 ---------------------
file_path = 'Day_1\input.txt'

with open(file_path, 'r') as file:
    numbers = []

    for line in file:
        r, l = 0, len(line) - 1
        number1, number2 = None, None

        while r <= l:
            if number1 is None and line[r].isnumeric():
                number1 = line[r]
            if number2 is None and line[l].isnumeric():
                number2 = line[l]

            if number1 is not None and number2 is not None:
                numbers.append(number1 + number2)
                break

            if number1 is None:
                r += 1
            if number2 is None:
                l -= 1

    print(sum(map(int, numbers)))
