# iterate from 1 to 10
class A:
    def __init__(self,max):
        self._max = max

    def __iter__(self):
        self._current = 0
        while self._current < self._max:
            yield self._current
            self._current += 1


a = A(10)
# b = next(a)

for item in a:
    print(item)