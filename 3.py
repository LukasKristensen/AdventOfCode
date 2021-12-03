with open('3.txt') as d:
    gamma, epsilon = [], []
    deciGamma, deciEpsilon = 0,0
    data = d.readlines()

    for x in range(len(data[0])-1):
        sum = 0
        for y in range(len(data)):
            if data[y][x] != '\n':
                sum += int(data[y][x])
        if sum <= len(data)/2:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)

    for i in range (len(gamma)):
        deciGamma += gamma[i]*pow(2, len(gamma)-i-1)
        deciEpsilon += epsilon[i]*pow(2, len(gamma)-i-1)
    print(deciGamma*deciEpsilon)


