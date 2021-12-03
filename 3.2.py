with open('3.txt') as d:
    data = d.read().splitlines()


def findRating(arrayInput, ifGenerator):
    for y in range(len(arrayInput[0])):
        if len(arrayInput) == 1:
            return int(arrayInput[0], 2)
        totalSum, mostCommon = 0, 0
        tempArray = []

        for x in range(len(arrayInput)):
            totalSum += int(arrayInput[x][y])
            if totalSum < len(arrayInput)/2:
                mostCommon = 0 if ifGenerator else 1
            else:
                mostCommon = 1 if ifGenerator else 0

        for x in range(len(arrayInput)):
            if int(arrayInput[x][y]) == int(mostCommon):
                tempArray.append(arrayInput[x])
        arrayInput = tempArray
    return int(arrayInput[0], 2)


generatorBinary = findRating(data, True)
scrubberBinary = findRating(data, False)
print(generatorBinary*scrubberBinary)

