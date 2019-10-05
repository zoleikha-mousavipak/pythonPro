from functools import reduce

class IP:

    def __init__(self, ip:str, netmask:str):
        if isinstance(ip , int):
            # self._octets = (
            #     ip >> 24 & (2**0 -1),
            #     ip >> 16 & (2**8 -1),
            #     ip >> 8  & (2**16-1),
            #     ip >> 0  & (2**24-1)
            # )
            t = f"{ip:b}"
            self._octets = (
                int(t[0:8],2),
                int(t[8:16],2),
                int(t[16:24],2),
                int(t[24:32],2))
        else:
            self._octets = tuple([int(_) for _ in ip.split(".")])

        self._network_address = reduce(lambda x,y: x << 8 | y, self._octets)

        if isinstance(netmask, int):
            self._mask = ((1 << netmask) -1) << (32 - netmask)

        elif isinstance(netmask, str):
            # 255.255.255.0

            d = [int(_) for _ in ip.split(".")]
            # m = 0
            # for _ in d:
            #     m = (m << 8) | _
            m = reduce(lambda x,y: x << 8 | y, d)

        self._network_address &= self._mask
        self._broadcast_address = self._network_address | (2 ** f"{self._mask:b}".count("0") - 1)


    def __iter__(self):
        self._current_ip = self._network_address
        return self

    def __next__(self):
        self._current_ip += 1
        if self._current_ip >= self._broadcast_address:
            raise StopIteration
        return IP(self._current_ip, 32)

    def __str__(self):
        if self._mask == 2**32 - 1:
            return ".".join([str(_) for _ in self._octets])
        else:
            return "{}/{}".format(".".join([str(_) for _ in self._octets]),
                                  f"{self._mask:b}".count("1"))

a = IP("192.168.1.1", 23)
# b = IP("192.168.8.1", 24)
# c = IP("192.168.9.1", 32)
# print(a)
# print(b)
# print(c)

for ip in a:
    print(ip)
