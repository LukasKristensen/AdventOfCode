data = [[y for y in x] for x in open("input.txt", "r").read().splitlines()]
indexes_empty_y = []
indexes_empty_x = []

for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] != ".":
            break
        if x == len(data[y])-1:
            indexes_empty_y.append(y)

for x in range(len(data[0])):
    for y in range(len(data)):
        if data[y][x] != ".":
            break
        if y == len(data)-1:
            indexes_empty_x.append(x)

locations = [(x, y) for x in range(len(data[0])) for y in range(len(data)) if data[y][x] == "#"]
distance = 0
additional_multiply = 0
checked_locations = []

for i in locations:
    for j in locations:
        if i != j and (i, j) not in checked_locations and (j, i) not in checked_locations:
            additional_multiply += sum([1 for x in range(i[0], j[0]) if x in indexes_empty_x and i[0] <= j[0]])
            additional_multiply += sum([1 for x in range(j[0], i[0]) if x in indexes_empty_x and i[0] > j[0]])
            additional_multiply += sum([1 for y in range(i[1], j[1]) if y in indexes_empty_y and i[1] <= j[1]])
            additional_multiply += sum([1 for y in range(j[1], i[1]) if y in indexes_empty_y and i[1] > j[1]])
            checked_locations.append((i, j))
            distance += abs(i[0] - j[0]) + abs(i[1] - j[1])

print("additional_multiply: ", additional_multiply)
print("part_one: ", distance+additional_multiply)
print("part_two: ", distance+(additional_multiply*1000000)-additional_multiply)

