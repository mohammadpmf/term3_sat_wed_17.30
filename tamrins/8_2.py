from tkinter import *
from threading import Thread
from time import sleep

def start(n):
    global time1, time2, time3, time1_is_running, time2_is_running, time3_is_running
    if n==1:
        btn_start1.config(state='disabled')
        time1_is_running = True
        while time1_is_running:
            time1+=1
            sleep(0.001)
            s = time1//1000
            ms = time1%1000
            m = s//60
            s = s%60
            label1.config(text=f"{m:02}:{s:02}.{ms:03}")
    elif n==2:
        btn_start2.config(state='disabled')
        time2_is_running = True
        while time2_is_running:
            time2+=1
            sleep(0.001)
            s = time2//1000
            ms = time2%1000
            m = s//60
            s = s%60
            label2.config(text=f"{m:02}:{s:02}.{ms:03}")
    elif n==3:
        btn_start3.config(state='disabled')
        time3_is_running = True
        while time3_is_running:
            time3+=1
            sleep(0.001)
            s = time3//1000
            ms = time3%1000
            m = s//60
            s = s%60
            label3.config(text=f"{m:02}:{s:02}.{ms:03}")

def stop(n):
    global time1_is_running, time2_is_running, time3_is_running
    if n==1:
        time1_is_running=False
        btn_start1.config(state='normal')
    elif n==2:
        time2_is_running=False
        btn_start2.config(state='normal')
    elif n==3:
        time3_is_running=False
        btn_start3.config(state='normal')

def run(n):
    Thread(target=start, args=(n,), daemon=True).start()

time1=0
time2=0
time3=0
time1_is_running = False
time2_is_running = False
time3_is_running = False

root = Tk()
btn_start1 = Button(root, text='Start', command=lambda:run(1))
btn_start2 = Button(root, text='Start', command=lambda:run(2))
btn_start3 = Button(root, text='Start', command=lambda:run(3))
btn_stop1 = Button(root, text='Stop', command=lambda:stop(1))
btn_stop2 = Button(root, text='Stop', command=lambda:stop(2))
btn_stop3 = Button(root, text='Stop', command=lambda:stop(3))
label1 = Label(root, text='00:00.00')
label2 = Label(root, text='00:00.00')
label3 = Label(root, text='00:00.00')
btn_start1.grid(row=1, column=1)
btn_start2.grid(row=2, column=1)
btn_start3.grid(row=3, column=1)
btn_stop1.grid(row=1, column=2)
btn_stop2.grid(row=2, column=2)
btn_stop3.grid(row=3, column=2)
label1.grid(row=1, column=3)
label2.grid(row=2, column=3)
label3.grid(row=3, column=3)
mainloop()
