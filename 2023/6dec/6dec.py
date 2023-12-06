data_load = open("input.txt", "r").read().splitlines()
time = [int(x) for x in data_load[0].split(':')[-1].split(" ") if x != ""]
distance = [int(x) for x in data_load[1].split(':')[-1].split(" ") if x != ""]


def race_simulate(time, distance):
    result = 1
    for race in range(len(time)):
        options = 0
        for i in range(int(time[race])):
            record = i*(int(time[race])-i)
            if int(distance[race]) < record:
                options += 1
        result *= options if options > 0 else 1
    return result


print("Part one:", race_simulate(time, distance))
print("Part two:", race_simulate(["".join(str(x) for x in time)], ["".join(str(x) for x in distance)]))

