from tkinter import *
from json import load, dump
def enter():
    if e_pin.get()=='1234':
        manage_window.deiconify()
        root.withdraw()

config_btn = {
    'bg': 'pink',
    'fg': 'purple',
    'padx': 20,
    'pady': 15,
    'font': ('Times', 20),
}
config_entry = {
    'bg': 'pink',
    'fg': 'purple',
    'font': ('Times', 20),
}
root = Tk()
root.config(bg='pink')
e_card = Entry(root, cnf=config_entry)
e_pin = Entry(root, cnf=config_entry)
btn_enter = Button(root, text='Enter', cnf=config_btn, command=enter)
manage_window = Toplevel(root)
manage_window.protocol('WM_DELETE_WINDOW', root.destroy)
manage_window.withdraw()
e_card.pack(padx=15, pady=10)
e_pin.pack(padx=15, pady=10)
btn_enter.pack(padx=15, pady=10)
mainloop()