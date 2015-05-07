#!/usr/bin/env python3

#
# example data for this file is in the file .hashtags in this repo
#

import Image
from numpy import fft
import numpy as np
import matplotlib.pyplot as plt
import sys

infile = sys.argv[1]
hashTags = []
tagFrequency = []
countList = []

def tagFunc():
    pass
def freqFunc():
    pass
def countFunc():
    pass

with open(infile) as f:
    for line in f:
        linelist=line.split()
        if linelist[0]="#":
            tagFunc(linelist)
        else:
            linelist = linelist.replace(",","")
            if len(linelist) > 3:
                freqFunc()
            else:
                countFunc():
