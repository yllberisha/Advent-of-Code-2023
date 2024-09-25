file_path = 'Day_6/input.txt'

def read_input(file_path):
    with open(file_path) as fin:
        lines = fin.read().strip().split("\n")
    times = list(map(int, lines[0].split()[1:]))
    dists = list(map(int, lines[1].split()[1:]))
    return times, dists

def ways(t, d):
    return sum(1 for i in range(t) if (t - i) * i > d)

def calculate_product(times, dists):
    results = [ways(t, d) for t, d in zip(times, dists)]
    product = 1
    for result in results:
        product *= result
    return product


times, dists = read_input(file_path)
product = calculate_product(times, dists)
print(product)
