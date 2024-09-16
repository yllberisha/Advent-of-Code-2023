config = {'red': 12, 'green': 13, 'blue': 14}

game_Index = 1
sum_of_indexes = 0
with open('Day_2\input.txt', 'r') as f:
    for line in f:
        my_list = line.split(' ')[2:]
        cleaned_list = [item.strip('\n,;:') for item in my_list]
        isPossible = True
        for i in range(0, len(cleaned_list)-1,2):
            if (config[cleaned_list[i+1]] - int(cleaned_list[i]) < 0):
                isPossible = False
                continue

        if isPossible:
            sum_of_indexes += game_Index

        game_Index += 1


print(sum_of_indexes)