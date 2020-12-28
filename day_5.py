
# Day 5

# Scanning all nearby boarding passes to find yours through process of elimination

# Airline uses binary space partitioning to seat people
# ex = FBFBBFFRLR

# first 7 characters will be either F or B and specify exactly one of the
# 128 rows on plane (numbered 0 thru 127)
# each letter tells you which half of a region the given seat is in
# F is front (0 thru 64), B is back (65 thru 127)

# last 3 characters will be either L or R, specify exactly one of the 8
# columns of seats on the plane (numbered 0 through 7)
# L means to keep the lower half and R means to keep upper half

import csv

with open('day_5_data.csv', newline = '') as f:
    reader = csv.reader(f)
    b_passes = list(reader)

seat_ids = []

b_pass = "BFFFBBFRRR"

b_pass_class = BoardingPass("BFFFBBFRRR")

def find_seat_id(b_pass):
    '''
    Input:
    row_code (str): first 7 letters of string boarding pass
    col_code (str): last 3 letters of string boarding pass
    '''
    row_code = b_pass[:7]
    col_code = b_pass[7:]

    rows = range(0, 127)

    for letter in row_code:
        if letter == "F":
            if max(rows) - min(rows) == 0:
                final_row = min(rows)
                break
            rows = range(int(min(rows)), int((min(rows) + max(rows))/2))
        else:
            if max(rows) - min(rows) == 0:
                final_row = max(rows) + 1
                break
            rows = range(int((min(rows) + max(rows))/2) + 1, int(max(rows)) + 1)

    cols = range(0,7)

    for letter in col_code:
        if letter == "L":
            if max(cols) - min(cols) == 0:
                final_col = min(cols)
                break
            cols = range(int(min(cols)), int((min(cols) + max(cols))/2))  
        else:
            if max(cols) - min(cols) == 0:
                final_col = max(cols) + 1
                break
            cols = range(int((min(cols) + max(cols))/ 2) + 1, int(max(cols)) + 1)  

    return (final_row * 8) + final_col
    

highest_seat_id = 0

for b_pass in b_passes:
    seat_id = find_seat_id(b_pass[0])
    if seat_id > highest_seat_id:
        highest_seat_id = seat_id

all_seats = []

for b_pass in b_passes:
    all_seats.append(find_seat_id(b_pass[0]))

next_item = all_seats[0] - 1

missing_seat = 0

for item in all_seats:
    if item != next_item + 1:
        missing_seat = next_item + 1
    next_item = item