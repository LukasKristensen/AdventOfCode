import tkinter as tk
from tkinter import *
import time
import random
iterationData = []
dumboArray = []
flashCount = 0
checkIfNotFlashed = []
arrayCheck = [[-1,-1],[-1,0],[-1,1]]


def isvalid(y,x):
    return (y >= 0 and y<len(dumboArray)) and (x >= 0 and x <len(dumboArray[y]))

def setTrue():
    for y in range(len(dumboArray)):
        for x in range(len(dumboArray[y])):
            checkIfNotFlashed[y][x] = 1

def flash(y,x):
    global flashCount
    flashCount += 1

    for g in range (3):
        for i in arrayCheck:
            if isvalid(y+i[0]+g,x+i[1]):
                energyGain(y + i[0]+g, x + i[1])

    dumboArray[y][x] = 0
    checkIfNotFlashed[y][x] = 0


def energyGain(y,x):
    if dumboArray[y][x] < 9 and checkIfNotFlashed[y][x] == 1:
        dumboArray[y][x]+=1
    else:
        if checkIfNotFlashed[y][x] == 1:
            checkIfNotFlashed[y][x] = 0
            flash(y,x)

def simulate():
    iterationCount = 0
    while True:
        global iterationData
        if iterationCount <= 100:
            iterationData.append(dumboArray.copy())
        #print("dumbo",dumboArray)
        #print("iterationData",iterationData)

        iterationCount+=1
        setTrue()
        for y in range(len(dumboArray)):
            for x in range(len(dumboArray[y])):
                energyGain(y,x)

        if iterationCount == 100:
            print("Part1:",flashCount)
            return iterationData

        anyTrue = any(any(row) for row in checkIfNotFlashed)

        if not anyTrue:
            print("Part2:",iterationCount)
            break


with open('11.txt') as d:
    dataSplit = d.read().splitlines()
    for y in range(len(dataSplit)):
        dumboArray.append([])
        checkIfNotFlashed.append([])
        for x in range(len(dataSplit[y])):
            dumboArray[y].append(int(dataSplit[y][x]))
            checkIfNotFlashed[y].append(1)
    getData = simulate()

values = {0:"#272727", 1:"#434343", 2:"#646464", 3:"#7B7B7B", 4:"#989898", 5:"#BABABA", 6:"#D0D0D0", 7:"#E2E2E2", 8:"#F2F2F2", 9:"#FBFBFB"}
window = Tk()
window.title("Day11 - Visualized")
iterationNum = 0

def drawSimulation():
    global iterationData
    rando = random.randint(0,99)
    print(iterationNum)
    print(iterationData)

    print("Printing Array")
    for i in iterationData[0][rando]:
        print (i)


    for y in range(10):
        for x in range(10):
            UI_frame = Frame(window, width= 25, height=25, bg=values[iterationData[rando][y][x]])
            UI_frame.grid(row=y, column=x)


sceneUpdateButton = tk.Button(window, width=2, height=1, command=drawSimulation)
sceneUpdateButton.grid(row=100, column=50)

window.mainloop()
