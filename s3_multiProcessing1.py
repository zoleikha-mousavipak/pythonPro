import multiprocessing
import time
import random


class MyProcess(multiprocessing.Process):

    def __init__(self, id , wait):
        super().__init__() # call parent init(constructor)
        self.id = id
        self.wait = wait


    def run(self) -> None :
        time.sleep(2)
        print("test", self.pid)


# a = MyProcess()
# a.start()


plist=[]
for _ in range(5):
    # plist.append(MyProcess())
    # plist[-1].start()
    p = MyProcess(_, random.randint(1,3))
    plist.append(p)
    p.start()

