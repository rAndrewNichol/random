# Program 1 - Cellular Automaton
# This program takes a number between 0 and 255 to define a 'rule' based on the 8-bit binary
# representation of that number. It takes the 'rule' and the number of steps as command-line arguments.
# For more information on the procedure of the step-by-step process, visit link below.
# http://mathworld.wolfram.com/CellularAutomaton.html

import sys

# Converts an integer between 0 and 255 to binary value (8 bits) in the form of a string.
# Takes integer value between 0 and 255.
# Returns this 8-character string of zeros and ones.
def binary(number = 1):
    i = 7
    string = ""
    while number != 0:
        if number >= 2**i:
            number = number - 2**i
            string = string + '1'
        else:
            string = string + '0'
        i -= 1
    if len(string) < 8:
        string = append_zeros(string, 8-len(string))
    return string

# Takes a string and appends 'number' zeros to it.
# Returns new string.
def append_zeros(string = '', number = 1):
    for i in range(number):
        string = string + '0'
    # or string = string + '0' * number
    return string

# Creates the first row of the image. Uses the fact that every step adds a zero to either side of the initial one.
# Takes the number of steps.
# Returns the row in string format.
def first_row(steps = 1):
    row =  ""
    row = append_zeros(row, steps)
    row = row + '1'
    row =append_zeros(row, steps)
    return row

# Defines the rule for our number.
# Takes in an integer between 0 and 255.
# Returns a dictionary with the 7 possible 3-bit strings as keys.
def create_map(number = 1):
    binary_string = binary(number)
    rule = {'111': binary_string[0],
            '110': binary_string[1],
            '101': binary_string[2],
            '100': binary_string[3],
            '011': binary_string[4],
            '010': binary_string[5],
            '001': binary_string[6],
            '000': binary_string[7]
            }
    return rule

# Creates the next row based on the previous row according to the rule.
# Takes in a
def next_row(prev = '1', map = {}):
    row = ''
    for i in range(len(prev)):
        if i == 0:
            key = '0' + prev[0] + prev[1]
        elif i == len(prev) - 1 :
            key = prev[i-1] + prev[i] + '0'
        else:
            key = prev[i-1] + prev[i] + prev[i+1]
        row = row + map[key]
    return row


# __main__
number = int(sys.argv[1])
num_steps = int(sys.argv[2])

nrows = num_steps + 1
ncols = 2*num_steps + 1

rule = create_map(number)

rows = []

rows.append(first_row(num_steps))

for i in range(num_steps):
    rows.append(next_row(rows[i], rule))

# Prints the rows as output (with the appropriate header to define a portable bitmap format).
print("P1", ncols, nrows, sep = " ")
for x in rows: print(x)


