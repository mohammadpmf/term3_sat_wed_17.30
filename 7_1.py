from tkinter import *
from tkinter import ttk
root = Tk()
months = ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Sharivar',
'Mehr', 'Aban', 'Azar', 'Dey', 'Bahman', 'Esfand']
days = []
for i in range(1, 32):
    days.append(i)
label_month = Label(root, text='Month: ')
label_day   = Label(root, text='Day: ')
combo_month = ttk.Combobox(root, values=months)
combo_day   = ttk.Combobox(root, values=days)
label_month .grid(row=1, column=1)
combo_month .grid(row=1, column=2)
label_day   .grid(row=1, column=3)
combo_day   .grid(row=1, column=4)

mainloop()