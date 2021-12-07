with open('1.txt') as d:
    data = d.readlines()

    count = 0
    sumPrev = 0

    for i in range(2, len(data)):
        current = int(data[i])+int(data[i-1])+int(data[i-2])
        if current > sumPrev and i > 2:
            count+=1
        sumPrev = current

print("Count:",count)


