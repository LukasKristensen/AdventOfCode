import math
data_load = open("input.txt", "r").read().splitlines()
navigation = data_load[0]
instructions = data_load[2:]
mapped_instructions = {}

for i in instructions:
    key, val = i.split(' = ')
    val = val[1:-1]
    mapped_instructions[key] = val.split(", ")

current_location = 'AAA'
step_count_p1, step_count_p2 = 0, 0

part_one = None
search = True

while search:
    if current_location == 'ZZZ' and not part_one:
        part_one = step_count_p1
        print("Part one:", part_one)
        search = False
    for i in navigation:
        step_count_p1 += 1
        if i == 'L':
            current_location = mapped_instructions[current_location][0]
        elif i == 'R':
            current_location = mapped_instructions[current_location][1]


step_count_2 = 0
testing = True
index_true = {}

locations_with_a = []
for i in mapped_instructions:
    if i[-1] == 'A':
        locations_with_a.append(i)
locations_from_a = locations_with_a.copy()

while testing:
    for i in navigation:
        for g in range(len(locations_from_a)):
            if locations_from_a[g][-1] == 'Z' and locations_with_a[g] not in index_true:
                index_true[locations_with_a[g]] = step_count_2

        print("Checking if:", len(index_true), len(locations_with_a))
        if len(index_true) == len(locations_with_a):
            testing = False
            break
        step_count_2 += 1

        for x in range(len(locations_from_a)):
            if i == 'L':
                locations_from_a[x] = mapped_instructions[locations_from_a[x]][0]
            elif i == 'R':
                locations_from_a[x] = mapped_instructions[locations_from_a[x]][1]

print("indexed:", index_true)

print("locations:", locations_with_a)
running_multi = [index_true[x] for x in index_true]
print("running multi:", running_multi)

lcm = running_multi[0]
for num in running_multi[1:]:
    lcm = lcm * num // math.gcd(lcm, num)
print("part 2:", lcm)
