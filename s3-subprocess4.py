import subprocess
from pprint import pprint

try:
    out = subprocess.call(['ls', '-l', '/tmp/*'])
    pprint(out)
except subprocess.CalledProcessError as e:
    print("Can not call ls" , e , sep = "\n")