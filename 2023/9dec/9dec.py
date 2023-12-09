data_load = open("input.txt", "r").read().splitlines()
data_formatted = [list(map(int, i.split(" "))) for i in data_load]

final_differences = []
for i in range(len(data_formatted)):
    differences = [data_formatted[i]]
    while differences[-1] != [0]*len(differences[-1]):
        differences.append([int(differences[-1][x])-int(differences[-1][x-1]) for x in range(1, len(differences[-1]))])
    final_differences.append(differences)

for i in range(len(final_differences)):
    for x in range(1, len(final_differences[i])):
        final_differences[i][-1-x].append(final_differences[i][-1-x][-1]+final_differences[i][-x][-1])
        final_differences[i][-1-x] = [final_differences[i][-1-x][0]-final_differences[i][-x][0]] + final_differences[i][-1-x]

print("Part one:", sum([i[0][-1] for i in final_differences]))
print("Part two:", sum([i[0][0] for i in final_differences]))
