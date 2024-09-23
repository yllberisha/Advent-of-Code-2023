"""
This script processes an input file to determine the final locations of a list of seed intervals after applying a series of mappings. 
Each seed interval is transformed based on the mappings, and the script outputs the minimum final location.

Steps:
1. Read the input file and extract the seed intervals and mappings.
2. For each seed interval, apply the mappings to find its final location.
3. Print the minimum of these final locations.

The mappings are defined as a list of transformations, where each transformation specifies a source range and a destination start.
If a seed interval falls within a source range, it is moved to the corresponding position in the destination range.
"""

import re

def read_input(file_path):
    with open(file_path) as fin:
        lines = fin.read().strip().split("\n")
    
    raw_seeds = list(map(int, lines[0].split()[1:]))
    seeds = [(raw_seeds[i], raw_seeds[i + 1]) for i in range(0, len(raw_seeds), 2)]
    
    maps = []
    i = 2
    while i < len(lines):
        catA, _, catB = lines[i].split()[0].split("-")
        current_map = []
        i += 1
        while i < len(lines) and lines[i] != "":
            dst_start, src_start, range_len = map(int, lines[i].split())
            current_map.append((dst_start, src_start, range_len))
            i += 1
        current_map.sort(key=lambda x: x[1])
        maps.append(current_map)
        i += 1
    
    return seeds, maps

def ensure_disjoint_mappings(maps):
    for mapping in maps:
        for i in range(len(mapping) - 1):
            if not mapping[i][1] + mapping[i][2] <= mapping[i + 1][1]:
                print(mapping[i], mapping[i + 1])

def remap_interval(low, high, mapping):
    ans = []
    for dst, src, R in mapping:
        end = src + R - 1
        D = dst - src  # How much is this range shifted

        if not (end < low or src > high):
            ans.append((max(src, low), min(end, high), D))

    for i, interval in enumerate(ans):
        l, r, D = interval
        yield (l + D, r + D)

        if i < len(ans) - 1 and ans[i + 1][0] > r + 1:
            yield (r + 1, ans[i + 1][0] - 1)

    if len(ans) == 0:
        yield (low, high)
        return

    if ans[0][0] != low:
        yield (low, ans[0][0] - 1)
    if ans[-1][1] != high:
        yield (ans[-1][1] + 1, high)

def find_min_location(seeds, maps):
    min_location = float('inf')

    for start, R in seeds:
        cur_intervals = [(start, start + R - 1)]
        new_intervals = []

        for mapping in maps:
            for low, high in cur_intervals:
                for new_interval in remap_interval(low, high, mapping):
                    new_intervals.append(new_interval)
            cur_intervals, new_intervals = new_intervals, []

        for low, high in cur_intervals:
            min_location = min(min_location, low)

    return min_location

# Main execution
file_path = "Day_5/input.txt"
seeds, maps = read_input(file_path)
ensure_disjoint_mappings(maps)
min_location = find_min_location(seeds, maps)
print(min_location)
