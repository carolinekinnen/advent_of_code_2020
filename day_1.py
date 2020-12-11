
# Part 1
# find the two numbers that sum to 2020 and then multiply those numbers together

# for example
sample_input = [1721, 979, 366, 299, 675, 1456]

# answer is 514579

import csv

with open('day_1_data.csv', newline = '') as f:
    reader = csv.reader(f)
    input_raw = list(reader)

data_input = []

for item in input_raw:
    num = int(item[0])
    data_input.append(num)

for num in data_input:
    for next_num in data_input:
        sum_two = num + next_num
        if sum_two == 2020:
            answer = num * next_num

# correct answer is 927684

# Part 2
# now find 3 numbers that meet same criteria

for num in data_input:
    for num2 in data_input:
        for num3 in data_input:
            sum_three = num + num2 + num3
            if sum_three == 2020:
                answer = num * num2 * num3

# correct answer is 292093004
