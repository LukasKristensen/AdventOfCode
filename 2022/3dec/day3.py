score = 0
for i in open('day3_data.txt').read().splitlines():
    first_bag, second_bag = i[round(len(i)/2):], i[:round(len(i)/2)]
    for x in first_bag:
        if x in second_bag:
            score += ord(x)-96 if x.islower() else ord(x)-38
            break
print("3a)",score)


score = 0
data = open('day3_data.txt').read().splitlines()
for i in range(round(len(data)/3)):
    for x in data[i*3]:
        if x in data[i*3+1] and x in data[i*3+2]:
            score += ord(x)-96 if x.islower() else ord(x)-38
            break
print("3b)",score)


