with open('5.txt') as d:
    data = d.read().splitlines()
    newData = []
    horizonVertical = []
    dictionaryCoordinates = {}
    tmpCoordinates = [[0 for x in range(1000)]for y in range (1000)]
    for i in data:
        tmpData = i.split(" -> ")
        firstInp, secondInp =(tmpData[0].split(",")),(tmpData[1].split(","))
        newData.append([[int(firstInp[0]), int(firstInp[1])], [int(secondInp[0]), int(secondInp[1])]])
    for i in range(len(newData)):
        if (newData[i][0][0] == newData[(i)][1][0]) or (newData[i][0][1] == newData[(i)][1][1]):
            horizonVertical.append(newData[i])

    print(horizonVertical)
    print(dictionaryCoordinates)