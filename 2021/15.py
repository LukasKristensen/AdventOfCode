arrayRisk, riskTrack = [], []
leastRisk = 0

def isvalid(y,x):
    return (0 <= y < len(arrayRisk)) and (0 <= x < len(arrayRisk[y]))

def walk(posY, posX, currentRisk):
    if posY+posX != 0:
        currentRisk += arrayRisk[posY][posX]

    if (riskTrack[posY][posX] > currentRisk) or (riskTrack[posY][posX] == -1):
        riskTrack[posY][posX] = currentRisk
    else:
        return

    checkY, checkX = isvalid(posY+1,posX), isvalid(posY,posX+1)
    if posY == len(arrayRisk)-1 and posX == len(arrayRisk[0])-1:
        global leastRisk
        if currentRisk < leastRisk or leastRisk == 0:
            leastRisk = currentRisk
    if checkY: walk(posY + 1, posX, currentRisk)
    if checkX: walk(posY, posX + 1, currentRisk)

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
    walk(0,0,-1)
    print("Least risk:",leastRisk)

