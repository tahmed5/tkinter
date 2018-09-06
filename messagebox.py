from tkinter import *
import tkinter.messagebox

window = Tk()

tkinter.messagebox.showinfo('Window Title', 'It Takes 43 muscles to frown') #for basic message box with an OK button

answer = tkinter.messagebox.askquestion('Question', 'Does it take 17 muscles to smile?')

if answer == 'yes':
    print('Correct')
else:
    print('Incorrect')
    
window.mainloop()
