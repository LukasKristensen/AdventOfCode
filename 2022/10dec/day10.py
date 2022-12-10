data = open('day10_data.txt').read().splitlines()
cycles_check = [20, 60, 100, 140, 180, 220]

summed_signal_strength = 0
value = 1
cycle = 1
for i in data:
    command = i[:4]
    if command == "addx":
        cycle += 1
        if cycle in cycles_check:
            summed_signal_strength += value*cycle
        cycle += 1
        value += int(i.split(" ")[1])
        if cycle in cycles_check:
            summed_signal_strength += value*cycle
    else:
        cycle += 1
        if cycle in cycles_check:
            summed_signal_strength += value*cycle
print(summed_signal_strength)


# 14040 too low
# 14760 too high

