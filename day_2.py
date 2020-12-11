
# Part 1
# count how many passwords are valid if a valid password has the specified
# letter between the min and max times

sample_password_lst = [("1-3 a", "abcde"),
("1-3 b", "cdefg"),
("2-9 c", "ccccccccc")]

import csv

with open('day_2_data.csv', newline = '') as f:
    reader = csv.reader(f)
    input_raw = list(reader)

password_lst = []

for item in input_raw:
    key, value = item[0].split(":")
    password_lst.append((key, value))

count_passwords = 0

for rule, password in password_lst:
    split = rule.split()
    letter = split[-1]
    string = split[0]
    min_x, max_x = [int(s) for s in string.split("-") if s.isdigit()]
    letter_count = password.count(letter)
    if letter_count >= min_x and letter_count <= max_x:
        count_passwords += 1

# Part 2
# rules changed: now numbers represent positions and exactly
# one of these positions must contain the given letter

count_passwords_again = 0

for rule, password in password_lst:
    split = rule.split()
    letter = split[-1]
    string = split[0]
    posit1, posit2 = [int(s) for s in string.split("-") if s.isdigit()]
    posit1_letter = password.strip()[posit1 - 1]
    posit2_letter = password.strip()[posit2 - 1]
    if posit1_letter == letter and posit2_letter != letter:
        count_passwords_again += 1
    elif posit2_letter == letter and posit1_letter != letter:
        count_passwords_again += 1
