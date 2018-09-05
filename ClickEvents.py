from tkinter import *

window = Tk() #As soon as we create an object from the class a blank window is created

def leftClick(event):
    print(type(event))
    print('Left')

def midClick(event):
    print('Middle')
    
def rightClick(event):
    print('Right')

frame = Frame(window, width = 300, height = 250)
frame.bind('<Button-1>', leftClick) #'<Button-1>' left click
frame.bind('<Button-2>', midClick) #'<Button-2>' middle click
frame.bind('<Button-3>', rightClick) #'<Button-3>' right click
frame.pack()


window.mainloop() #puts it into an infinite loop until window is closed
 
