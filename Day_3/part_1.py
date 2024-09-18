
# -------- Part 1 -------------
"""
Steps:
1. **Read Input Data**:
   - Reads a text file where each line represents a row of characters.
   - Stores this data in a 2D list (matrix), with each line becoming a row in the matrix.

2. **Add Padding**:
   - Adds padding around the matrix to handle edge cases.
   - Padding consists of extra rows and columns filled with a specified character (`.`) around the original data.

3. **Extract Small Matrices**:
   - Defines a function to extract a small submatrix (bbox) centered around each digit in the matrix.
   - The submatrix size and position depend on the digit and padding.

4. **Check for Valid Characters**:
   - Defines a function to check if all characters in the small matrix are either digits or the padding character (`.`).
   - Flags any matrix containing invalid characters.

5. **Sum Calculation**:
   - Traverses the matrix to locate digit characters.
   - For each digit, extracts the corresponding small matrix, validates it, and if valid, converts the sequence of digits into an integer.
   - Adds valid integers to a running total.

"""

def get_small_matrix(padding, row, col):
    number = ''
    j = col
    while data_matrix[row][j].isdigit():
        number += data_matrix[row][j]
        j += 1
    
    bbox = [['' for _ in range(len(number) + 2 * padding)] for _ in range(3)]
    
    start_col = col
    for bi in range(3):
        col = start_col
        for bj in range(len(number) + 2 * padding):
            bbox[bi][bj] = data_matrix[row - 1][col - 1]
            col += 1
        row += 1

    return bbox, number

def has_invalid_characters(matrix):
    # Use any() to check if any element in the matrix is not a digit or '.'
    return any(not (element.isdigit() or element == '.') for row in matrix for element in row)

file_path = 'Day_3/input.txt'

data_matrix = []

# Read the file and build the matrix
with open(file_path, 'r') as file:
    data_matrix = [list(line.rstrip('\n')) for line in file]

padding = 1
char = '.'
num_cols = len(data_matrix[0])

# Add padding to each row
data_matrix = [[char] * padding + row + [char] * padding for row in data_matrix]

# Add padding rows at the beginning and end
padding_row = [char] * len(data_matrix[0])
data_matrix = [padding_row] * padding + data_matrix + [padding_row] * padding

i = 1
total_sum = 0
while i < len(data_matrix) - 1:
    j = 0
    while j < len(data_matrix[0]) - 1:
        if data_matrix[i][j].isdigit():
            bbox, number = get_small_matrix(padding, i, j)
            if has_invalid_characters(bbox):
                total_sum += int(number)
            j += len(number) - 1  # Skip past the number
        j += 1
    i += 1

print(total_sum)
