print("1a)",sum([1 if i == "(" else -1 for i in open('day1_data.txt').read().splitlines()[0]]))

floor, i = 0, 0
data = open('day1_data.txt').read().splitlines()[0]
while floor > -1:
    if data[i] == "(":
        floor += 1
    else:
        floor -= 1
    i += 1
print("1b)",i)

