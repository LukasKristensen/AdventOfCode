def runData(inputData, inputDictionary):
    tmpHold = ""

    for i in range(len(inputData)):
        tmpHold+=(inputData[i])
        if inputData[i:i+2] in inputDictionary:
            tmpHold+=(inputDictionary[inputData[i:i+2]])
        print("no")
    return tmpHold

def getMostFrequent(inputData):
    dictionary = {}
    for i in inputData:
        if i not in dictionary: dictionary[i] = 1
        else: dictionary[i] += 1
    return dictionary[max(dictionary)]-dictionary[min(dictionary, key=dictionary.get)]

with open('14.txt') as d:
    dataSplit = d.read().splitlines()
    dataRead, dataDict = dataSplit[0], dataSplit[2:]
    dictionary = {}

    for i in dataDict:
        tmpHold = i.split(" -> ")
        dictionary[tmpHold[0]] = tmpHold[1]
    for i in range(10):
        dataRead = runData(dataRead, dictionary)
        print("Iteration",i,dataRead)

    print("result:",getMostFrequent(dataRead))

