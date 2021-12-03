with open('1.txt') as d:
    data = d.readlines()
    counter = -1
    current = 0

    for i in range (len(data)):
        if (int(data[i])>current):
            counter+=1
        current = int(data[i])

print("Total count: ",counter)