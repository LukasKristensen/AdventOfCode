dumboArray = []
flashCount = 0
checkIfNotFlashed = []
arrayCheck = [[-1,-1],[-1,0],[-1,1]]


def isvalid(y,x):
    return (y >= 0 and y<len(dumboArray)) and (x >= 0 and x <len(dumboArray[y]))

def setTrue():
    for y in range(len(dumboArray)):
        for x in range(len(dumboArray[y])):
            checkIfNotFlashed[y][x] = 1

def flash(y,x):
    global flashCount
    flashCount += 1

    for g in range (3):
        for i in arrayCheck:
            if isvalid(y+i[0]+g,x+i[1]):
                energyGain(y + i[0]+g, x + i[1])

    dumboArray[y][x] = 0
    checkIfNotFlashed[y][x] = 0


def energyGain(y,x):
    if dumboArray[y][x] < 9 and checkIfNotFlashed[y][x] == 1:
        dumboArray[y][x]+=1
    else:
        if checkIfNotFlashed[y][x] == 1:
            checkIfNotFlashed[y][x] = 0
            flash(y,x)

def simulate():
    iterationCount = 0
    while True:
        iterationCount+=1
        setTrue()
        for y in range(len(dumboArray)):
            for x in range(len(dumboArray[y])):
                energyGain(y,x)

        if iterationCount == 100:
            print("Part1:",flashCount)

        anyTrue = any(any(row) for row in checkIfNotFlashed)

        if not anyTrue:
            print("Part2:",iterationCount)
            break

with open('11.txt') as d:
    dataSplit = d.read().splitlines()
    for y in range(len(dataSplit)):
        dumboArray.append([])
        checkIfNotFlashed.append([])
        for x in range(len(dataSplit[y])):
            dumboArray[y].append(int(dataSplit[y][x]))
            checkIfNotFlashed[y].append(1)

    simulate()
