import subprocess
from pprint import pprint

try:
    out= subprocess.getstatusoutput('ls -l /tmp/aaa/')
    if out[0] == 0:
        pprint(out[1])
    else:
        print(f"Error{out[0]}")

except subprocess.CalledProcessError as e:
    print("Can not call ls" , e , sep = "\n")