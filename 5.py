with open('5.txt') as d:
    data = d.read().splitlines()
    newData = []
    horizonVertical = []
    dictionaryCoordinates = {}
    for i in data:
        tmpData = i.split(" -> ")
        newData.append([(tmpData[0].split(",")),(tmpData[1].split(","))])
    for i in range(len(newData)):
        if (newData[i][0][0] == newData[(i)][1][0]) or (newData[i][0][1] == newData[(i)][1][1]):
            horizonVertical.append(newData[i])
    for i in horizonVertical:
        elementNotEqual = 1 if int(i[0][0]) == int(i[1][0]) else 0

    print(horizonVertical)
    print(dictionaryCoordinates)