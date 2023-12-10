import math
data_load = open("input.txt", "r").read().splitlines()

start_pos = [0, 0]

for y in range(len(data_load)):
    for x in range(len(data_load[y])):
        if data_load[y][x] == 'S':
            start_pos = [y, x]

directions = {'|D': 'D', '|U': 'U',
              '-R': 'R', '-L': 'L',
              'LD': 'R', 'LL': 'U',
              'JD': 'L', 'JR': 'U',
              '7R': 'D', '7U': 'L',
              'FL': 'D', 'FU': 'R',
              }

print("Start position:", start_pos)


def move(current_pos, prev_move):
    next_move = directions[str(data_load[current_pos[0]][current_pos[1]])+prev_move]
    if next_move == 'R':
        current_pos[1] += 1
    elif next_move == 'L':
        current_pos[1] -= 1
    elif next_move == 'D':
        current_pos[0] += 1
    elif next_move == 'U':
        current_pos[0] -= 1
    return next_move


current_pos_a = start_pos.copy()
current_pos_a[1] += 1
prev_move_a = 'R'

current_pos_b = start_pos.copy()
current_pos_b[1] -= 1
prev_move_b = 'L'

count = 1

loop_map = []
for y in range(len(data_load)):
    loop_map.append(["o"]*len(data_load[y]))

while True:
    count += 1
    prev_move_a = move(current_pos_a, prev_move_a)
    prev_move_b = move(current_pos_b, prev_move_b)

    loop_map[current_pos_a[0]][current_pos_a[1]] = "x"
    loop_map[current_pos_b[0]][current_pos_b[1]] = "x"

    if current_pos_a == current_pos_b:
        print("Part A:", count)
        break


coord_checked = []


def fire_spread(y, x):
    try:
        if 0 <= y <= len(loop_map) and 0 <= x <= len(loop_map):
            if loop_map[y][x] == "o":
                loop_map[y][x] = "."
            else:
                return
            if [y, x+1] not in coord_checked:
                fire_spread(y, x+1)
            if [y, x-1] not in coord_checked:
                fire_spread(y, x-1)
            if [y-1, x] not in coord_checked:
                fire_spread(y-1, x)
            if [y+1, x] not in coord_checked:
                fire_spread(y+1, x)
            if [y+1, x+1] not in coord_checked:
                fire_spread(y+1, x+1)
            if [y-1, x-1] not in coord_checked:
                fire_spread(y-1, x-1)
            if [y-1, x+1] not in coord_checked:
                fire_spread(y+1, x+1)
            if [y-1, x+1] not in coord_checked:
                fire_spread(y-1, x-1)
        coord_checked.append([y, x])
    except:
        pass


for y in range(len(loop_map)):
    for x in range(len(loop_map)):
        fire_spread(y, 0)

for y in range(len(loop_map)):
    for x in range(len(loop_map)):
        fire_spread(y, len(loop_map[y])-1)

for x in range(len(loop_map[0])):
    for y in range(len(loop_map[x])):
        if loop_map[len(loop_map)-y-1][x] == "x":
            break
        fire_spread(len(loop_map)-y-1, x)


part_b = 0
for y in range(len(loop_map)):
    for x in range(len(loop_map[y])):
        if loop_map[y][x] == 'o':
            part_b += 1

print("Part B:", math.floor(part_b/2))

