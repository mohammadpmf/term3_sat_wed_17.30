from tkinter import *

def reset():
    spin1.delete(0, END)
    spin1.insert(5, '0')

root = Tk()
spin1 = Spinbox(root, from_=0, to=99)
spin1.pack()
btn = Button(root, command=reset)
btn.pack()
mainloop()