from tkinter import *


window = Tk() #As soon as we create an object from the class a blank window is created

topFrame = Frame(window)
topFrame.pack()
bottomFrame = Frame(window)
bottomFrame.pack(side = BOTTOM) # pack it into a specified side as well

button1 = Button(topFrame, text = 'Button 1', fg='red') #frame, text, colour
button2 = Button(topFrame, text = 'Button 2', fg='blue') #frame, text, colour
button3 = Button(topFrame, text = 'Button 3', fg='green') #frame, text, colour
button4 = Button(bottomFrame, text = 'Button 4', fg='purple') #frame, text, colour

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)

window.mainloop() #puts it into an infinite loop until window is closed
 
