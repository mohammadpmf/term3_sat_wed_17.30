from tkinter import *
def show_result():
    global correct_answer, wrong_answer, nazadeh
    correct_answer = 0
    wrong_answer = 0
    nazadeh = 0
    if sv1.get() == 'Berlin':
        correct_answer += 1
    elif sv1.get() in ['Moonikh', 'Amesterdam', 'Denhakh']:
        wrong_answer += 1
    else:
        nazadeh += 1
    if sv2.get() == "2":
        correct_answer+=1
    elif sv2.get() in ['4', '6', '10']:
        wrong_answer +=1
    else:
        nazadeh+=1
    if sv3.get() == "4":
        correct_answer+=1
    elif sv3.get() in ['12', '6', '5']:
        wrong_answer +=1
    else:
        nazadeh+=1
    btn.config(text=f'Correct: {correct_answer}\nWrong: {wrong_answer}\nNazadeh: {nazadeh}')

correct_answer = 0
wrong_answer = 0
nazadeh = 0
root = Tk()
root.geometry('800x600')
l_q1 = Label(root, text="What is capital of germany?", font=('Times', 20))
l_q2 = Label(root, text="1+1?", font=('Times', 20))
l_q3 = Label(root, text="2*2?", font=('Times', 20))
sv1 = StringVar(root)
sv2 = StringVar(root)
sv3 = StringVar(root)
sv1.set(' ')
sv2.set(' ')
sv3.set(' ')
rb1_1 = Radiobutton(root, text='Moonikh', font=('Times', 20),    variable=sv1, value='Moonikh')
rb1_2 = Radiobutton(root, text='Berlin', font=('Times', 20),     variable=sv1, value='Berlin')
rb1_3 = Radiobutton(root, text='Amesterdam', font=('Times', 20), variable=sv1, value='Amesterdam')
rb1_4 = Radiobutton(root, text='Denhakh', font=('Times', 20),    variable=sv1, value='Denhakh')
rb2_1 = Radiobutton(root, text='2', font=('Times', 20),    variable=sv2, value='2')
rb2_2 = Radiobutton(root, text='6', font=('Times', 20),     variable=sv2, value='6')
rb2_3 = Radiobutton(root, text='4', font=('Times', 20), variable=sv2, value='4')
rb2_4 = Radiobutton(root, text='10', font=('Times', 20),    variable=sv2, value='10')
rb3_1 = Radiobutton(root, text='5', font=('Times', 20),    variable=sv3, value='5')
rb3_2 = Radiobutton(root, text='6', font=('Times', 20),     variable=sv3, value='6')
rb3_3 = Radiobutton(root, text='4', font=('Times', 20), variable=sv3, value='4')
rb3_4 = Radiobutton(root, text='12', font=('Times', 20),    variable=sv3, value='12')
l_q1.grid(row=2, column=1, columnspan=4)
rb1_1.grid(row=3, column=1)
rb1_2.grid(row=3, column=2)
rb1_3.grid(row=3, column=3)
rb1_4.grid(row=3, column=4)
l_q2.grid(row=4, column=1, columnspan=4)
rb2_1.grid(row=5, column=1)
rb2_2.grid(row=5, column=2)
rb2_3.grid(row=5, column=3)
rb2_4.grid(row=5, column=4)
l_q3.grid(row=6, column=1, columnspan=4)
rb3_1.grid(row=7, column=1)
rb3_2.grid(row=7, column=2)
rb3_3.grid(row=7, column=3)
rb3_4.grid(row=7, column=4)
btn = Button(root, text='send', command=show_result)
btn.grid(row=8, column=1, columnspan=4, sticky='ew')
mainloop()