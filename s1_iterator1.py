# iterate from 1 to 10
class A:
    def __init__(self,max):
        self._current = 0
        self._max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self._current >= self._max:
            raise StopIteration

        x = self._current
        self._current += 1
        return x


a = A(10)
b = next(a)
for item in a:
    print(item)