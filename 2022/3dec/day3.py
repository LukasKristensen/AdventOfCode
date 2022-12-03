print(ord("a"))
print(ord("b"))
print(ord("A"))

print("A".islower())

score = 0
for i in open('day3_data.txt').read().splitlines():
    first_bag, second_bag = i[:round(len(i)/2)], i[round(len(i)/2):]
    for x in first_bag:
        if x in second_bag:
            if x.islower():
                score+=ord(x)-96
            else:
                score+=ord(x)-38
            break
print("3a)",score)

