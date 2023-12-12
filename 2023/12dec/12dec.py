data_load = open("input.txt", "r").read().splitlines()
possibility_count = 0


def day_12(data, nums):
    global possibility_count
    nums = nums.split(",")
    possibilities, index_list, solutions = [], [], []

    for x in range(len(data)):
        if data[x] == "?":
            index_list.append(x)

    for x in range(2**len(index_list)):
        possibilities.append(data)
        for y in range(len(index_list)):
            if x & (1 << y):
                possibilities[x] = possibilities[x].replace("?", "#", 1)
            else:
                possibilities[x] = possibilities[x].replace("?", ".", 1)

    for x in possibilities:
        groups = [y for y in x.split(".") if y != ""]

        if len(groups) != len(nums):
            continue

        for g in range(len(groups)):
            if int(nums[g]) * "#" != groups[g]:
                break
            if g == len(groups)-1:
                possibility_count += 1


for i in data_load:
    data, nums = i.split(" ")
    day_12(data, nums)
print("Part 1:", possibility_count)

possibility_count = 0
for i in data_load:
    data, nums = i.split(" ")
    data = data+"?"+data+"?"+data+"?"+data+"?"+data
    nums = nums+","+nums+","+nums+","+nums+","+nums
    day_12(data, nums)
print("Part 2:", possibility_count)
