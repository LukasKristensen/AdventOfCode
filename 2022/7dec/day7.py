data = open('day7_data.txt').read().splitlines()
current_dir, folders_checked = [], {}

for i in range(0, len(data)):
    command = data[i]
    if "$ cd" in command:
        new_dir = command.split(" ")[-1]
        if new_dir == "..":
            current_dir.pop(-1)
        else:
            current_dir.append(command.split(" ")[-1])
    if command == "$ ls":
        dir_size = 0
        i += 1
        while data[i].split(" ")[0].isdigit() or data[i].split(" ")[0] == "dir":
            if data[i].split(" ")[0].isdigit():
                dir_size += int(data[i].split(" ")[0])
            if i+1 < len(data):
                i += 1
            else:
                break
        previous_folders = []
        for x in current_dir:
            previous_folders.append(x)
            if "".join(previous_folders) not in folders_checked:
                folders_checked["".join(previous_folders)] = dir_size
            else:
                folders_checked["".join(previous_folders)] += dir_size

space_to_delete = folders_checked['/']-40000000
smallest_dir_for_deletion = 40000000
summed_below_threshold = 0

for i in folders_checked:
    if folders_checked[i] <= 100000:
        summed_below_threshold += folders_checked[i]
    if smallest_dir_for_deletion > folders_checked[i] >= space_to_delete:
        smallest_dir_for_deletion = folders_checked[i]

print("7a):", summed_below_threshold)
print("7b):", smallest_dir_for_deletion)


