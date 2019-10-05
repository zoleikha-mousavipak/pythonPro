class A:
    def __init__(self):
        print("init")
        self._x = 20

    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")


with A() as x:
    print(x._x)
    print(type(x))

