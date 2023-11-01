from tkinter import *
root = Tk()
root.geometry('600x600')
def start(n):
    h = int(spin_h1.get())
    m = int(spin_m1.get())
    lbl_1.config(text=f"Amoxicilin {h:02}:{m:02}")
# Labelframes
frame1 = LabelFrame(root, text='Amoxicilin', labelanchor='n')
frame1.grid(row=1, column=1)
# End Labelframes
# Frame1
lbl_1 = Label(frame1, text="00:00", font=('', 20))
btn1 = Button(frame1, text='Start', font=('', 20), command=lambda:start(1))
btn2 = Button(frame1, text='Reset', font=('', 20))
spin_h1 = Spinbox(frame1, from_=0, to=23, width=3, justify='center', wrap=True, state='readonly',
font=('', 20))
spin_m1 = Spinbox(frame1, from_=0, to=59, width=3, justify='center', wrap=True, state='readonly',
font=('', 20))
lbl_1.grid(row=0, column=1, columnspan=2)
spin_h1.grid(row=1, column=1)
spin_m1.grid(row=1, column=2)
btn1.grid(row=2, column=1)
btn2.grid(row=2, column=2)
# End Frame1
mainloop()
