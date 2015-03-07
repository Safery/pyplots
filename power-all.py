#!/usr/bin/python
from numpy import fft
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib.backends.backend_pdf import PdfPages


pp = PdfPages('multipage.pdf')

for file in sys.argv:

    with open(file, "r") as f:
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
    plt.savefig(pp, format='pdf')
    pp.close()




