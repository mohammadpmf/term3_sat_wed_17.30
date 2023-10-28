from tkinter import *
def close():
    root.destroy()
def login(event=None):
    if e_password.get()=='123':
        root2.deiconify()
        root.withdraw()
    else:
        print('wrong pass')
def test(event):
    global score
    if event.keysym == 'Up':
        score +=1
    elif event.keysym == 'Down':
        score-=1
    print(score)
score = 0
root = Tk()
root2 = Toplevel(root)
root2.protocol("WM_DELETE_WINDOW", close)
root2.geometry('400x200')
root2.withdraw()
root.geometry('800x600')
e_password = Entry(root, show='*')
btn = Button(root, text='Login', command=login)
e_password.pack()
btn.pack()
label = Label(root2)
label.grid(row=1, column=1)
e_password.bind('<Return>', login)
e_password.bind('<Key>', test)
mainloop()