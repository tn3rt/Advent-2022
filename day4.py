import re

# Read the Advent of Code input
def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


# Convert list of strings with numbers to list of ints
def input_str_to_int(str_list):
    int_list = []
    for pairs in str_list:
        int_list.append([int(s) for s in re.findall(r'\b\d+\b', pairs)])
    return int_list


# Part 1
def subset(int_list):
    part1_sum = 0
    for i in int_list:
        if i[0] == i[2] or i[1] == i[3]:
            part1_sum += 1
        elif i[0] < i[2] and i[1] > i[3]:
            part1_sum += 1
        elif i[0] > i[2] and i[1] < i[3]:
            part1_sum += 1
    return part1_sum


# Part 2
def any_overlap(int_list):
    part2_sum = 0
    for i in int_list:
        if i[0] == i[2] or i[1] == i[3]:
            part2_sum += 1
        elif i[0] < i[2] and i[1] > i[3]:
            part2_sum += 1
        elif i[0] > i[2] and i[1] < i[3]:
            part2_sum += 1
        elif i[0] < i[2] <= i[1]:
            part2_sum += 1
        elif i[0] <= i[3] < i[1]:
            part2_sum += 1

    return part2_sum


# Read input and strip newline chars
my_input = read_input('day4.txt')
my_input = [item.strip() for item in my_input]

my_input_int = input_str_to_int(my_input)

print(subset(my_input_int))
print(any_overlap(my_input_int))