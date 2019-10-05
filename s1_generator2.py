import sys
from humanize import naturalsize
import time


# range(0,10)
def func1(max):
    i = 0
    out= []
    while i < max:
        out.append(i)
        i += 1
    return out


# generator
def func2(max):
    i = 0
    while i < max:
        yield i
        i += 1


start1 = time.process_time()
start2 = time.perf_counter()
out1 = func1(1000000)
print(time.process_time() - start1)
print(time.perf_counter() - start2)

print("="*40)


start1 = time.process_time()
start2 = time.perf_counter()
out2 = func2(1000000)
print(time.process_time() - start1)
print(time.perf_counter() - start2)

print("+"*40)

start1 = time.process_time()
start2 = time.perf_counter()
for item in out1:
    pass
print(time.process_time() - start1)
print(time.perf_counter() - start2)

print("="*40)


start1 = time.process_time()
start2 = time.perf_counter()
for item in out2:
    pass
print(time.process_time() - start1)
print(time.perf_counter() - start2)

print("+"*40)