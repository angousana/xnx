import os
from concurrent.futures import ThreadPoolExecutor
from sys import stdout

def get(name):
    try:
        with open(str(name), "r") as getf:
            file=getf.readlines()
            lines = []
            for x in file:
                lines.append(x.replace("\n", ""))
            return lines
    except Exception as e:
        pass
    return []
def app(name, this):
    with open(str(name), "a") as a:
        a.write(str(this)+"\n")
        a.close()
        return True
    return False
def put(name, this):
    with open(str(name), "w") as a:
        a.write(str(this))
        a.close()
        return True
    return False
def rem(name):
    os.system("rm -rf "+str(name))

def exe(workers):
    return ThreadPoolExecutor(max_workers=workers)
def printf(thiz):
    stdout.write("\x1b[K%s\r" % thiz)

import base64

def b64e(x):
    return (base64.b64encode(x.encode()).decode())
def b64d(x):
    try:
        return (base64.b64decode(x.encode()).decode())
    except Exception as x:
        return

ltp=True