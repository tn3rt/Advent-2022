# Read the Advent of Code input
def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


def part_1_score_calc(x):
    score = 0
    if x[2] == 'X':
        score += 1
        if x[0] == 'A':
            score += 3
        if x[0] == 'C':
            score += 6
    if x[2] == 'Y':
        score += 2
        if x[0] == 'A':
            score += 6
        if x[0] == 'B':
            score += 3
    if x[2] == 'Z':
        score += 3
        if x[0] == 'B':
            score += 6
        if x[0] == 'C':
            score += 3
    return score

def part_2_score_calc(x):
    score = 0
    if x[0] == 'A':
        if x[2] == 'X':
            score += (3 + 0)
        if x[2] == 'Y':
            score += (1 + 3)
        if x[2] == 'Z':
            score += (2 + 6)
    if x[0] == 'B':
        if x[2] == 'X':
            score += (1 + 0)
        if x[2] == 'Y':
            score += (2 + 3)
        if x[2] == 'Z':
            score += (3 + 6)
    if x[0] == 'C':
        if x[2] == 'X':
            score += (2 + 0)
        if x[2] == 'Y':
            score += (3 + 3)
        if x[2] == 'Z':
            score += (1 + 6)
    return score


my_input = read_input('day2.txt')
sum_1 = 0
sum_2 = 0
for line in my_input:
    sum_1 += part_1_score_calc(line)
for line in my_input:
    sum_2 += part_2_score_calc(line)

print( sum_1 )
print( sum_2 )