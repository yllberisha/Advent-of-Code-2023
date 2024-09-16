# -------- Part 2 -----------
with open('Day_2\input.txt', 'r') as f:
    sum_of_cubes = 0
    for line in f:
        config = {'red': -1, 'green': -1, 'blue': -1}
        product = 1

        my_list = line.split(' ')[2:]
        cleaned_list = [item.strip('\n,;:') for item in my_list]
        isPossible = True
        for i in range(0, len(cleaned_list)-1,2):
            if int(cleaned_list[i]) > config[cleaned_list[i+1]]:
                config[cleaned_list[i+1]] = int(cleaned_list[i])

        for index, (key, value) in enumerate(config.items()):
    
            product = product * value

        sum_of_cubes += product
 

print(sum_of_cubes)