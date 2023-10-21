from tkinter import *
def up1(n):
    global b
    b += n
    if b>10 or b<0:
        b -= n
        return
    lbl_b.config(text=f"Barbari {b}")
def up2(n):
    global l
    l += n
    if l>50 or l<0:
        l -= n
        return
    lbl_l.config(text=f"Lavash {l}")
b = 0
l = 0
root = Tk()
root.geometry("300x300+600+300")
btn_b1 = Button(root, text='add barbari', relief='groove', border=2, command=lambda:up1(1))
btn_b2 = Button(root, text='sub barbari', command=lambda:up1(-1))
btn_l1 = Button(root, text='add lavash', command=lambda:up2(5))
btn_l2 = Button(root, text='sub lavash', bg='red', command=lambda:up2(-5))
lbl_b = Label(root, text='Barbari 0')
lbl_l = Label(root, text='Lavash 0')
btn_b1.grid(row=0, column=0)
lbl_b.grid(row=1, column=0)
btn_b2.grid(row=2, column=0)
btn_l1.grid(row=0, column=1)
lbl_l.grid(row=1, column=1)
btn_l2.grid(row=2, column=1)
mainloop()