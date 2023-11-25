from tkinter import *
from threading import Thread
from time import sleep

def start(n):
    btns_start[n].config(state='disabled')
    times_running[n] = True
    while times_running[n]:
        times[n]+=1
        sleep(0.001)
        s = times[n]//1000
        ms = times[n]%1000
        m = s//60
        s = s%60
        labels[n].config(text=f"{m:02}:{s:02}.{ms:03}")

def stop(n):
    times_running[n]=False
    btns_start[n].config(state='normal')

def run(n):
    Thread(target=start, args=(n,), daemon=True).start()

times = [0,0,0,0]
times_running = [False, False, False, False]

root = Tk()
btns_start = [
    Button(root, text='Start', command=lambda:run(0)),
    Button(root, text='Start', command=lambda:run(1)),
    Button(root, text='Start', command=lambda:run(2)),
    Button(root, text='Start', command=lambda:run(3)),
]
btns_stop = [
    Button(root, text='Stop', command=lambda:stop(0)),
    Button(root, text='Stop', command=lambda:stop(1)),
    Button(root, text='Stop', command=lambda:stop(2)),
    Button(root, text='Stop', command=lambda:stop(3)),
]
labels = [
    Label(root, text='00:00.00'),
    Label(root, text='00:00.00'),
    Label(root, text='00:00.00'),
    Label(root, text='00:00.00'),
]
for i in range(4):
    btns_start[i].grid(row=i, column=1)
    btns_stop[i].grid(row=i, column=2)
    labels[i].grid(row=i, column=3)

mainloop()
