from turtle import *
from threading import Thread
def go_ahed(t:Pen):
    for i in range(100):
        t.fd(4)

t1 = Pen()
t2 = Pen()
t1.shape('turtle')
t2.shape('turtle')
t1.up()
t2.up()
t1.goto(-200, -200)
t2.goto(-200, 200)
t1.down()
t2.down()
Thread(target=go_ahed, args=(t1,)).start()
Thread(target=go_ahed, args=(t2,)).start()

done()