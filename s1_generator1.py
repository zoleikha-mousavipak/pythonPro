import sys
from humanize import naturalsize


# range(0,10)
def func1(i,max):
    # i = 0
    out= []
    while i < max:
        out.append(i)
        i += 1
    return out


# generator
def func2(i,max):
    while i < max:
        yield i
        i += 1



print(naturalsize(sys.getsizeof(func1(0,10)), gnu=True))
print(naturalsize(sys.getsizeof(func1(0,100)), gnu=True))
print(naturalsize(sys.getsizeof(func1(0,100000)), gnu=True))
print(naturalsize(sys.getsizeof(func1(0,10000000)), gnu=True))


print(naturalsize(sys.getsizeof(func2(0,10)), gnu=True))
print(naturalsize(sys.getsizeof(func2(0,100)), gnu=True))
print(naturalsize(sys.getsizeof(func2(0,100000)), gnu=True))
print(naturalsize(sys.getsizeof(func2(0,10000000)), gnu=True))