file_path = 'Day_10/input.txt'

# Read the input file and process it into lines
with open(file_path) as file:
    lines = [line.strip() for line in file.readlines()]

n, m = len(lines), len(lines[0])

# Define the directions for different symbols
direction_map = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": []
}

# Get the neighbors of a given position
def fetch_neighbors(x, y):
    neighbors = []
    for dx, dy in determine_directions(x, y):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            neighbors.append((nx, ny))
    return neighbors

# Determine valid directions based on the character in the grid
def determine_directions(x, y):
    if lines[x][y] == "S":
        connecting_dirs = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (x, y) in fetch_neighbors(nx, ny):
                connecting_dirs.append((dx, dy))

        # Find the character that matches the connecting directions
        for symbol, directions in direction_map.items():
            if sorted(directions) == sorted(connecting_dirs):
                lines[x] = lines[x].replace("S", symbol)
                break
        return connecting_dirs
    else:
        return direction_map[lines[x][y]]

# Find the start position 'S'
start_x, start_y = None, None
for row_idx, row in enumerate(lines):
    if 'S' in row:
        start_x, start_y = row_idx, row.index('S')
        break

# Perform DFS (Depth-First Search) to mark visited nodes
visited = set()
stack = [(start_x, start_y)]

while stack:
    current = stack.pop()
    if current in visited:
        continue
    visited.add(current)

    for neighbor in fetch_neighbors(*current):
        if neighbor not in visited:
            stack.append(neighbor)

# Count the number of inversions in a row
def count_inversions(row_idx, col_idx):
    count = 0
    line = lines[row_idx]

    for k in range(col_idx):
        if (row_idx, k) not in visited:
            continue
        if line[k] in {"J", "L", "|"}:
            count += 1

    return count

# Calculate the answer by counting odd inversions
result = 0
for row_idx, row in enumerate(lines):
    for col_idx in range(m):
        if (row_idx, col_idx) not in visited:
            inversions = count_inversions(row_idx, col_idx)
            if inversions % 2 == 1:
                result += 1

print(result)
