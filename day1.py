# Read the Advent of Code input
def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


# Returns the sum of the calories from the top N elves
def max_calories(input_string, N):
    elf_calories = list()
    sum = 0
    top_N = 0

    # Returns a list of each elf's calorie sum
    for calories in my_input:
        if calories == '\n':
            elf_calories.append(sum)
            sum = 0
        else:
            sum += int(calories)

    # Adds the calories from the top elf, then removes it from the list
    for x in range(N):
        top_N += max(elf_calories)
        elf_calories.remove(max(elf_calories))

    return top_N


my_input = read_input('day1.txt')
print(max_calories(my_input, 1))
print(max_calories(my_input, 3))