# Read the Advent of Code input
def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines

# Splits the strings into sets, ANDs them to find common letter
def find_common(str):
    l = str[:len(str) // 2]
    r = str[len(str) // 2:]
    item = list(set(l) & set(r))
    return item[0]


# Converts letter to priority number
def char_to_priority(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


my_input = read_input('day3.txt')
part1_sum = 0
part2_sum = 0
my_input = [item.strip() for item in my_input]
for line in my_input:
    part1_sum += char_to_priority(find_common(line))

# Splits the input into groups of 3, finds intersection of the sets of strings
groups_of_three = zip(*(iter(my_input),) * 3)
for i in groups_of_three:
    part2_sum += char_to_priority(list(set(i[0]) & set(i[1]) & set(i[2])).pop())

print(part1_sum)
print(part2_sum)