data_load = open("input.txt", "r").read().splitlines()
print("Data:", data_load)
possibilities_nums = []

for i in range(len(data_load)):
    print("Line:", i, "of", len(data_load))
    i = data_load[i]

    data, nums = i.split(" ")
    nums = nums.split(",")
    print("Data:", data, "nums:", nums)

    possibilities = []
    index_list = []

    # Get all indexes which can have different solutions
    for x in range(len(data)):
        if data[x] == "?":
            index_list.append(x)

    # Get all possible solutions where each ? is replaced by 0 or 1 while keeping the remaining data
    for x in range(2**len(index_list)):
        possibilities.append(data)
        for y in range(len(index_list)):
            if x & (1 << y):
                possibilities[x] = possibilities[x].replace("?", "#", 1)
            else:
                possibilities[x] = possibilities[x].replace("?", ".", 1)

    possibility_count = 0
    solutions = []
    for x in possibilities:
        temp_nums = nums.copy()
        groups = x.split(".")

        new_groups = []
        # remove all empty groups
        for y in groups:
            if y != "":
                new_groups.append(y)
        groups = new_groups

        if len(groups) != len(temp_nums):
            continue

        solution_found = True
        # Check if the amount of # is equal to the amount of nums
        for g in range(len(groups)):
            if int(nums[g]) * "#" != groups[g]:
                solution_found = False
                break
        if solution_found:
            print("FOUND SOLUTION:", x)
            possibility_count += 1
    possibilities_nums.append(possibility_count)

print("possibilities:", possibilities_nums)
print("Sum:", sum(possibilities_nums))