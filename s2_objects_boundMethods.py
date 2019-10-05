class A:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x


class B:
    def __init__(self, x):
        self.x = x

    def get_x(self):
        return self.x


a = A(10)
print(a)
print(a.get_x())
print(A)
print(A.get_x(a))

b = B(12)
print(b.get_x())
print(B.get_x(b))
print(B.get_x(a))