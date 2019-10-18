import multiprocessing
import time


def worker(id, t: int):
    print(f"worker {id} started")
    time.sleep(t)
    print(f"worker {id} ended")
    exit(1)

t=[]
t.append(multiprocessing.Process(target=worker, args=("first" , 5,)))
t.append(multiprocessing.Process(target=worker, args=("second" , 25,)))
t.append(multiprocessing.Process(target=worker, args=("third" , 2,)))

for _ in t:
    _.start()

all_exited = False
while not all_exited:
    all_exited = True
    for _ in t:
        _.join(1)
        if _.is_alive():
            all_exited = False
        else:
            print(_.exitcode)
            t.remove(_)

