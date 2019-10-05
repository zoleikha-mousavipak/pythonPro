class A:
    def __init__(self, data):
        self._data = data

    def __add__(self, other):
        # if not isinstance(other , A):
        #     raise ValueError
        assert isinstance(other, A)
        return A(self._data + other._data)

    def __str__(self):
        return str(self._data)


class B(A):
    def __init__(self, data):
        self._data = data


class C:
    def __init__(self, data):
        self._data = data


a = A(10)
b = A(11)
z = a + b
print(z)

c = B(10.5)
x = a + c
print(x)

d = C(10.5)
y = a + d
print(y)