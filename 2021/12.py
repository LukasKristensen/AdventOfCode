waysFound = []

def clearPath(arrayWays, toDelete):
    print("test")

def findWays(arrayWays, lastWay, pathTrace):
    for m in range(len(arrayWays)):
        if m < len(arrayWays)-1:
            if (arrayWays[m][0] == "end" and arrayWays[m][1] == lastWay) or (arrayWays[m][1] == "end" and arrayWays[m][0] == lastWay):
                waysFound.append(pathTrace)
                return
            elif arrayWays[m][0] == lastWay:
                tmpArray = arrayWays.copy()
                tmpArray.pop(m)
                pathTrace.append(tmpArray[m])
                findWays(tmpArray, arrayWays[m][1], pathTrace)
            elif arrayWays[m][1] == lastWay:
                tmpArray = arrayWays.copy()
                pathTrace.append(tmpArray[m])
                tmpArray.pop(m)
                findWays(tmpArray, arrayWays[m][0], pathTrace)


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
        findWays(middlePositions,arrayPos,[arrayPos])

    print("Found ways:")
    for i in waysFound:
        print(i)
    print("amount",len(waysFound))