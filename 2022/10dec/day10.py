cpu_cycles = [-20+x*40 for x in range(1, 6)]
screen = ["" for x in range(6)]
summed_signal_strength, value, cycle, row = 0, 1, 0, -1


def draw():
    global row, cycle, summed_signal_strength
    if (cycle / 40).is_integer():
        row += 1
    if value - 1 <= cycle % 40 <= value + 1:
        screen[row] += "\033[32m▓▓"
    else:
        screen[row] += "\033[31m░░"
    cycle += 1
    if cycle in cpu_cycles:
        summed_signal_strength += value * cycle


for i in open('day10_data.txt').read().splitlines():
    draw()
    if i[:4] == "addx":
        draw()
        value += int(i.split(" ")[1])

print(f'10a) {summed_signal_strength}', "10b)",*screen,sep="\n")

