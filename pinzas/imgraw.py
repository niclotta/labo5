#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/pinzas/imgraw.py, 2026-05-10 Sunday 21:16:05 nclotta>
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import pims

px_per_um = 11.1943     # px/um, primer valor obtenido
#px_per_um = 13.40168     # px/um, segundo valor
#px_per_um = 8.92693     # px/um, tercer valor
px_per_um = 10.4307
px_per_um = 9.8283
print(11.1943-9.8283)
um_per_px = 1/px_per_um # um/px
factor_de_conv = 0.5
frames = pims.open("./data/sinlaser_7.avi")
fig, ax = plt.subplots()
ax.imshow(frames[42])

#plt.grid(color='yellow', linestyle='--', linewidth=0.5, alpha=0.7, zorder=5)
x = np.linspace(0, 1280, 8)
y = np.linspace(0, 1024, 7)
ax.set_xlim()
tx = tck.FuncFormatter(lambda x, p: f'{x*um_per_px:.1f}')
ty = tck.FuncFormatter(lambda y, p: f'{y*um_per_px:.1f}')
ax.xaxis.set_major_formatter(tx)
ax.yaxis.set_major_formatter(ty)
plt.xticks(x, fontsize=14)
plt.yticks(y, fontsize=14)
ax.set_xlabel(r'$\mathrm{\mu m}$', fontsize=14)
ax.set_ylabel(r'$\mathrm{\mu m}$', fontsize=14)
plt.tight_layout()
plt.grid(color='orange', which='major', linestyle='--', linewidth=0.5, alpha=0.83, zorder=5)
plt.minorticks_on()
plt.grid(color='orange', which='minor', linestyle='--', linewidth=0.5, alpha=0.32, zorder=5)
#plt.plot([], [], label=r'Factor de conversi\'{o}n tabulado', color='yellow')
#plt.plot([], [], label=r'Calibraci\'{o}n', color='orange')
#plt.legend()
plt.savefig("rawimg.png")
