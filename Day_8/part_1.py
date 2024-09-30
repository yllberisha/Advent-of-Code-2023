"""
This script reads a set of instructions from a file and navigates through a series of nodes based on these instructions.

The file 'Day_8/input.txt' contains:
1. A string of steps ('L' for left, 'R' for right) on the first line.
2. A series of node definitions starting from the third line, where each line defines a parent node and its left and right child nodes in the format 'AAA = (BBB, CCC)'.

The script performs the following steps:
1. Reads the input file and splits it into lines.
2. Initializes a dictionary to store nodes.
3. Parses the steps from the first line of the file.
4. Creates Node objects for each parent node and stores them in the dictionary.
5. Starts at the node 'AAA' and follows the steps ('L' or 'R') to navigate through the nodes until it reaches the node 'ZZZ'.
6. Counts the number of steps taken to reach 'ZZZ' and prints the count.

"""


import re

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

file_path = 'Day_8/input.txt'

with open(file_path) as fin:
    lines = fin.read().strip().split("\n")

nodes = {}

steps = lines[0]
for line in lines[2:]:
    par, left, right = re.search("(...) = \((...), (...)\)", line).groups(0)
    nodes[par] = Node(left, right)

cur = "AAA"
count = 0
while cur != "ZZZ":
    step = steps[count % len(steps)]
    if step == "L":
        cur = nodes[cur].left
    else:
        cur = nodes[cur].right

    count += 1

print(count)
