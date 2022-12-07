data = open('day7_data.txt').read().splitlines()
sum = 0
current_dir = []
folders_checked = {}

for i in range(0, len(data)):
    print(i,data[i])
    command = data[i]
    print("Command:",command)

    if "$ cd" in command:
        new_dir = command.split(" ")[-1]
        if new_dir == "..":
            current_dir.pop(-1)
        else:
            current_dir.append(command.split(" ")[-1])
        print("New dir:",current_dir)

    if command == "$ ls" and len(current_dir)>1:
        dir_size = 0
        i+=1
        print("Check if:", data[i].split(" ")[0])
        while data[i].split(" ")[0].isdigit():
            print("Appending size:",int(data[i].split(" ")[0]))
            dir_size += int(data[i].split(" ")[0])
            if i+1 < len(data):
                i += 1
            else:
                break
        print("Final dir size:",dir_size)

        previous_folders = []
        for x in current_dir:
            previous_folders.append(x)
            if x not in folders_checked:
                folders_checked["".join(previous_folders)] = dir_size
            else:
                folders_checked["".join(previous_folders)] += dir_size

print("Folders:",folders_checked)
gotten = []

for i in folders_checked:
    for y in gotten:
        print("Checkijng if:", i, "In:", y)
        if y in i:
            print("Found:",i,"In:",y)
            continue
    print(i, folders_checked[i])
    if folders_checked[i] <= 100000:
        sum += folders_checked[i]
        gotten.append(i)

print("SUM:",sum)

# 142652 too high
# 2138415
