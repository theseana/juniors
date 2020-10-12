from threading import Thread
from time import sleep


def time(t):
    for i in range(t):
        print(i)
        sleep(1)

thread1 = Thread(target = time, args = (10, ))
thread1.start()
thread2 = Thread(target = time, args = (10, ))
thread2.start()
