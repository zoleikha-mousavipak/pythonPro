import multiprocessing
import time


def worker(id, t: int):
    print(f"worker {id} started")
    time.sleep(t)
    print(f"worker {id} ended")
    exit(0)


t=[]
t.append(multiprocessing.Process(target=worker, args=("test" , 5,)))



for _ in t:
    _.start()
    print(_.daemon)

time.sleep(1)
print("Parent exited")
