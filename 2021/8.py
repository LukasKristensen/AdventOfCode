with open('8.txt') as d:
    dataSplit = d.read().splitlines()
    counter = 0
    output2 = 0

    for i in dataSplit:
        tmpOutput = ((i.split(" | "))[1].split(" "))
        segments = ["cf", "bcdf", "acf", "abcdefg"]
        for x in tmpOutput:
            for z in segments:
                if len(x)==len(z):
                    counter+=1

    for i in dataSplit:
        tmpOutput = ((i.split(" | "))[1].split(" "))
        segments = ["cf", "bcdf", "acf", "abcdefg"]

        tmpHold = ""
        tmpOutput = ((i.split(" | "))[1].split(" "))
        segments = {"cagedb": 0,"ab":1,"gcdfa":2,"fbcad":3,"eafb":4,"cdfbe":5,"cdfgeb":6,"dab":7,"acedgfb":8,"cefabd":9}
        for x in tmpOutput:
            for z in segments:
                if sorted(x) == sorted(z):
                    tmpHold+=str(segments[z])
        if tmpHold != "":
            output2+=int(tmpHold)
    print(counter)