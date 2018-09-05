from tkinter import *

#bg = background
#fg = foreground
window = Tk() #As soon as we create an object from the class a blank window is created

one = Label(window, text = 'One', bg = 'red', fg='white')
one.pack()
two = Label(window, text = 'Two', bg = 'blue', fg='white')
two.pack(fill= X) #If the window is enlarged the size of the label will dynamically grow in the x axis
three = Label(window, text = 'Three', bg = 'green', fg='white')
three.pack(side = LEFT, fill = Y) #fill = Y, dynamically grow in the Y axis

window.mainloop() #puts it into an infinite loop until window is closed
 
