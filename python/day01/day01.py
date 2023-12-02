#!/bin/python

FILENAME = '../../inputs/day01.input'

PEEK = -1

number_map = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

print("Starting...")

def get_input():
    with open(FILENAME, 'r') as f:
        inputs = f.readlines()
        return inputs

def filter_digits (code):
    return tuple([ x for x in code if x in '0123456789'])

def replace_all_numbers (codes):
    replaced = [ replace_numbers(s) for s in codes ] 
    return replaced 

def replace_numbers_in_string (s):
    replaced = s
    for number,digit in number_map.items():
        replaced = replaced.replace(number, digit) 
    return ''.join(replaced)

#def replace_subs(s):
#    replaced = s
#    for number,digit in number_map.items():
#        replaced = replaced.replace(number, digit) 
#    return ''.join(replaced)

def replace_numbers(s):
    subs = s
    replaced = []

    numbers_in = [ x for x in number_map.keys() if x in subs]
    if not numbers_in:
        return subs
    else:
        indexes = [ (num, subs.find(num)) for num in numbers_in ]
        matches = sorted(indexes, key=lambda x: x[1])
        subs = subs.replace(matches[0][0], number_map[matches[0][0]])
        return replace_numbers(subs)

unreplaced = get_input()
for line in unreplaced[:PEEK]:
    print(line.strip())
print()

replaced = replace_all_numbers(unreplaced)
# for line in replaced[:PEEK]:
#     print(line)
# print()

only_digits = [ filter_digits(code) for code in replaced ]
print(only_digits[:PEEK])

all_codes = [ f"{digits[0]}{digits[-1]}" for digits in only_digits  ]
print(all_codes[:PEEK])

all_codes_int = [ int(x) for x in all_codes ] 
print(all_codes_int[:PEEK])

total = sum(all_codes_int)
print(total)

test = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
]

for i,t in enumerate(test):
    print(i, ':', replace_numbers(t))
    #print(i, ':', ''.join(filter_digits(replace_numbers(t))))



print("Complete!")
