data = open('day10_data.txt').read().splitlines()
cpu_cycles = [20, 60, 100, 140, 180, 220]
summed_signal_strength = 0
value = 1
cycle = 1

for i in data:
    command = i[:4]
    if command == "addx":
        cycle += 1
        if cycle in cpu_cycles:
            summed_signal_strength += value*cycle
        cycle += 1
        value += int(i.split(" ")[1])
        if cycle in cpu_cycles:
            summed_signal_strength += value*cycle
    else:
        cycle += 1
        if cycle in cpu_cycles:
            summed_signal_strength += value*cycle
print("10a)", summed_signal_strength)

screen = ["#", "", "", "", "", "", "","",""]

sprite = 1
cycle = 1
row = 0


def draw():
    global row
    if (cycle/40).is_integer():
        row += 1
    if sprite-1 <= cycle%40 <= sprite+1:
        screen[row] += "#"
    else:
        screen[row] += "."


for i in data:
    command = i[:4]
    if command == "addx":
        draw()
        cycle += 1
        sprite += int(i.split(" ")[1])
        draw()
        cycle += 1
    else:
        draw()
        cycle += 1

print("10b)")
for row in screen:
    print(row)


