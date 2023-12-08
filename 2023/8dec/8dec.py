import math
data_load = open("input.txt", "r").read().splitlines()
navigation = data_load[0]
instructions = data_load[2:]
mapped_instructions = {}

for i in instructions:
    key, val = i.split(' = ')
    mapped_instructions[key] = val[1:-1].split(", ")

current_location = 'AAA'
step_count1, step_count2 = 0, 0
part_one = None

while not part_one:
    if current_location == 'ZZZ':
        part_one = step_count1
    for i in navigation:
        step_count1 += 1
        if i == 'L':
            current_location = mapped_instructions[current_location][0]
        elif i == 'R':
            current_location = mapped_instructions[current_location][1]
print("Part one:", part_one)

index_true = {}
locations_with_a = [i for i in mapped_instructions if i[-1] == 'A']
locations_from_a = locations_with_a.copy()

while len(index_true) != len(locations_with_a):
    for i in navigation:
        for g in range(len(locations_from_a)):
            if locations_from_a[g][-1] == 'Z' and locations_with_a[g] not in index_true:
                index_true[locations_with_a[g]] = step_count2
        step_count2 += 1

        for x in range(len(locations_from_a)):
            if i == 'L':
                locations_from_a[x] = mapped_instructions[locations_from_a[x]][0]
            elif i == 'R':
                locations_from_a[x] = mapped_instructions[locations_from_a[x]][1]


running_multi = [index_true[x] for x in index_true]
lcm = running_multi[0]

for num in running_multi[1:]:
    lcm = lcm * num // math.gcd(lcm, num)

print("Part two:", lcm)
