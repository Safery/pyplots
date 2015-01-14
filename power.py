#!/usr/bin/python

from numpy import fft
import numpy as np
import matplotlib.pyplot as plt
from sys import argv
import scipy.fftpack
script, infile = argv

y = []
x = []
k=0
with open(infile, "r") as f:
    for line in f:
        y.append(float(line.strip('\r\n')))
        x.append(int(k))
        k+=1
Fk = fft.fft(y)
sFk = fft.fftshift(Fk)
Fkabs=np.absolute(sFk)**2
plt.plot(x,Fkabs)
plt.show()
