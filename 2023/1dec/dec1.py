dict_numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
part_one, part_two = 0, 0

for i in open("input.txt", "r").read().splitlines():
    first_digit, last_digit = "", ""
    for x in range(len(i)):
        if i[x].isdigit() and not first_digit:
            first_digit = i[x]
        if i[-x-1].isdigit() and not last_digit:
            last_digit = i[-x-1]
    part_one += int(first_digit+last_digit)
print("1a)", part_one)


for i in open("input.txt", "r").read().splitlines():
    first_digit, last_digit = "", ""
    for x in range(len(i)):
        for key, value in dict_numbers.items():
            if (key in i[:x+1] or value in i[:x+1]) and not first_digit:
                first_digit = value
            if (key in i[-x-1:] or value in i[-x-1:]) and not last_digit:
                last_digit = value
    part_two += int(first_digit+last_digit)
print("1b)", part_two)

