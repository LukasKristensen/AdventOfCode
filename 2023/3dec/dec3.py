input_data = open("input.txt", "r").read().splitlines()
digits_coordinated, part_one_gears = {}, []
part_one, part_two, gear_id = 0, 0, 0

for y in range(len(input_data)):
    stored_digit = ""
    for x in range(len(input_data[y])):
        if input_data[y][x].isdigit():
            stored_digit += str(input_data[y][x])
        if (not input_data[y][x].isdigit() or x == len(input_data[y])-1) and stored_digit:
            for i in range(0, len(stored_digit)):
                digits_coordinated[f'{y}, {x-i-1}'] = {'val': stored_digit, 'id': gear_id}
            gear_id += 1
            stored_digit = ""

for y in range(len(input_data)):
    for x in range(len(input_data[y])):
        first_gear = None
        if input_data[y][x] != '.' and not input_data[y][x].isdigit():
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if f'{y-i}, {x-j}' in digits_coordinated and digits_coordinated[f'{y-i}, {x-j}']['id'] not in part_one_gears:
                        part_one += int(digits_coordinated[f'{y-i}, {x-j}']['val'])
                        part_one_gears.append(digits_coordinated[f'{y-i}, {x-j}']['id'])
                    if f'{y-i}, {x-j}' in digits_coordinated:
                        if not first_gear:
                            first_gear = digits_coordinated[f'{y - i}, {x - j}']
                        elif not digits_coordinated[f'{y-i}, {x-j}']['id'] == first_gear['id']:
                            part_two += int(first_gear['val']) * int(digits_coordinated[f'{y - i}, {x - j}']['val']) if input_data[y][x] == '*' else 0
                            break
print("Part one:", part_one, "\nPart two:", part_two)

