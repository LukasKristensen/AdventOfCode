input_data = open("input.txt", "r").read().splitlines()

for i in input_data:
    print(i)


digits_coordinated = {}


# Get all numbers and convert store them as coordinates
def validate(y_neighbor, x_neighbor):
    if not 0 <= y_neighbor <= len(input_data)-1 or not 0 <= x_neighbor <= len(input_data[0])-1:
        return False
    input_coord = input_data[y_neighbor][x_neighbor]
    return True if input_coord != '.' and not input_coord.isdigit() else False


part_one = 0
gear_id = 0
for y in range(len(input_data)):
    valid_digit = False
    stored_digit = ""
    for x in range(len(input_data[y])):
        if input_data[y][x].isdigit():
            stored_digit += str(input_data[y][x])
        if valid_digit and (not input_data[y][x].isdigit() or x == len(input_data[y])-1):
            part_one += int(stored_digit)
            valid_digit = False
            for i in range(0, len(stored_digit)):
                digits_coordinated[f'{y}, {x-i-1}'] = [stored_digit, gear_id]
            gear_id += 1
            stored_digit = ""
        if not input_data[y][x].isdigit() and not valid_digit:
            stored_digit = ""
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not valid_digit and stored_digit:
                    valid_digit = validate(y + i, x + j)

print("Part one:", part_one)


print("Digits coordinated:",digits_coordinated)
part_two = 0
for y in range(len(input_data)):
    for x in range(len(input_data[y])):
        first_gear, second_gear = None, None
        if input_data[y][x] == '*':
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if f'{y-i}, {x-j}' in digits_coordinated and not first_gear:
                        first_gear = digits_coordinated[f'{y-i}, {x-j}']
                        # break
                    elif f'{y-i}, {x-j}' in digits_coordinated and not digits_coordinated[f'{y-i}, {x-j}'][1] == first_gear[1]:
                        second_gear = digits_coordinated[f'{y-i}, {x-j}']
                        print("Found first:",first_gear,"Second:",second_gear)
                        part_two += int(first_gear[0])*int(second_gear[0])
                        break
print("Part two:", part_two)