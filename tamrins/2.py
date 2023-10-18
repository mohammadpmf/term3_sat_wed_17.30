from tkinter import *
def check():
    global temp
    if temp>30:
        lbl_temp.config(bg='red')
    elif temp<15:
        lbl_temp.config(bg='blue')
    else:
        lbl_temp.config(bg='green')
def up():
    global temp
    temp += 1
    lbl_temp.config(text=temp)
    check()
def down():
    global temp
    temp -= 1
    lbl_temp.config(text=temp)
    check()
temp = 25
root = Tk()
btn1 = Button(root, text='UP', command=up)
lbl_temp = Label(root, text=25, bg='green')
btn2 = Button(root, text='Down', command=down)
btn1.pack()
lbl_temp.pack()
btn2.pack()

mainloop()