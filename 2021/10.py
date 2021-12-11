with open('10.txt') as d:
    dataSplit = d.read().splitlines()
    dictSyntax = {")": "(", "]": "[", "}": "{", ">": "<"}
    inverseDict = {"(": ")", "[": "]", "{": "}", "<": ">"}
    checkOpen = ["(", "[","{","<"]
    expectedPoitns = {")":3, "]":57, "}":1197, ">":25137}
    sumPoints = 0
    print("lengthData",len(dataSplit))

    for s in dataSplit:
        tmpStack = []

        for x, c in enumerate (s):
            print("x c",x,c,"bdrr",s)
            if c in checkOpen:
                tmpStack.append(c)
            else:
                if tmpStack[len(tmpStack)-1] == dictSyntax[c]:
                    tmpStack.pop()
                else:
                    sumPoints += expectedPoitns[inverseDict[tmpStack[len(tmpStack)-1]]]
                    print("breaking")
                    break
        print("Completed")
    print("sum",sumPoints)
