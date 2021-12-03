with open('2.txt') as d:
    horizontal, depth = 0,0

    for i in d.readlines():
        data = i.split(" ")
        if data[0] == "forward":
            horizontal += int(data[1])
        if data[0] == "up":
            depth -= int(data[1])
        if data[0] == "down":
            depth += int(data[1])
    print(horizontal*depth)

