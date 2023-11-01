from tkinter import *

sadra = {
    'bg': 'pink',
    'fg': 'cyan',
    'font': ('', 48),
    'activebackground': 'white',
    'activeforeground': 'pink',
    'relief': 'raised',
    'bd': 16,
    'padx': 12,
    'pady': 12,
}
sadra2={
    'padx': 8,
    'pady': 8,
}

root = Tk()
frame = Frame(root)
frame.grid(padx=400)
btn0 = Button(frame, text=0, cnf=sadra)
btn1 = Button(frame, text=1, cnf=sadra)
btn2 = Button(frame, text=2, cnf=sadra)
btn3 = Button(frame, text=3, cnf=sadra)
btn4 = Button(frame, text=4, cnf=sadra)
btn5 = Button(frame, text=5, cnf=sadra)
btn6 = Button(frame, text=6, cnf=sadra)
btn7 = Button(frame, text=7, cnf=sadra)
btn8 = Button(frame, text=8, cnf=sadra)
btn9 = Button(frame, text=9, cnf=sadra)
btnp = Button(frame, text='+', cnf=sadra)
btnm = Button(frame, text='-', cnf=sadra)
btn0.grid(row=4, column=1, columnspan=2, sticky='ew', cnf=sadra2)
btn1.grid(row=3, column=2, cnf=sadra2)
btn2.grid(row=2, column=2, cnf=sadra2)
btn3.grid(row=1, column=3, cnf=sadra2)
btn4.grid(row=1, column=2, cnf=sadra2)
btn5.grid(row=2, column=1, cnf=sadra2)
btn6.grid(row=3, column=1, cnf=sadra2)
btn7.grid(row=2, column=3, cnf=sadra2)
btn8.grid(row=1, column=1, cnf=sadra2)
btn9.grid(row=3, rowspan=2, column=3, sticky='news', columnspan=2, cnf=sadra2)
btnp.grid(row=1, column=4, rowspan=2, cnf=sadra2, sticky='news')
btnm.grid(row=3, column=5, rowspan=2, cnf=sadra2, sticky='news')

mainloop()
