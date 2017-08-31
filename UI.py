from tkinter import *
from LEDCube import LEDCube

import threading

cs = LEDCube([4,4,4])
pulseAllThread = threading.Thread(target=cs.pulseAll, args=[], kwargs={}, daemon=True)
pulseRowThread = threading.Thread(target=cs.pulseRows, args=[], kwargs={}, daemon=True)
pulseLayThread = threading.Thread(target=cs.pulseLayers, args=[], kwargs={}, daemon=True)

# root is the window for Test App

root = Tk()

# menuTitle = "Test App"
# subtitles are "Cycle:" and "Coordinate:"

menuTitle = Label(root, text="Test App")
menuTitle.grid(row=0)
subtitle1 = Label(root, text="Cycle:")
button1 = Button(root, text="LEDs", command=cs.pulseAll)
button2 = Button(root, text="Rows", command=cs.pulseRows)
button3 = Button(root, text="Layers", command=cs.pulseLayers)

subtitle1.grid(row=1, sticky=W)
button1.grid(row=1, column=1)
button2.grid(row=1, column=2)
button3.grid(row=1, column=3)

subtitle2 = Label(root, text="     Coordinate: (")
entryX = Entry(root)
comma1 = Label(root, text=",")
entryY = Entry(root)
comma2 = Label(root, text=",")
entryZ = Entry(root)
paren = Label(root, text=")   ")
button4 = Button(root, text="Toggle", command=lambda: cs.togglePixel([int(entryX.get()), int(entryY.get()), int(entryZ.get())]))
button5 = Button(root, text="Clear All", command=cs.clearAll)

subtitle2.grid(row=1, column=4)
entryX.grid(row=1, column=5)
comma1.grid(row=1, column=6)
entryY.grid(row=1, column=7)
comma2.grid(row=1, column=8)
entryZ.grid(row=1, column=9)
paren.grid(row=1, column=10)
button4.grid(row=1, column=11)
button5.grid(row=1, column=12)

def startPulseAll():
    pulseAllThread.start()

def startPulseRows():
    pulseRowThread.start()

def startPulseLayers():
    pulseLayThread.start()


#circle radius
r = 5

class layerDisplay:

    def __init__(self, root, row, column, r, name):
        self.root = root
        self.row = row
        self.column = column
        self.r = r
        self.name = name
        canvas = Canvas(root, width=18*r, height=18*r)
        canvas.grid(row=row, column=column)
        for i in range(0, 4):
            for j in range(0, 4):
                canvas.create_oval(2 * r + 4 * r * j, 2 * r + 4 * r * i, 4 * r + 4 * r * j, 4 * r + 4 * r * i)
        nameLabel = Label(root, text=name)
        nameLabel.grid(row=row, column=column + 1)

layerZ1 = layerDisplay(root, 3, 0, 5, "z1")
layerZ2 = layerDisplay(root, 4, 0, 5, "z2")
layerZ3 = layerDisplay(root, 5, 0, 5, "z3")
layerZ4 = layerDisplay(root, 6, 0, 5, "z4")

root.mainloop()
