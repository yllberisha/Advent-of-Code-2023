file_path = 'Day_6/input.txt'

def read_input(file_path):
    with open(file_path) as fin:
        lines = fin.read().strip().split("\n")
    t = int("".join(lines[0].split()[1:]))
    d = int("".join(lines[1].split()[1:]))
    return t, d

def ways(t, d):
    return sum(1 for i in range(t) if (t - i) * i > d)

t, d = read_input(file_path)
print(ways(t, d))
