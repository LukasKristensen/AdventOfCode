with open('4.txt') as d:
    data = d.read().splitlines()

drawnNumbers, boards, boardsArray, drawnOut, boardsWon, numbersArray = data[0], data[2:], [], [], [], data[0].split(",")

for i, board in enumerate(boards):
    tempHold = board.split()
    boardsArray.append(tempHold)
    for x, num in enumerate(tempHold):
        boardsArray[i][x] = int(num)

def calculateResult(arrayWon, latestDrawn, boardNumber, checkIfFirst):
    if boardNumber not in boardsWon:
        sumHit = 0
        for row in arrayWon:
            for i in row:
                if i not in drawnOut:
                    sumHit += int(i)
        if checkIfFirst and (len(boardsWon) == 0) or (not checkIfFirst and (len(boardsWon) >= (len(boardsArray)/6)-1)):
            print("FinalResult",int(latestDrawn)*int(sumHit))
        boardsWon.append(boardNumber)

def checkIfBingo(row):
    for i in row:
        if i not in drawnOut:
            return False
    return True

for drawn in numbersArray:
    drawnOut.append(int(drawn))
    for y in range(len(boardsArray)):
        for x in range(len(boardsArray[0])):
            if ((y+1) % 6) == 0:
                pass
            elif int(drawn) == (boardsArray[y][x]):
                ifBingo = checkIfBingo(boardsArray[y])
                column = []
                for i in range (5):
                    column.append(boardsArray[y-(y%6)+i][x])
                if not ifBingo:
                    ifBingo = checkIfBingo(column)
                if ifBingo:
                    calculateResult(boardsArray[y - (y % 6):y - (y % 6) + 5], drawn, y - (y % 6), False)
            else:
                pass


