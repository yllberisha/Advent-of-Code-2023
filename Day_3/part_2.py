"""
Extract Numbers:

extract_number(line, start_col) extracts a number from a line starting at a specific column and returns
the number as a string and the new column position.

Check Symbols and Update Goods Matrix:

is_symbol(i, j, num, lines, goods) checks if a cell at position (i, j) contains a symbol (not a dot or a digit). 
If it's a symbol ('*'), it adds the number num to the goods matrix at that position.

Process Each Line:

process_lines(lines) processes each line to update the goods matrix based on numbers 
found and their surrounding symbols. It extracts numbers, updates the goods matrix by checking cells 
around the numbers, and calculates a result based on the product of numbers found in cells marked with '*'.

Calculate Final Answer:

It iterates through the goods matrix to sum up the products of numbers in cells marked with '*' where exactly 
two numbers were found.
"""

def is_symbol(i, j, num, lines, goods):
    """Check if the cell at (i, j) is a symbol and update the goods matrix if it is."""
    if not (0 <= i < len(lines) and 0 <= j < len(lines[0])):
        return False

    if lines[i][j] == "*":
        goods[i][j].append(num)
    return lines[i][j] != "." and not lines[i][j].isdigit()

def extract_number(line, start_col):
    """Extract a number from a line starting at a specific column."""
    num_chars = []
    j = start_col
    while j < len(line) and line[j].isdigit():
        num_chars.append(line[j])
        j += 1
    return ''.join(num_chars), j

def process_lines(lines):
    """Process each line to update the goods matrix and calculate the final answer."""
    n = len(lines)
    m = len(lines[0])
    goods = [[[] for _ in range(m)] for _ in range(n)]
    ans = 0

    for i, line in enumerate(lines):
        j = 0
        while j < m:
            start = j
            num, j = extract_number(line, j)
            if num:
                num = int(num)
                # Check surrounding cells
                is_symbol(i, start - 1, num, lines, goods) or is_symbol(i, j, num, lines, goods)
                for k in range(start - 1, j + 1):
                    is_symbol(i - 1, k, num, lines, goods) or is_symbol(i + 1, k, num, lines, goods)
            j += 1

    # Calculate the final answer
    for i in range(n):
        for j in range(m):
            nums = goods[i][j]
            if lines[i][j] == "*" and len(nums) == 2:
                ans += nums[0] * nums[1]

    return ans

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.rstrip('\n') for line in file]

file_path = 'Day_3/input.txt'
lines = read_file(file_path)
result = process_lines(lines)
print(result)