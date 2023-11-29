from tkinter import *
from tkinter.ttk import Combobox
from json import load, dump
from tkinter import messagebox, filedialog

money = [10, 25, 40, 80, 120, 160, 200]

def change_window(show_window:Toplevel, hide_window:Toplevel):
    show_window.deiconify()
    hide_window.withdraw()

def get_info(card_number:str):
    if card_number.endswith('.json'):
        f = open(card_number, 'r')
        data = load(f)
        return data
    else:
        messagebox.showerror("Error", f"Card {card_number} is not a real bank card.")

def enter():
    global data
    data = get_info(filedialog.askopenfilename())
    if data==None:
        return
    elif e_pin.get()==data['pin']:
        manage_window.deiconify()
        root.withdraw()
    else:
        messagebox.showwarning("Warning", 
         f"Wrong pin for card {data['card number']}")

def save(file_name, data):
    f = open(file_name, 'w')
    dump(data, f, indent=4)
    f.close()

def balance():
    global data
    balance = data['balance']
    if balance-0.5<0:
        messagebox.showerror("Error", "Not enough money.")
        return
    balance -= 0.5
    data['balance']=balance
    messagebox.showinfo("Balance", f"Your new balance is {balance}")
    save('bank/'+data["card number"][0:4]+".json", data)

def withdraw():
    global data
    balance = data['balance']
    amount = combo_withdraw.get()
    try:
        amount = int(amount)
    except ValueError:
        messagebox.showwarning("Warning", "Select some value")
        return
    if balance-amount<0:
        messagebox.showerror("Error", "Don't money.")
        return
    balance-=amount
    data['balance'] = balance
    messagebox.showinfo("Success", f"Get your {amount}$")
    save('bank/'+data["card number"][0:4]+".json", data)

config_btn = {
    'bg': 'pink',
    'fg': 'purple',
    'padx': 20,
    'pady': 15,
    'font': ('Times', 20),
    'width': 16
}
config_entry = {
    'bg': 'pink',
    'fg': 'purple',
    'font': ('Times', 20),
}
root = Tk()
root.config(bg='pink')
e_pin = Entry(root, cnf=config_entry)
btn_enter = Button(root, text='Enter', cnf=config_btn, command=enter)
manage_window = Toplevel(root)
change_pin_window = Toplevel(manage_window)
transfer_window = Toplevel(manage_window)
withdraw_window = Toplevel(manage_window)
manage_window.protocol('WM_DELETE_WINDOW', root.destroy)
change_pin_window.protocol('WM_DELETE_WINDOW', root.destroy)
transfer_window.protocol('WM_DELETE_WINDOW', root.destroy)
withdraw_window.protocol('WM_DELETE_WINDOW', root.destroy)
manage_window.config(bg='pink')
change_pin_window.config(bg='pink')
transfer_window.config(bg='pink')
withdraw_window.config(bg='pink')
combo_withdraw = Combobox(withdraw_window, values=money, state='readonly')
combo_withdraw.grid(row=1, column=1)
btn_withdraw_withdraw_window = Button(withdraw_window, cnf=config_btn, text='Withdraw',
    command=withdraw)
btn_withdraw_withdraw_window.grid(row=2, column=1)
btn_back_withdraw_window = Button(withdraw_window, cnf=config_btn, text='Back',
    command=lambda:change_window(manage_window, withdraw_window))
btn_back_withdraw_window.grid(row=3, column=1)
manage_window.withdraw()
change_pin_window.withdraw()
transfer_window.withdraw()
withdraw_window.withdraw()
btn_withdraw   = Button(manage_window, text='Withdraw', cnf=config_btn,
command=lambda:change_window(withdraw_window, manage_window))
btn_transfer   = Button(manage_window, text='Transfer', cnf=config_btn)
btn_balance    = Button(manage_window, text='Balance', cnf=config_btn,
                                command=balance)
btn_change_pin = Button(manage_window, text='Change Pin', cnf=config_btn)
btn_withdraw.grid  (row=1, column=2, sticky='news', padx=20, pady=10)
btn_transfer.grid  (row=1, column=1, sticky='news', padx=20, pady=10)
btn_balance.grid   (row=2, column=1, sticky='news', padx=20, pady=10)
btn_change_pin.grid(row=2, column=2, sticky='news', padx=20, pady=10)


e_pin.pack(padx=15, pady=10)
btn_enter.pack(padx=15, pady=10)
mainloop()