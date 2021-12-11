checked = ["test"]

def grassFire(inputArray, startY, startX):
    print("Checking",startY,startX)
    if [startX,startY] in checked:
        print("bdrrrr")
    print("checked",checked)
    print("input",inputArray)

    if inputArray[startY][startX] < 9 and checked[startY][startX] == 0:
        checked[startY][startX] = 1
        if inputArray[startY+1][startX]<9:
            print("Going down",inputArray[startY+1][startX])
            grassFire(inputArray,startY+1,startX)
        if inputArray[startY][startX+1]<9:
            print("right")
            grassFire(inputArray,startY,startX+1)
        if inputArray[startY-1][startX]<9:
            print("down")
            grassFire(inputArray,startY-1,startX)
        if inputArray[startY][startX-1]<9:
            print("left")
            grassFire(inputArray,startY,startX-1)


with open('9.txt') as d:
    dataSplit = d.read().splitlines()
    maxNum = int(max(dataSplit))+1
    padding = [[maxNum for x in range(len(dataSplit[0])+2)]for y in range (len(dataSplit)+2)]
    for y in range(len(dataSplit)):
        for x in range(len(dataSplit[y])):
            padding[y+1][x+1] = int(dataSplit[y][x])

    riskLevel = 0
    for y in range(1,len(padding)-1):
        for x in range(1,len(padding[y])-1):
            tmp = padding[y][x]
            if tmp<(padding[y+1][x] and (padding[y-1][x]) and (padding[y][x+1]) and (padding[y][x-1])):
                riskLevel += tmp+1
    print(riskLevel)

    for y in range(1,len(padding)-1):
        for x in range(1,len(padding[y])-1):
            tmp = padding[y][x]
            if tmp<(padding[y+1][x] and (padding[y-1][x]) and (padding[y][x+1]) and (padding[y][x-1])):
                riskLevel += tmp+1
    checked = padding
    for y in range(len(checked)):
        for x in range(len(checked[y])):
            checked[y][x] = 0
    grassFire(padding,2,2)

print("checked",checked)

