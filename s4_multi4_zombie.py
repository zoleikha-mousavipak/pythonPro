import multiprocessing
import time


def worker(id, t: int):
    print(f"worker {id} started")
    time.sleep(t)
    print(f"worker {id} ended")


t=[]
t = multiprocessing.Process(target=worker, args=("first" , 5,))



for _ in t:
    _.start()
    print(_.deamen)

time.sleep(1)
print("Parent exited")
