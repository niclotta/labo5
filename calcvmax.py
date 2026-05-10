#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:17:30 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/pinzas/calcvmax.py, 2026-05-10 Sunday 20:28:27 nclotta>

import numpy as np
import matplotlib.pyplot as plt
import trackpy as tp
import os

import datasets
from trackeo import track_vid

# para 0.01 mm tenemos 111.9431 px,
# sale de ImageJ, no se cual es el error asociado.
px_per_um = 11.1943     # px/um
um_per_px = 1/px_per_um # um/px

def msd_part(q, i, d, subtract_drift=True):
  part = q[q['particle'] == i]
  if subtract_drift:
    part = tp.subtract_drift(part.copy(), d)
  msd = tp.msd(part, mpp=um_per_px, fps=15, max_lagtime=q['frame'].max())
  return msd

def msd_conj(dataset, subtract_drift=True, savetofile=False, graph=False, save_drift=False):
  emsd  = []
  drift = []
  index = []
  for n in range(len(dataset[0])):
    if dataset[0][n][0] > 0:
      if not os.path.exists(f"./results/{dataset[1]}"):
        os.makedirs(f"./results/{dataset[1]}")
      q = track_vid(f"data/{dataset[1]}_5.avi", dataset[0][n],
                      graph=True, imgpath=f"./results", mem=dataset[2], sr=dataset[3])
      d = tp.compute_drift(q)
      for i in dataset[0][n][3]:
        msd = msd_part(q, i, d, subtract_drift=subtract_drift)
        emsd.append(msd)
        drift.append(d)
        index.append([n, i])
        if savetofile:
          msd.to_csv(f"./results/{dataset[1]}_5_part_{i}_msd.csv", index=False)
          if subtract_drift & save_drift:
            d.to_csv(f"./results/{dataset[1]}_5_part_{i}_drift.csv", index=False)
        if graph & subtract_drift:
          d.plot()
          if not os.path.exists(f"./img/{dataset[1]}"):
            os.makedirs(f"./img/{dataset[1]}")
          plt.savefig(f"./img/{dataset[1]}_5_part_{i}_drift.png", dpi=300)
          plt.close()
  return emsd, drift, index

if __name__ == '__main__':
  for dataset in datasets.todo:
    msd_conj(dataset, save_drift=True, savetofile=True)

# eof
