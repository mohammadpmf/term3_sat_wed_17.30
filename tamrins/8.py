from turtle import *
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
for i in range(100):
    t1.fd(4)
for i in range(100):
    t2.fd(4)

done()