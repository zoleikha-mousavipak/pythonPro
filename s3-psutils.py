# monitoring Tools

import psutil
import time

for _ in range(100):
    print("\r", psutil.cpu_freq().current, end="", flush=True)
    # print("\r", psutil.cpu_stats(), end="", flush=True)
    # print("\r", psutil.disk_usage("/"), end="", flush=True)
    # print("\r", psutil.disk_partitions(), end="", flush=True)
    # print("\r", psutil.virtual_memory(), end="", flush=True)

    time.sleep(.1)