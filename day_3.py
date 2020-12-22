
import csv
import numpy as np

# Solution using a for loop
# uses List of Lists of Strings
# importing from CSV

with open('day_3_data.csv', newline = '') as f:
    reader = csv.reader(f)
    trail = list(reader)

trail_paste = [['..##.........##.........##.........##.........##.........##.......'],
                ['#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..'],
                [".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#."],
                ["..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#"],
                [".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#."],
                ["..#.##.......#.##.......#.##.......#.##.......#.##.......#.##....."],
                [".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#"],
                [".#........#.#........#.#........#.#........#.#........#.#........#"],
                ["#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#..."],
                ["#...##....##...##....##...##....##...##....##...##....##...##....#"],
                [".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"]]

col = 3
trees = 0
max_len = len(trail[0][0])

for row, line in enumerate(trail):
    list_line = list(line[0])

    if row != 0:
        if col > max_len:
            col = 3

        character = list_line[col]

        col += 3

        if character == "#":
            trees += 1

# Solution using a function
# uses List of Strings
# importing from txt

trail_list = []

with open("day_3_data_txt.txt","r") as f:
    for line in f:
        trail_list.append(line)

max_len = len(trail_list[0])-1

def slope(col_incr, row_incr):
    '''
    Input, integers: column (x axis) increment, row (y axis) increment

    Return, integer: count of number of trees
    '''
    col = 0;
    row = 0;
    trees = 0;

    while row < len(trail_list):
        if trail_list[row][col] == "#":
            trees += 1
        col += col_incr
        row += row_incr
        if col >= max_len:
           col -= max_len

    return trees
