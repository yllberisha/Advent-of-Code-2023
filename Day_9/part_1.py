input_file = "Day_9/input.txt"

with open(input_file) as file:
    data = file.read().strip().split("\n")


def calculate_differences(array):
    return [array[i + 1] - array[i] for i in range(len(array) - 1)]


def compute_extrapolation(history):
    stages = [history]

    while not all([element == 0 for element in stages[-1]]):
        stages.append(calculate_differences(stages[-1]))

    stages[-1].append(0)
    for idx in range(len(stages) - 2, -1, -1):
        stages[idx].append(stages[idx][-1] + stages[idx + 1][-1])

    return stages[0][-1]


results = []
for entry in data:
    array = list(map(int, entry.split()))
    results.append(compute_extrapolation(array))

print(sum(results))
