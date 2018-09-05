from tkinter import *


window = Tk() #As soon as we create an object from the class a blank window is created

username = Label(window, text = 'Username:')
password = Label(window, text = 'Password:')
entry_un = Entry(window) #Entry displays an input box
entry_pw = Entry(window)
#.grid() allows you to specify the row and column to display the widget
#sticky allows you to align N E S W
username.grid(row = 0, column = 0, sticky = E) 
password.grid(row = 1, column = 0, sticky = E)
entry_un.grid(row = 0, column = 1)
entry_pw.grid(row = 1, column = 1)

#Checkbutton() dispalys a tick box

checkbox = Checkbutton(window, text = 'Keep Me Logged In')
#You can set a columnspan to take up more than one cell
checkbox.grid(columnspan = 2)

window.mainloop() #puts it into an infinite loop until window is closed
 
