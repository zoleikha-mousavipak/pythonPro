import multiprocessing
import time
import random
import requests

class MyProcess(multiprocessing.Process):
    def __init__(self, id, wait):
        super().__init__()
        self.id = id
        self.wait = wait

    def run(self) -> None:
        # while True:
        #     pass

        time.sleep(self.wait)
        print("test" , self.id , self.pid)
        # requests.get('http://mirror.exetel.com.au/pub/ubuntu/xubuntu-releases/18.04/release/xubuntu-18.04-desktop-amd64.iso')


core = multiprocessing.cpu_count()
plist = []
for _ in range(core):
    plist.append(MyProcess(_, random.randint(5,15)))
    plist[-1].start()
    # print(MyProcess(2, 1))
    # MyProcess(2, 1).terminate

for _ in plist:
    _.join()
print("I am Parent")