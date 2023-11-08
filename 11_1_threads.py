from tkinter import *
from threading import Thread
from time import sleep
from gtts import gTTS
import pygame
pygame.mixer.init()
player = pygame.mixer
tts=gTTS(text="Time to eat Amoxicilin",lang="en")
tts.save("drug1.mp3")
tts2=gTTS(text="Time to eat Acetaminophen",lang="en")
tts2.save("drug2.mp3")

def real_start(n):
    global h, m, h2, m2
    if n==1:
        h = int(spin_h1.get())
        m = int(spin_m1.get())
        lbl_1.config(text=f"Amoxicilin {h:02}:{m:02}")
        btn1.config(state='disable')
        while (h, m) != (0, 0):
            sleep(1)
            m -= 1
            if m==-1:
                h-=1
                m+=60
                if h==-1:
                    h=0
                    m=0
            lbl_1.config(text=f"Amoxicilin {h:02}:{m:02}")
            lbl_1.update()
        btn1.config(state='normal')
        player.music.load('drug1.mp3')
        player.music.play()
    elif n==2:
        h2 = int(spin_h2.get())
        m2 = int(spin_m2.get())
        lbl_2.config(text=f"Acetaminophen {h2:02}:{m2:02}")
        btn11.config(state='disable')
        while (h2, m2) != (0, 0):
            sleep(1)
            m2 -= 1
            if m2==-1:
                h2-=1
                m2+=60
                if h2==-1:
                    h2=0
                    m2=0
            lbl_2.config(text=f"Acetaminophen {h2:02}:{m2:02}")
            lbl_2.update()
        btn11.config(state='normal')
        player.music.load('drug2.mp3')
        player.music.play()

def start(n):
    t = Thread(target=real_start, args=(n, ), daemon=True)
    t.start()


def reset(n):
    global h, m, h2, m2
    if n==1:
        h=0
        m=0
        btn1.config(state='normal')
        lbl_1.config(text=f"00:00")
        spin_h1.config(state='normal')
        spin_h1.delete(0, END)
        spin_h1.insert(0, '0')
        spin_h1.config(state='readonly')
        spin_m1.config(state='normal')
        spin_m1.delete(0, END)
        spin_m1.insert(0, '0')
        spin_m1.config(state='readonly')
    elif n==2:
        h2=0
        m2=0
        btn11.config(state='normal')
        lbl_2.config(text=f"00:00")
        spin_h2.config(state='normal')
        spin_h2.delete(0, END)
        spin_h2.insert(0, '0')
        spin_h2.config(state='readonly')
        spin_m2.config(state='normal')
        spin_m2.delete(0, END)
        spin_m2.insert(0, '0')
        spin_m2.config(state='readonly')

root = Tk()
root.geometry('600x600')

h=0
m=0
# Labelframes
frame1 = LabelFrame(root, text='Amoxicilin', labelanchor='n')
frame2 = LabelFrame(root, text='Acetaminophen', labelanchor='n')
frame1.grid(row=1, column=1)
frame2.grid(row=1, column=2)
# End Labelframes
# Frame1
lbl_1 = Label(frame1, text="00:00", font=('', 20))
lbl_2 = Label(frame2, text="00:00", font=('', 20))
btn1 = Button(frame1, text='Start', font=('', 20), command=lambda:start(1))
btn2 = Button(frame1, text='Reset', font=('', 20), command=lambda:reset(1))
btn11 = Button(frame2, text='Start', font=('', 20), command=lambda:start(2))
btn12 = Button(frame2, text='Reset', font=('', 20), command=lambda:reset(2))
spin_h1 = Spinbox(frame1, from_=0, to=23, width=3, justify='center', wrap=True, state='readonly',
font=('', 20))
spin_h2 = Spinbox(frame2, from_=0, to=23, width=3, justify='center', wrap=True, state='readonly',
font=('', 20))
spin_m1 = Spinbox(frame1, from_=0, to=59, width=3, justify='center', wrap=True, state='readonly',
font=('', 20))
spin_m2 = Spinbox(frame2, from_=0, to=59, width=3, justify='center', wrap=True, state='readonly',
font=('', 20))
lbl_1.grid(row=0, column=1, columnspan=2)
lbl_2.grid(row=0, column=1, columnspan=2)
spin_h1.grid(row=1, column=1)
spin_h2.grid(row=1, column=1)
spin_m1.grid(row=1, column=2)
spin_m2.grid(row=1, column=2)
btn1.grid(row=2, column=1)
btn11.grid(row=2, column=1)
btn2.grid(row=2, column=2)
btn12.grid(row=2, column=2)

# End Frame1
mainloop()
