data = open('day5_data.txt').read().splitlines()
crates = {}

for i in range(round(len(data[0])/4)):
    crates[i] = []

for i in range(len(data)):
    if data[i] != "":
        for x in range(len(crates)):
            if '[' in data[i][x*4:(x+1)*4]:
                crates[x].append(data[i][x*4:(x+1)*4].replace(' ',''))

print("Crates:",crates)

for i in crates:
    print(crates[i])