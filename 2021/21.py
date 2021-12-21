p1pos, p2pos = 0, 0
p1points, p2points = 0,0
diceCount = 0
diceRolls = 0

with open('21.txt') as d:
    dataSplit = d.read().splitlines()
    formatArray = []
    for i in dataSplit:
        formatArray.append(i.split(" "))
    p1pos,p2pos = int(formatArray[0][4]), int(formatArray[1][4])

while p1points < 1000 and p2points < 1000:
    print("p1",p1pos,"p2",p2pos,"POINTS:",p1points,p2points)

    diceHold = diceCount*3+3
    diceCount += 3
    diceRolls += 3
    p1points += ((p1pos+diceHold) % 10)+1
    print("P1 Rolls:",((p1pos+diceHold)%10)+1)
    p1pos = ((p1pos+diceHold) % 10)+1

    if p1points > 999:
        print("test")
        break

    testHold = diceCount*3+3
    diceCount += 3
    diceRolls += 3
    print("Points before:",p2points)
    print("Rolled:",((p2pos+testHold) % 10)+1)
    p2points += ((p2pos+testHold) % 10)+1
    print("Points after:",p2points)
    p2pos = ((p2pos + testHold) % 10)+1


print("POS:",p1pos,p2pos,"SCORES:",p1points,p2points,"ROLLS:",diceRolls)