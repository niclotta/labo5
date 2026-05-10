#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/pinzas/imgraw.py, 2026-05-10 Sunday 19:48:09 nclotta>
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import pims

px_per_um = 11.1943     # px/um
um_per_px = 1/px_per_um # um/px
factor_de_conv = 
frames = pims.open("./data/sinlaser_7.avi")
fig, ax = plt.subplots()
ax.imshow(frames[42])
x = np.linspace(0, 1280, 10)
y = np.linspace(0, 1024, 8)
tx = tck.FuncFormatter(lambda x, p: f'{x*factor_de_conv*um_per_px:.1f}')
ty = tck.FuncFormatter(lambda y, p: f'{y*factor_de_conv*um_per_px:.1f}')
ax.xaxis.set_major_formatter(tx)
ax.yaxis.set_major_formatter(ty)
plt.grid(color='yellow', linestyle='--', linewidth=0.5, alpha=0.7, zorder=5)
x = np.linspace(0, 1280, 10)
y = np.linspace(0, 1024, 8)
tx = tck.FuncFormatter(lambda x, p: f'{x*um_per_px:.1f}')
ty = tck.FuncFormatter(lambda y, p: f'{y*um_per_px:.1f}')
ax.xaxis.set_major_formatter(tx)
ax.yaxis.set_major_formatter(ty)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
ax.set_xlabel(r'$\mathrm{\mu m}$', fontsize=14)
ax.set_ylabel(r'$\mathrm{\mu m}$', fontsize=14)
plt.tight_layout()
plt.grid(color='orange', linestyle='--', linewidth=0.5, alpha=0.7, zorder=5)
plt.plot([], [], label=r'Factor de conversi\'{o}n tabulado', color='yellow')
plt.plot([], [], label=r'Calibraci\'{o}n', color='orange')
plt.legend()
plt.savefig("rawimg.png")
