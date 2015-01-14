#!/usr/bin/python

import time
import requests
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
script, infile = argv
k = 1
v = []
x = []

while True:
    req = requests.get("http://coinbase.com/api/v1/prices/historical?page="+str(k))
    if req.status_code == 200:
        with open(infile,'a') as f:
            f.write('\n'+req.content)
            x.append(int(k))
            print(req.content)
    else:
        print("sorry")
    k+=1
    if req.content == "":
        break

with open(infile,'r') as g:
    for line in g:
        v.append(float(line[26:].strip('\n')))

plt.plot(x,v)
plt.show()
