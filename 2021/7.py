def fuelCalculate(num):
    return (num*num+num)/2

with open('7.txt') as d:
    data = (d.read().splitlines())[0].split(",")
    data = [int(toString) for toString in data]

    smallestSum = 0

    for x in range (max(data)):
        sumX = [fuelCalculate(abs(int(i)-int(x))) for i in data]
        if sum(sumX)<smallestSum or smallestSum == 0: smallestSum=sum(sumX)
    print(smallestSum)

