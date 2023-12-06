data_load = open("input.txt", "r").read().splitlines()
seeds = [int(x) for x in data_load[0].split(": ")[-1].split(" ")]
mapped_val, collected_maps = [], []

for index, i in enumerate(data_load[2:]):
    if ':' in i:
        mapped_val = []
    elif i != "":
        mapped_val.append([int(x) for x in i.split(" ")])
    if i == "" or index == len(data_load[2:])-1:
        collected_maps.append(mapped_val)


part_one = []
for seed in seeds:
    tmp_num = int(seed)
    for x in collected_maps:
        for map_val in x:
            if map_val[1] <= tmp_num <= map_val[1]+map_val[2]:
                tmp_num = map_val[0]-map_val[1]+tmp_num
                break
    part_one.append(tmp_num)
print("Part one:", min(part_one))

