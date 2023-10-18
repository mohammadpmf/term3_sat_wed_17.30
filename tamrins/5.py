from tkinter import *
import pygame

pygame.mixer.init()
player = pygame.mixer

def play():
    try:
        player.music.load('address')
        player.music.play()
    except:
        pass

def insert(n):
    entry.insert(END, n)

def clear1():
    tool = len(entry.get())
    entry.delete(tool-1, END)

def equal():
    try:
        res = eval(entry.get())
        clear()
        entry.insert(0, res)
    except:
        clear()
        entry.insert(0, 'Error')

def clear():
    entry.delete(0, END)

cnf_btns = {
    'bg': '#333333',
    'fg': 'orange',
    'font': ('', 28),
    'bd': 8
}

root = Tk()
root.config(bg="#333333")
root.geometry('900x500')
btn000   = Button(root, text='000', cnf=cnf_btns, command=lambda:insert('000'))
btn00    = Button(root, text='00' , cnf=cnf_btns, command=lambda:insert('00'))
btn0     = Button(root, text='0'  , cnf=cnf_btns, command=lambda:insert('0'))
btn1     = Button(root, text='1'  , cnf=cnf_btns, command=lambda:insert('1'))
btn2     = Button(root, text='2'  , cnf=cnf_btns, command=lambda:insert('2'))
btn3     = Button(root, text='3'  , cnf=cnf_btns, command=lambda:insert('3'))
btn4     = Button(root, text='4'  , cnf=cnf_btns, command=lambda:insert('4'))
btn5     = Button(root, text='5'  , cnf=cnf_btns, command=lambda:insert('5'))
btn6     = Button(root, text='6'  , cnf=cnf_btns, command=lambda:insert('6'))
btn7     = Button(root, text='7'  , cnf=cnf_btns, command=lambda:insert('7'))
btn8     = Button(root, text='8'  , cnf=cnf_btns, command=lambda:insert('8'))
btn9     = Button(root, text='9'  , cnf=cnf_btns, command=lambda:insert('9'))
btnplus  = Button(root, text='+'  , cnf=cnf_btns, command=lambda:insert('+'))
btnminus = Button(root, text='-'  , cnf=cnf_btns, command=lambda:insert('-'))
btnmul   = Button(root, text='*'  , cnf=cnf_btns, command=lambda:insert('*'))
btndiv   = Button(root, text='/'  , cnf=cnf_btns, command=lambda:insert('/'))
btndot   = Button(root, text='.'  , cnf=cnf_btns, command=lambda:insert('.'))
btnclear = Button(root, text='AC' , cnf=cnf_btns, command=clear)
btnclear1= Button(root, text='←'  , cnf=cnf_btns, command=clear1)
btncequal= Button(root, text='='  , cnf=cnf_btns, command=equal)
entry    = Entry(root, insertbackground='orange', cnf=cnf_btns)
btn000.grid(row=5, column=4, columnspan=3, sticky='news')
btn00.grid(row=5, column=2, columnspan=2, sticky='news')
btn0.grid(row=5, column=1, sticky='news')
btn1.grid(row=4, column=1, sticky='news')
btn2.grid(row=4, column=2, sticky='news')
btn3.grid(row=4, column=3, sticky='news')
btn4.grid(row=3, column=1, sticky='news')
btn5.grid(row=3, column=2, sticky='news')
btn6.grid(row=3, column=3, sticky='news')
btn7.grid(row=2, column=1, sticky='news')
btn8.grid(row=2, column=2, sticky='news')
btn9.grid(row=2, column=3, sticky='news')
btnplus.grid(row=2, column=4, rowspan=2, sticky='news')
btnminus.grid(row=4, column=4, sticky='news')
btnmul.grid(row=2, column=5, sticky='news')
btndiv.grid(row=3, column=5, sticky='news')
btndot.grid(row=4, column=5, sticky='news')
btnclear.grid(row=2, column=6, sticky='news')
btnclear1.grid(row=3, column=6, sticky='news')
btncequal.grid(row=4, column=6, sticky='news')
entry.grid(row=1, column=1, columnspan=6, sticky='news')
btnclose = Button(root, text='Play', cnf=cnf_btns, command=play)
btnclose.place(x=500, y=400, width=200, height=80)

mainloop()