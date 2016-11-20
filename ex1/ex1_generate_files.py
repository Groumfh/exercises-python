#!/usr/bin/env python
import random
import os
import shutil

data = [1008, 1368, 1260, 1188, 1248, 1212,
        1404, 1368, 396, 384, 792, 1368, 1164,
        1416, 1332, 384, 1392, 1404, 384, 1308, 468,
        1164, 384, 1200, 1212, 1188, 1332, 1200, 1212, 396]
if __name__ == '__main__':
    dest = "./data"
    if os.path.exists(dest):
        shutil.rmtree(dest)
    val3 = 10
    val4 = val3+2
    for i in range(val3):
        val = i*7 - i+5
        val2 = i*3 - i+7
        deep = random.randint(1,2)
        path = dest
        for d in range(deep):
            folder = "folder_{0}".format(random.randint(1,5))
            path = os.path.join(path,folder)
        if not os.path.exists(path):
            os.makedirs(path)
        with open(os.path.join(path,"file_{0}.txt").format(val),'w') as file:
            content = ":".join(str(x/val4+val2) for x in [val*val4] + data[i*2+val3:i*2+2+val3])
            file.write(content)