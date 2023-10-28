from tkinter import *
def start_exam():
    if b1.get():
        print("Exam is started.")
    else:
        print(":D")
    print(sv1.get())
def check():
    global prev_state
    temp = sv1.get()
    if temp == prev_state:
        sv1.set(' ')
    prev_state = sv1.get()
def show_result():
    pass

correct_answer = 0
wrong_answer = 0
nazadeh = 0
prev_state = ' '
root = Tk()
root.geometry('800x600')
b1 = BooleanVar(root)
cb1 = Checkbutton(root, text='start exam?', variable=b1, font=('Times', 20), command=start_exam)
l_q1 = Label(root, text="What is capital of germany?", font=('Times', 20))
sv1 = StringVar(root)
sv1.set(' ')
rb1 = Radiobutton(root, text='Moonikh', font=('Times', 20),    variable=sv1, value='Moonikh', command=check)
rb2 = Radiobutton(root, text='Berlin', font=('Times', 20),     variable=sv1, value='Berlin', command=check)
rb3 = Radiobutton(root, text='Amesterdam', font=('Times', 20), variable=sv1, value='Amesterdam', command=check)
rb4 = Radiobutton(root, text='Denhakh', font=('Times', 20),    variable=sv1, value='Denhakh', command=check)
cb1.grid(row=1, column=1)
l_q1.grid(row=2, column=1, columnspan=4)
rb1.grid(row=3, column=1)
rb2.grid(row=3, column=2)
rb3.grid(row=3, column=3)
rb4.grid(row=3, column=4)
l_q1 = Label(root, text="What is capital of germany?", font=('Times', 20))
sv1 = StringVar(root)
sv1.set(' ')
rb1 = Radiobutton(root, text='Moonikh', font=('Times', 20),    variable=sv1, value='Moonikh', command=check)
rb2 = Radiobutton(root, text='Berlin', font=('Times', 20),     variable=sv1, value='Berlin', command=check)
rb3 = Radiobutton(root, text='Amesterdam', font=('Times', 20), variable=sv1, value='Amesterdam', command=check)
rb4 = Radiobutton(root, text='Denhakh', font=('Times', 20),    variable=sv1, value='Denhakh', command=check)
cb1.grid(row=1, column=1)
l_q1.grid(row=4, column=1, columnspan=4)
rb1.grid(row=5, column=1)
rb2.grid(row=5, column=2)
rb3.grid(row=5, column=3)
rb4.grid(row=5, column=4)
l_q1 = Label(root, text="What is capital of germany?", font=('Times', 20))
sv1 = StringVar(root)
sv1.set(' ')
rb1 = Radiobutton(root, text='Moonikh', font=('Times', 20),    variable=sv1, value='Moonikh', command=check)
rb2 = Radiobutton(root, text='Berlin', font=('Times', 20),     variable=sv1, value='Berlin', command=check)
rb3 = Radiobutton(root, text='Amesterdam', font=('Times', 20), variable=sv1, value='Amesterdam', command=check)
rb4 = Radiobutton(root, text='Denhakh', font=('Times', 20),    variable=sv1, value='Denhakh', command=check)
cb1.grid(row=1, column=1)
l_q1.grid(row=6, column=1, columnspan=4)
rb1.grid(row=7, column=1)
rb2.grid(row=7, column=2)
rb3.grid(row=7, column=3)
rb4.grid(row=7, column=4)
btn = Button(root, text='send', command=show_result)
btn.grid(row=8, column=1, columnspan=4, sticky='ew')


mainloop()