import subprocess
from pprint import pprint

try:
    out = subprocess.getoutput('ls -l /tmp/aaa/')
    pprint(out)

except subprocess.CalledProcessError as e:
    print("Can not call ls" , e , sep = "\n")