#!/usr/bin/python
import math
from numpy import fft
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import scipy.fftpack
script, infile = argv

y = []
x = []
q = []
k=0
with open(infile, "r") as f:
    for line in f:
        y.append(float(line.strip('\r\n')))
        x.append(int(k))
        k+=1
Fk = fft.fft(y)
sFk = fft.fftshift(Fk)
Fkabs=np.absolute(sFk)**2
for item in Fkabs:
    k=math.log(item,10)
    q.append(k)

plt.plot(x,q)
plt.show()
