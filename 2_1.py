from tkinter import *

def say_hello():
    global a
    a = a+1
    btn_test.config(text=a)
    name = entry_name.get()
    lable_name.config(text=f"barbari {a}")

a = 1
root = Tk()
root.title("Mohammad Pourmohammadi Fallah :D")
root.geometry("900x600")
root.resizable(0, 0)
root.config(bg='#ed40d6')
lable_name = Label(root, bg='#ed40d6', fg='red', text="Enter Your name here:",
font=('',20))
lable_name.pack()
entry_name = Entry(root, font=('', 20), fg='green')
entry_name.pack(pady=50)
btn_test = Button(root, command=say_hello, text='Click here to start the game',
font=('', 20), bg='black', fg='white', activebackground='white',
activeforeground='black')
btn_test.pack()
mainloop()
