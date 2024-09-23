"""
This script processes an input file to determine the final locations of a list of seeds after applying a series of mappings. 
Each seed is transformed based on the mappings, and the script outputs the minimum final location.

Steps:
1. Read the input file and extract the seeds and mappings.
2. For each seed, apply the mappings to find its final location.
3. Print the minimum of these final locations.

The mappings are defined as a list of transformations, where each transformation specifies a source range and a destination start.
If a seed falls within a source range, it is moved to the corresponding position in the destination range.
"""

# ---- Part 1 -----

file_path = 'Day_5\input.txt'
with open(file_path) as fin:
    lines = fin.read().strip().split("\n")

# Extract seeds from the first line
seeds = list(map(int, lines[0].split()[1:]))

# Generate all the mappings
maps = []
i = 2
while i < len(lines):
    current_map = []
    i += 1
    while i < len(lines) and lines[i] != "":
        dst_start, src_start, range_len = map(int, lines[i].split())
        current_map.append((dst_start, src_start, range_len))
        i += 1
    maps.append(current_map)
    i += 1

def find_loc(seed):
    cur_num = seed
    for mapping in maps:
        for dst_start, src_start, range_len in mapping:
            if src_start <= cur_num < src_start + range_len:
                cur_num = dst_start + (cur_num - src_start)
                break
    return cur_num

# Find final locations for all seeds
final_locations = [find_loc(seed) for seed in seeds]

# Print the minimum final location
print(min(final_locations))
