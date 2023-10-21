from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
# pip install pillow
# py -m pip install pillow
# p = PhotoImage(file='tamrins/mar.jpeg')
root = Tk()
# address = filedialog.askopenfilename()
# p1 = Image.open(address)
p1 = Image.open('tamrins/tom.png')
p1 = p1.resize((160,160))
p = ImageTk.PhotoImage(p1)
label_pic = Label(root, image=p)
label_pic.grid(row=1, column=1)
s1 = Spinbox(root, from_=0, to=10, width=5, state='readonly', justify='center', wrap=True)
s1.grid(row=1, column=2)
b1 = Button(root, text='ok')
# label_pic.place(x=600, y=0, width=60, height=60)
mainloop()
