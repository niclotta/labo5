#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:26:07 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/git_repo/zeeman/triang.py, 2026-06-01 Monday 22:43:32 nclotta>

from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from scipy.stats import linregress
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
import os

import datasets

#datasets.select[]

if __name__ == '__main__':
    for data in datasets.select['sin avg con B monitores ds1 26 del 5']:
        fig, ax = plt.subplots(1, 1, figsize=(10, 7), sharex=True)
        pctg_extremos = 0.34
        n     = len(data[0].t1)
        n_ext = int(n * pctg_extremos)
        mask = np.zeros(n, dtype=bool)
        mask[:n_ext]  = True
        mask[-n_ext:] = True
        coef  = np.polyfit(data[0].t1[mask], data[0].ch1[mask], deg=1)
        rampa = np.polyval(coef, data[0].t1)
        snl_1 = data[0].ch1 - rampa
        coef  = np.polyfit(data[0].t1[mask], data[0].ch2[mask], deg=1)
        rampa = np.polyval(coef, data[0].t1)
        snl_2 = data[0].ch2 - rampa
        i_inicio = int(n * pctg_extremos)
        i_fin    = int(n * (1 - pctg_extremos))
        t_zoom     = data[0].t1[i_inicio:i_fin]
        snl_1_zoom = snl_1[i_inicio:i_fin]
        plt.plot(t_zoom, snl_1_zoom, label=r"Monitor $+$", color='red', alpha=1, lw=2)
#        plt.plot(t_zoom, snl_1_zoom - snl_2_zoom, label='DAVS', color='green')
#        ax.xaxis.set_major_formatter(tck.FuncFormatter(lambda x, pos: f"{calibracion.cal(x) * 1e-9:.2f}"))
        plt.ylabel("Voltaje (V)", fontsize=18)
#        plt.xlabel(r"$\nu$ (THz)", fontsize=18)
        plt.xlabel("Tiempo (u.a.)", fontsize=18)
        plt.legend(fontsize=18)
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)
        plt.grid(alpha=0.3)
        plt.tight_layout()
#        pmask, prop = find_peaks(np.abs(data[0].ch1), distance=10, prominence=0.085)
#        plt.scatter(data[0].t1[pmask], data[0].ch1[pmask], color='red')
        if not os.path.exists("./img/" + data[1]):
            os.makedirs("./img/" + data[1])
        plt.savefig("./img/" + data[1] + "/" + data[2] + ".png", dpi=256)
        plt.close()


# eof
