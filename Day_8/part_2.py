from collections import defaultdict
import re
import math


def read_input(file_path):

    with open(file_path) as fin:
        lines = fin.read().strip().split("\n")

    steps = lines[0]
    children = defaultdict(str)

    for line in lines[2:]:
        par, left, right = re.search(r"(...) = \((...), (...)\)", line).groups(0)
        children[par] = (left, right)

    return steps, children

def calculate_steps(steps, children, cur):

    count = 0
    while cur[2] != "Z":
        step = steps[count % len(steps)]
        if step == "L":
            cur = children[cur][0]
        else:
            cur = children[cur][1]

        count += 1

    return count

def main(file_path):

    steps, children = read_input(file_path)
    cur = [n for n in children if n[2] == "A"]
    lens = [calculate_steps(steps, children, node) for node in cur]

    ans = math.lcm(*lens)
    print(ans)

if __name__ == "__main__":
    file_path = 'Day_8/input.txt'
    main(file_path)
