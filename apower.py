#!/usr/bin/python

import Image
from numpy import fft
import numpy as np
import matplotlib.pyplot as plt
import sys

del sys.argv[0]

for infile in sys.argv:

    with open(infile, "r") as f:
        y = []
        x = []
        k=0
        for line in f:
            y.append(float(line.strip('\r\n')))
            x.append(int(k))
            k+=1
    Fk = fft.fft(y)
    sFk = fft.fftshift(Fk)
    Fkabs=np.absolute(sFk)**2
    plt.plot(x,Fkabs)
    plt.show()
