#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:26:07 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/git_repo/zeeman/analavs.py, 2026-05-28 Thursday 16:37:10 nclotta>

from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from scipy.stats import linregress
import matplotlib.pyplot as plt
import os

import datasets

def lineal(x, a, b):
    return x * a + b



if __name__ == '__main__':
    for data in datasets.all:
        plt.plot(data[0].t1, data[0].ch1)
        popt, pcov = curve_fit(lineal, data[0].t1, data[0].ch1)
        ajuste = lineal(data[0].t1, *popt)
        plt.plot(data[0].t1, ajuste)
        if not os.path.exists("./img/" + data[1]):
            os.makedirs("./img/" + data[1])
        plt.savefig("./img/" + data[1] + "/" + data[2] + ".png")
        plt.close()


# eof
