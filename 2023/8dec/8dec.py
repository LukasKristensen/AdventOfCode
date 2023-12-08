import math
data_load = open("input.txt", "r").read().splitlines()
navigation, instructions = data_load[0], data_load[2:]
mapped_instructions = {}

for i in instructions:
    key, val = i.split(' = ')
    mapped_instructions[key] = {'L': val[1:-1].split(", ")[0], 'R': val[1:-1].split(", ")[1]}

current_location = 'AAA'
step_count1, step_count2 = 0, 0

while current_location != 'ZZZ':
    for i in navigation:
        step_count1 += 1
        current_location = mapped_instructions[current_location][i]

print("Part one:", step_count1)

locations = [{'origin': i, 'new': i, 'seed': 0} for i in mapped_instructions if i[-1] == 'A']

while 0 in [loc['seed'] for loc in locations]:
    for i in navigation:
        for g in range(len(locations)):
            if locations[g]['new'][-1] == 'Z' and locations[g]['seed'] == 0:
                locations[g]['seed'] = step_count2
        step_count2 += 1

        for x in range(len(locations)):
            locations[x]['new'] = mapped_instructions[locations[x]['new']][i]

collected_seeds = [x['seed'] for x in locations]
lcm = collected_seeds[0]

for num in collected_seeds[1:]:
    lcm = lcm * num // math.gcd(lcm, num)

print("Part two:", lcm)
