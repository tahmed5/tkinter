from tkinter import *
import random

window = Tk() #As soon as we create an object from the class a blank window is created

def DisplayText():
    print('Hello World')

def printNum(event):
    print(random.randint(0,1000))

#command = (function_name)
    
button1 = Button(window,text= 'Display Text', command = DisplayText)
button1.pack()

#waiting for event. Binding a key to a button
button2 = Button(window,text= 'Display Number')
button2.bind("<Button-1>", printNum)

button2.pack()


window.mainloop() #puts it into an infinite loop until window is closed
 
