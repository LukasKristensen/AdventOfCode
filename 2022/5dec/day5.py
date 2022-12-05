import copy
data = open('day5_data.txt').read().splitlines()
crates = {}
crates_second = {}

for i in range(round(len(data[0])/4)):
    crates[i] = []

for i in range(len(data)):
    if data[i] != "":
        if not crates_second:
            for x in range(len(crates)):
                if '[' in data[i][x*4:(x+1)*4]:
                    crates[x].append(data[i][x*4:(x+1)*4].replace(' ',''))
        else:
            _, amount, _, before, _, after = data[i].split(" ")
            for y in range(int(amount)):
                crates[int(after)-1].append(crates[int(before)-1].pop(-1))
            crates_second[int(after)-1]+=crates_second[int(before)-1][-int(amount):]
            crates_second[int(before)-1] = crates_second[int(before)-1][:-int(amount)]
    else:
        for crate in range(len(crates)): crates[crate] = crates[crate][::-1]
        crates_second = copy.deepcopy(crates)

result_a, result_b = "", ""
for x in crates:
    result_a += crates[x][-1].replace('[', '').replace(']', '')
    result_b += crates_second[x][-1].replace('[', '').replace(']', '')
print("5a)",result_a)
print("5b)",result_b)



