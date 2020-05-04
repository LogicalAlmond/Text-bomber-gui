from tkinter import *
import pyautogui
from time import sleep

root = Tk()

# Functions
def clearEntry():
    msgEntry.delete(0, END)
    numEntry.delete(0, END)

def startBomb():
    message = msgEntry.get()
    maxnum = numEntry.get()
    maxsend = int(maxnum)
    pyautogui.FAILSAFE = True
    sleep(1)
    pyautogui.keyDown('command')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('command')
    pyautogui.keyUp('tab')
    sleep(2)
    sent = 0
    pyautogui.PAUSE = 0.05
    while sent < maxsend:
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        sent += 1

# Title and Description label
titleLabel = Label(root, text='Text Bomber GUI')
desLabel = Label(root, text='Open the iMessage thread youd like to bomb first.')
titleLabel.pack(side=TOP)
desLabel.pack(side=TOP)

# Frames
msgFrame = Frame(root)
numFrame = Frame(root)
msgFrame.pack(side=TOP)
numFrame.pack(side=TOP)

# Labels
msgLabel = Label(msgFrame, text='Message:')
numLabel = Label(numFrame, text='Number:')
msgLabel.pack(side=LEFT)
numLabel.pack(side=LEFT)

# Entry boxes
msgEntry = Entry(msgFrame)
numEntry = Entry(numFrame)
msgEntry.pack()
numEntry.pack()

# Buttons
startButton = Button(root, text='Start', command=startBomb)
clearButton = Button(root, text='Clear', command=clearEntry)
startButton.pack(side=BOTTOM, fill=BOTH)
clearButton.pack(side=BOTTOM, fill=BOTH)







root.mainloop()