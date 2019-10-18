import multiprocessing
import time


def worker(id, t: int):
    print(f"worker {id} started")
    time.sleep(t)
    print(f"worker {id} ended")


a = multiprocessing.Process(target=worker, args=("first" , 5,))
b = multiprocessing.Process(target=worker, args=("second" , 25,))
c = multiprocessing.Process(target=worker, args=("third" , 2,))

a.start()
b.start()
c.start()

b.join()
a.join() #zombie
c.join() #zombie

