
# Examining Passports
# form asks a series of 26 yes-or-no questions marked a thru z
# need to record which one a persons answers yes to

# ex:
abcz
abcx
abcy

# in this group there are 6 questions to which at least one person answered yes
abczxy

# Puzzle input is answers from every group on the plane
# answer is sum of each group's count of number of questions w/ at least one yes

passp_raw = []

with open("day_6_data.txt", "r", encoding="utf-8") as f:
    for line in f:
        passp_raw.append(line.split())

for i, item in enumerate(passp_raw):
    if item == []:
        passp_raw[i] = ["new entry"]
        
passp = []
group = []

for items in passp_raw:
    if items == ['new entry']:
        passp.append(group)
        group = []
    else:
        for one_item in items:
            group.append(one_item)

count_lst = []

for one_group in passp:
    group_letters = set()
    for one_person in one_group:
        for one_letter in one_person:
            group_letters.add(one_letter)

    count_lst.append(len(group_letters))

total_sum = 0

for num in count_lst:
    total_sum += num

