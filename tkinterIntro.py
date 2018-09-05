from tkinter import *


window = Tk() #As soon as we create an object from the class a blank window is created
label = Label(window, text = 'Hello World') #Text = Label (window, text)
label.pack() #Pack it into the window
window.mainloop() #puts it into an infinite loop until window is closed
 
