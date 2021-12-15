arrayRisk = []
riskTrack = []
stack = []
leastRisk = 0

def isvalid(y,x):
    return (y >= 0 and y<len(arrayRisk)) and (x >= 0 and x <len(arrayRisk[y]))

def walk(posY, posX, currentRisk):
    currentRisk += arrayRisk[posY][posX]

    if (riskTrack[posY][posX] > currentRisk) or (riskTrack[posY][posX] == -1):
        riskTrack[posY][posX] = currentRisk
    else:
        return

    checkY, checkX = isvalid(posY+1,posX), isvalid(posY,posX+1)
    if posY == len(arrayRisk)-1 and posX == len(arrayRisk[0])-1:
        global leastRisk
        if currentRisk < leastRisk or leastRisk == 0:
            print("Done!", currentRisk)
            leastRisk = currentRisk

    elif checkY and checkX:
        if arrayRisk[posY+1][posX] < arrayRisk[posY][posX+1]:
            walk(posY+1, posX, currentRisk)
        else:
            if checkX:
                walk(posY, posX+1, currentRisk)
    elif checkY:
        walk(posY + 1, posX, currentRisk)
    elif checkX:
        walk(posY, posX + 1, currentRisk)
    else:
        return



with open('15.txt') as d:
    dataSplit = d.read().splitlines()

    for l in range(len(dataSplit)):
        arrayRisk.append([])
        riskTrack.append([])
        for n in range(len(dataSplit[l])):
            arrayRisk[l].append(int(dataSplit[l][n]))
            riskTrack[l].append(-1)
    for i in arrayRisk:
        print (i)

    walk(0,0,0)

    for i in riskTrack:
        print (i)

    print("Least risk:",leastRisk)
