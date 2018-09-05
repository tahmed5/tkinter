from tkinter import *


class Buttons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(master, text = 'Print Hello World', command = self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(master, text = 'Quit Button', command = frame.quit)
        self.quitButton.pack(side = LEFT)

    def printMessage(self):
        print('Hello World')
        
window = Tk() #As soon as we create an object from the class a blank window is created
b = Buttons(window)
window.mainloop() #puts it into an infinite loop until window is closed
 
