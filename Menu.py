from tkinter import *
import random

def newFile():
    print('New File Generated')

window = Tk() #As soon as we create an object from the class a blank window is created

#drop down menu function - Menu()
menu = Menu(window)
window.config(menu= menu) #configure the menu. tkinter defaulty packs it.

subMenu = Menu(menu)  #Menu item within a menu
menu.add_cascade(label = 'File', menu = subMenu)#Cascade is a drop down menu
subMenu.add_command(label = 'New File', command = newFile)
subMenu.add_command(label = 'Open...')
subMenu.add_command(label = 'Open Module..')
subMenu.add_separator()
subMenu.add_command(label = 'Save')
subMenu.add_separator()
subMenu.add_command(label = 'Exit')

editMenu = Menu(menu)
menu.add_cascade(label = 'Edit', menu = editMenu)
editMenu.add_command(label = 'Undo')
editMenu.add_command(label = 'Redo')

window.mainloop() #puts it into an infinite loop until window is closed
 
