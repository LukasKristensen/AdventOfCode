import time

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


def search_mappings(seed):
    tmp_num = seed
    for x in collected_maps:
        for map_val in x:
            if map_val[1] <= tmp_num <= map_val[1] + map_val[2]:
                tmp_num = map_val[0] - map_val[1] + tmp_num
                break
    return tmp_num


part_one = max(seeds)
for seed in seeds:
    best_seed = search_mappings(seed)
    if best_seed < part_one:
        part_one = best_seed
print("Part one:", part_one)


part_two = max(seeds)
optimal_seed = [0,0]

start_part_two = time.time()
for i in range(int(len(seeds)/2)):
    seed_start, seed_interval = seeds[i*2], seeds[i*2+1]
    for seed in range(int(seed_start), int(seed_start)+int(seed_interval), 100000):
        best_seed = search_mappings(seed)
        if best_seed < part_two:
            part_two = best_seed
            optimal_seed[0] = seed_start
            optimal_seed[1] = seed_start+seed_interval


for i in [10000, 1000, 100, 10, 1]:
    for seed in range(optimal_seed[0], optimal_seed[1], i):
        best_seed = search_mappings(seed)
        if best_seed < part_two:
            part_two = best_seed
            if seed-i > optimal_seed[0]:
                optimal_seed[0] = seed-i
            if seed+i < optimal_seed[1]:
                optimal_seed[1] = seed+i

print("Part two:", part_two)
print("Computation time:", time.time()-start_part_two, "seconds")
