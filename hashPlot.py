#!/usr/bin/env python3

import sys
import os
from sys import argv

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
   


