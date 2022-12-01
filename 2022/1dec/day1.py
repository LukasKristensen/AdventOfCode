current_count = 0
elves = []

for i in open('day1_data.txt').read().splitlines():
    if i != '':
        current_count+=int(i)
    else:
        elves.append(current_count)
        current_count = 0

# 1a
print("1a)",max(elves))

# 1b
summed_three_most = 0
for i in range(3):
    biggest_val = max(elves)
    elves.remove(biggest_val)
    summed_three_most+=biggest_val
print("1b)",summed_three_most)


