data = open('day5_data.txt').read().splitlines()
crates = {}

for i in range(round(len(data[0])/4)):
    crates[i] = []

data_sorted = False
for i in range(len(data)):
    if data[i] != "":
        if not data_sorted:
            for x in range(len(crates)):
                if '[' in data[i][x*4:(x+1)*4]:
                    crates[x].append(data[i][x*4:(x+1)*4].replace(' ',''))
        else:
            _, amount, _, before, _, after = data[i].split(" ")
            for y in range(int(amount)):
                crates[int(after)-1].append(crates[int(before)-1].pop(-1))
            crates = crates[::-1]
            data_sorted = True
    else:
        for crate in range(len(crates)): crates[crate] = crates[crate][::-1]

result_a = ""
for x in crates:
    result_a += crates[x][-1].replace('[', '').replace(']', '')
print("5a)",result_a)



