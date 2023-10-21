from tkinter import *
from PIL import Image, ImageTk

def order():
    print(s0.get())
    print(s1.get())
    print(s2.get())

root = Tk()
addresses = ['1.jpg', 'mar.jpeg', 'tom.png']
pic0 = Image.open(addresses[0])
pic1 = Image.open(addresses[1])
pic2 = Image.open(addresses[2])
pic0 = pic0.resize((100, 100))
pic0 = ImageTk.PhotoImage(pic0)
pic1 = pic1.resize((100, 100))
pic1 = ImageTk.PhotoImage(pic1)
pic2 = pic2.resize((100, 100))
pic2 = ImageTk.PhotoImage(pic2)
lbl0 = Label(root, image=pic0)
lbl1 = Label(root, image=pic1)
lbl2 = Label(root, image=pic2)
lbl0.grid(row=1, column=1)
lbl1.grid(row=2, column=1)
lbl2.grid(row=3, column=1)
s0 = Spinbox(root, width=5, from_=0, to=10, wrap=True, state='readonly')
s1 = Spinbox(root, width=5, from_=0, to=10, state='readonly')
s2 = Spinbox(root, width=5, from_=0, to=10, state='readonly')
s0.grid(row=1, column=2)
s1.grid(row=2, column=2)
s2.grid(row=3, column=2)
btn = Button(root, text='order', command=order)
btn.grid(row=4, column=1, columnspan=2)

mainloop()