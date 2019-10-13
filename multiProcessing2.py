import multiprocessing
import time
import random


class MyProcess(multiprocessing.Process):

    def __init__(self, id , wait):
        super().__init__()
        self.id = id
        self.wait = wait


    def run(self) -> None :
        time.sleep(self.wait)
        print("test", self.id, self.pid)


# a = MyProcess()
# a.start()

core = multiprocessing.cpu_count()

plist=[]
for _ in range(core):
    # plist.append(MyProcess())
    # plist[-1].start()
    p = MyProcess(_, random.randint(5,15))
    plist.append(p)
    p.start()

