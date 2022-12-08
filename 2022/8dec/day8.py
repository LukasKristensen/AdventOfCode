data = open('day8_validation.txt').read().splitlines()
formatted = []

for i in range(len(data)):
    formatted.append([])
    for x in range(len(data[0])):
        formatted[i].append(int(data[i][x]))

data = formatted
print("Formatted:",formatted)

print("Showed")
for z in formatted:
    print(z)

trees_visible = 0

for y in range(1, len(data) - 1):
    for x in range(1, len(data[0])-1):
        up_visible = True
        down_visible = True
        left_visible = True
        right_visible = True

        print("Data:",data)

        current_value = data[y][x]
        left_side = data[y][:x]
        right_side = data[y][x+1:]
        up_side = []
        down_side = []

        print("Coordinate:","X:",x,"Y:",y)
        print("Left side:",left_side)
        print("Right side:",right_side)

        for up in range(y):
            up_side.append(data[y-up-1][x])
        for down in range(y, len(data[0])-y):
            down_side.append(data[y+down][x])

        print("Up side:",up_side)
        print("down side:",down_side)

        visible = False
        for i in [left_side, right_side, down_side, up_side]:
            if current_value < max(i):
                trees_visible += 1
                break


print("Summed visible:",trees_visible)

# 7855 too high