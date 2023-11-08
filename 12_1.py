from threading import Thread
from time import sleep

def count(n):
    for i in range(n, -1, -1):
        sleep(1)
        print(i)

kargar1 = Thread(target=count, args=(10,))
kargar2 = Thread(target=count, args=(10,))
kargar3 = Thread(target=count, args=(10,))
#amogus
kargar1.start()
kargar2.start()
kargar3.start()
# count(10) # 10 seconds
# count(10) # 10  seconds
# count(10) # 10 seconds
print("End")
