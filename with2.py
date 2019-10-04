class MyOpen:
    def __init__(self, path, mode):
        self._path = path
        self._mode = mode
        self._f = None

    def __enter__(self):
        self._f = open(self._path, self._mode)
        return self._f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._f.close()


with MyOpen("/var/log/syslog","r") as x:
    print(x.read())