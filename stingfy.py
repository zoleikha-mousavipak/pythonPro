class A:

    def __init__(self,x):
        self.x = x

    def __str__(self):
        return "A - {}".format(self.x)
        # return f"{self.x}"

    def __repr__(self):
        # return f"A({self.x})"
        return f"{self.x}"


a = A(10)
print(a)
print(repr(a))

print(type(a))