from tkinter import *
from tkinter import ttk
import random




window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg = "WHITE")

### User interface here ###
UI_frame = Frame(window, width= 900, height=300, bg="WHITE")
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select sorting algorithm
l1 = Label(UI_frame, text="Algorithm: ", bg="WHITE")
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)


# dropdown to select sorting speed
l2 = Label(UI_frame, text="Sorting Speed: ", bg="WHITE")
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)

# canvas to draw our array
canvas = Canvas(window, width=800, height=400, bg="WHITE")
canvas.grid(row=1, column=0, padx=10, pady=5)




with open('3.txt') as d:
    data = d.read().splitlines()


def findRating(arrayInput, ifGenerator):
    arrayDraw = []
    for d in arrayInput:
        sumT = 0
        for g in d:
            sumT += int(g)
        arrayDraw.append(sumT)
    drawData(arrayDraw)

    for y in range(len(arrayInput[0])):
        if len(arrayInput) == 1:
            return int(arrayInput[0], 2)
        totalSum, mostCommon = 0, 0
        tempArray = []

        for x in range(len(arrayInput)):
            totalSum += int(arrayInput[x][y])
            if totalSum < len(arrayInput) / 2:
                mostCommon = 0 if ifGenerator else 1
            else:
                mostCommon = 1 if ifGenerator else 0

        for x in range(len(arrayInput)):
            if int(arrayInput[x][y]) == int(mostCommon):
                tempArray.append(arrayInput[x])
        arrayInput = tempArray
    window.update_idletasks()
    return int(arrayInput[0], 2)

def drawData(data):
    print("Drawing")
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1)
    window.update_idletasks()

generatorBinary = findRating(data, True)
scrubberBinary = findRating(data, False)
print(generatorBinary * scrubberBinary)

window.mainloop()