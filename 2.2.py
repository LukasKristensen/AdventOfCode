with open('2.txt') as d:
    horizontal, depth, aim = 0,0,0

    for i in d.readlines():
        data = i.split(" ")
        if data[0] == "forward":
            horizontal += int(data[1])
            depth += aim*int(data[1])
        if data[0] == "up":
            aim-=int(data[1])
        if data[0] == "down":
            aim+=int(data[1])
    print(horizontal*depth)

