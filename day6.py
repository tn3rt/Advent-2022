# Read the Advent of Code input
def read_input(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines


# Finds the first time all the letters are different, n is the size of the window
def find_marker(str, n):
    for i in range(0, len(str)):
        if len(''.join(set(str[i:i+n]))) == n:
            print(i+n)
            break

# Read input and strip newline chars
my_input = read_input('day6.txt')
my_input_str = my_input[0]

find_marker(my_input[0], 14)