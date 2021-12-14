def fold(arrayInput, foldInput, maxY, maxX):
    tmpNew = []
    print("foldinput:",foldInput)
    if foldInput[11] == "x":
        tmpFlip = foldInput.split("=")
        for x in arrayInput:
            tmpHold = x.split(",")
            if int(tmpHold[0]) < int(maxX)/2:
                tmpNew.append([tmpFlip[1]-tmpHold[0]],[tmpHold[1]])
    else:
        tmpFlip = foldInput.split("=")
        for x in arrayInput:
            tmpHold = x.split(",")
            if tmpHold[0] < maxX/2:
                tmpNew.append([tmpFlip[1]-tmpHold[0],tmpHold[1]])
    return tmpNew


with open('13.txt') as d:
    dataSplit = d.read().splitlines()
    coordinates, folds = [], []
    maxX, maxY = 0,0

    for i in range(len(dataSplit)):
        if dataSplit[i] == "":
            coordinates, folds = dataSplit[:i], dataSplit[i+1:]
    print(coordinates)
    print(folds)

    for i in coordinates:
        x,y = i.split(",")
        if int(x) > maxX: maxX = int(x)
        if int(y) > maxY: maxY = int(y)

    for i in folds:
        fold(dataSplit, i, maxY, maxX)