import multiprocessing
from random import randint
import time
from multiprocessing import Queue


q = Queue()


# producer
def Ping(q: Queue):
    while True:
        i = randint(1,10)
        q.put(i)
        print(f"{i} inserted to memory")
        time.sleep(i)


# consumer
def Pong(q: Queue):
    while True:
        i = q.get()
        print(i**2)
        time.sleep(randint(1,10))


ps1 = multiprocessing.Process(target=Ping, args=(q,))
ps2 = multiprocessing.Process(target=Pong, args=(q,))

ps1.start()
ps2.start()
ps1.join()
ps2.join()



