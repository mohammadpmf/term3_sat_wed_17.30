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
btn0 = Button(root, text=0, cnf=sadra)
btn1 = Button(root, text=1, cnf=sadra)
btn2 = Button(root, text=2, cnf=sadra)
btn3 = Button(root, text=3, cnf=sadra)
btn4 = Button(root, text=4, cnf=sadra)
btn5 = Button(root, text=5, cnf=sadra)
btn6 = Button(root, text=6, cnf=sadra)
btn7 = Button(root, text=7, cnf=sadra)
btn8 = Button(root, text=8, cnf=sadra)
btn9 = Button(root, text=9, cnf=sadra)
btnp = Button(root, text='+', cnf=sadra)
btnm = Button(root, text='-', cnf=sadra)
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
