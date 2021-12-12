waysFound = []

def clearPath(arrayWays, toDelete):
    i = 0
    while i < len(arrayWays):
        if (arrayWays[i][0] == toDelete) or (arrayWays[i][1] == toDelete):
            arrayWays.pop(i)
        else:
            i+=1
    return arrayWays


iterations = 0

def findWays(arrayWays, lastWay, pathTrace):
    print("new iteration:",pathTrace)
    global iterations
    iterations+=1
    if lastWay[0].islower() and len(pathTrace)>1:
        print("Running destroy")
        arrayWays = clearPath(arrayWays, lastWay)

    for m in range(len(arrayWays)):
        tmpArray = arrayWays.copy()
        if m < len(tmpArray)-1:
            if (tmpArray[m][0] == "end" and tmpArray[m][1] == lastWay) or (tmpArray[m][1] == "end" and tmpArray[m][0] == lastWay):
                waysFound.append(pathTrace+tmpArray[m])
                continue
            elif tmpArray[m][0] == lastWay:
                tmpArray.pop(m)
                findWays(tmpArray, tmpArray[m][1], pathTrace+tmpArray[m])
            elif tmpArray[m][1] == lastWay:
                tmpArray.pop(m)
                findWays(tmpArray, arrayWays[m][0], pathTrace+tmpArray[m])
    print("Ended search")


with open('12.txt') as d:
    dataSplit = d.read().splitlines()
    formatArray = []
    for i in dataSplit:
        formatArray.append(i.split("-"))

    startPositions = []
    endPositions = []
    middlePositions = []

    for i in formatArray:
        if i[0] == "start" or i[1] == "start":
            startPositions.append(i)
        else:
            middlePositions.append(i)

    print("START", startPositions)
    print("MIDDLE", middlePositions)
    print("END", endPositions)

    for s in startPositions:
        arrayPos = s[1] if s[0] == "start" else s[0]
        print("Running:",s)
        findWays(middlePositions,arrayPos,[arrayPos])

    print("Found ways:")
    for i in waysFound:
        print(i)
    print(iterations,"amount",len(waysFound))