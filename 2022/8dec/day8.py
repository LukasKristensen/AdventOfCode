data = open('day8_data.txt').read().splitlines()
formatted = []
trees_visible = 0
max_scenic_score = 0

for i in range(len(data)):
    formatted.append([])
    for x in range(len(data[0])):
        formatted[i].append(int(data[i][x]))

for y in range(1, len(formatted) - 1):
    for x in range(1, len(formatted[0]) - 1):
        current_value = formatted[y][x]
        left_side, right_side, up_side, down_side = formatted[y][:x], formatted[y][x+1:], [], []

        for up in range(y):
            up_side.append(formatted[y - up - 1][x])
        for down in range(y, len(formatted[0]) - 1):
            down_side.append(formatted[down + 1][x])
        for i in [left_side, right_side, down_side, up_side]:
            if current_value > max(i):
                trees_visible += 1
                break

        scenic_score = 1
        tree_sight = []
        for i in [right_side, down_side, left_side[::-1], up_side]:
            tree_sight.append(0)
            for t in i:
                tree_sight[-1] += 1
                if current_value <= t:
                    break
            scenic_score *= tree_sight[-1]

        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print("8a)", trees_visible + len(formatted) * 2 + len(formatted[0]) * 2 - 4)
print("8b)", max_scenic_score)


