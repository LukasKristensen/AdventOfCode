with open('6.txt') as d:
    data = d.read().splitlines()
    data = data[0].split(",")
    dictionary = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    newFish = 0
    toAppend = 0

    for i, x in enumerate(data):
        dictionary[int(x)] += 1


    for i in range(80):
        print(i)
        print(dictionary)
        for x in range(9):
            if x == 0:
                dictionary[8] = dictionary[0]
                dictionary[6] = dictionary[0]
            else:
                dictionary[x-1] = dictionary[x]
    sumTotal = sum(dictionary.values())

    print("sumTotal",sumTotal)
    print (dictionary)

    print(len(data))


