data = open('day6_data.txt').read().splitlines()[0]
first_task_found=False
for i in range(3, len(data)):
    seen_data = {}
    seen_data_second = {}
    for x in range(4):
        seen_data[data[i-x]] = 0
    for x in range(16):
        seen_data_second[data[i-x]] = 0
    if len(seen_data) == 4 and not first_task_found:
        first_task_found = True
        print("6a)",i+1)
    if len(seen_data_second) == 15:
        print("6b)",i+1)
        break

