max_count = 0
current_count = 0

for i in open('day1_data.txt').read().splitlines():
    if i != '':
        current_count+=int(i)
    else:
        if current_count > max_count:
            max_count = current_count
        current_count = 0
print("Max count:",max_count)