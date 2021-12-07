with open('2.txt') as d:
    data = (d.read().splitlines())
    validChecks = 0
    for i in data:
        tmpHold = i.split(" ")
        tmpHold[0] = tmpHold[0].split("-")

        toCheck = tmpHold[1][0]
        counter = 0
        for x in tmpHold[2]:
            if toCheck == x:
                counter+=1
        if (counter >= int(tmpHold[0][0])) and (int(tmpHold[0][1]) >= counter):
            validChecks += 1
    print(validChecks)

