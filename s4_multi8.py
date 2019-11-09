import multiprocessing
import time

# useing shared value in multi processing in force situations

shared_value = 0

def worker(id, t:int):
    global shared_value
    print(f"worker {id} started")
    time.sleep(t)
    print(shared_value)
    shared_value = t
    print(f"worker {id} ended")
    print(shared_value)


p =[]
p.append(multiprocessing.Process(target=worker, args=("test1" , 5)))
p.append(multiprocessing.Process(target=worker, args=("test2" , 10)))


for _ in p:
    _.start()

for _ in p:
    _.join()

#