def read_grid(file_path):
    with open(file_path, 'r') as file:
        grid = [line.strip() for line in file.readlines()]
    return grid

def find_coords(grid):
    coordinates = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == "#"]
    return coordinates

def find_empty_rows_and_cols(grid):
    n, m = len(grid), len(grid[0])
    empty_rows = [all(cell == "." for cell in row) for row in grid]
    empty_cols = [all(grid[i][j] == "." for i in range(n)) for j in range(m)]
    return empty_rows, empty_cols

def calculate_distance(point1, point2, empty_rows, empty_cols):
    i1, j1 = min(point1[0], point2[0]), min(point1[1], point2[1])
    i2, j2 = max(point1[0], point2[0]), max(point1[1], point2[1])

    distance = (i2 - i1) + (j2 - j1)
    for i in range(i1, i2):
        if empty_rows[i]:
            distance += 1
    for j in range(j1, j2):
        if empty_cols[j]:
            distance += 1

    return distance

def total_distance(coords, empty_rows, empty_cols):
    total = 0
    for idx1 in range(len(coords)):
        for idx2 in range(idx1 + 1, len(coords)):
            total += calculate_distance(coords[idx1], coords[idx2], empty_rows, empty_cols)
    return total

file_path = 'Day_11/input.txt'
grid = read_grid(file_path)
coords = find_coords(grid)
empty_rows, empty_cols = find_empty_rows_and_cols(grid)
result = total_distance(coords, empty_rows, empty_cols)

print(result)
