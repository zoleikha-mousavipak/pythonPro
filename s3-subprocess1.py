import subprocess
from pprint import pprint

try:
    out = subprocess.check_output(['ls', '-l', '/tmp/*'])
    pprint(out.decode())
except subprocess.CalledProcessError as e:
    print("Can not call ls" , e , sep = "\n")