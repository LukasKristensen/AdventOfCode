with open('1.txt') as d:
    data = (d.read().splitlines())
    [print(int(x)*int(y)) for x in data for y in data if (int(x)+int(y)==2020) and x>y]
    [print(int(x)*int(y)*int(z)) for x in data for y in data for z in data if (int(x)+int(y)+int(z)==2020) and x>y>z]


[print(int(x)*int(y)) for x in open("1.txt").read().split("\n") for y in open("1.txt").read().split("\n")  if ((int(x)+int(y)==2020) and x > y)]
[print(int(x)*int(y)*int(z)) for x in open("1.txt").read().split("\n") for y in open("1.txt").read().split("\n") for z in open("1.txt").read().split("\n") if ((int(x)+int(y)+int(z)==2020) and x > y > z)]
