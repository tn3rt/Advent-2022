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
# Instructions are "move x (crates) from y to z", input is list [x,y,z]
def move_crates(crates, instruction):
    x = instruction[0]
    y = instruction[1] - 1
    z = instruction[2] - 1
    for i in range(0,x):
        crates[z].append(crates[y].pop())


# Part 2
def move_n_crates(crates, instruction):
    x = instruction[0]
    y = instruction[1] - 1
    z = instruction[2] - 1
    tmp = []
    for i in range(0,x):
        tmp.append(crates[y].pop())
    for j in range(0,x):
        crates[z].append(tmp.pop())


# Read input and strip newline chars
my_input = read_input('day5.txt')

c1 = ['G', 'T', 'R', 'W']
c2 = ['G', 'C', 'H', 'P', 'M', 'S', 'V', 'W']
c3 = ['C', 'L', 'T', 'S', 'G', 'M']
c4 = ['J', 'H', 'D', 'M', 'W', 'R', 'F']
c5 = ['P', 'Q', 'L', 'H', 'S', 'W', 'F', 'J']
c6 = ['P', 'J', 'D', 'N', 'F', 'M', 'S']
c7 = ['Z', 'B', 'D', 'F', 'G', 'C', 'S', 'J']
c8 = ['R', 'T', 'B']
c9 = ['H', 'N', 'W', 'L', 'C']
# m1 = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
m2 = [c1, c2, c3, c4, c5, c6, c7, c8, c9]

my_input_int = input_str_to_int(my_input)

# Part 1
#for move in my_input_int:
#    move_crates(m1, move)
#for col in m1:
#    print(col.pop())

# Part 2
for move in my_input_int:
    move_N_crates(m2, move)
for col in m2:
    print(col.pop())