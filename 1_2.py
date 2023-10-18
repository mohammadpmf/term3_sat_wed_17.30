from tkinter import *

root = Tk()
root.title('به رستوران من خوش آمدید')
root.geometry('900x700')
root.resizable(0, 0)
root.config(bg='#333333')
label_name = Label(root, text="Enter your name: ", bg="#333333", fg='yellow',
                        font=("", 28, 'italic'))
label_name.pack(pady=16)
entry_name = Entry(root)
entry_name.pack()
label_name2 = Label(root, text="Enter your name: ", bg="#333333", fg='yellow',
                        font=("", 28, 'italic'))
label_name2.pack(pady=16)
entry_name2 = Entry(root)
entry_name2.pack()
label_name3 = Label(root, text="Enter your name: ", bg="#333333", fg='yellow',
                        font=("", 28, 'italic'))
label_name3.pack(pady=16)
entry_name3 = Entry(root)
entry_name3.pack()
btn_save = Button(root, text="Save", bg="#333333", fg="yellow",
                activebackground='yellow', activeforeground='#333333')
btn_save.pack(pady=16)
mainloop()
