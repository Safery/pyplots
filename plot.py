#!/usr/bin/python
import matplotlib.pyplot as plt
from sys import argv
script, infile = argv

v = []
x = []
k=0
with open(infile, "r") as f:
    for line in f:
        v.append(float(line.strip('\r\n')))
        x.append(int(k))
        k+=1

plt.plot(x,v)
plt.show()
plt.savefig('p'+infile.strip('eFULL')+'.pdf')
plt.savefig('p'+infile.strip('eFULL')+'.jpg')

