#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:17:30 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/pinzas/calcmsd.py, 2026-05-02 Saturday 18:18:20 nclotta>

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

def msd_part(q, i, subtract_drift=True):
  part = q[q['particle'] == i]
  if subtract_drift:
    d = tp.compute_drift(part)
    part = tp.subtract_drift(part.copy(), d)
  else:
    d = None                                # esto del lagtime es dudoso
  msd = tp.msd(part, mpp=um_per_px, fps=15, max_lagtime=q['frame'].max())
  return msd, d

def msd_conj(dataset, subtract_drift=True, savetofile=False, graph=False):
  emsd  = []
  drift = []
  index = []
  for n in range(len(dataset[0])):
    if dataset[0][n][0] > 0:
      if not os.path.exists(f"./img/{dataset[1]}"):
        os.makedirs(f"./img/{dataset[1]}")
      q = track_vid(f"data/{dataset[1]}_{n}.avi", dataset[0][n], mem=dataset[2], sr=dataset[3])
      for i in dataset[0][n][3]:
        msd, d = msd_part(q, i, subtract_drift=subtract_drift)
        emsd.append(msd)
        drift.append(d)
        index.append([n, i])
        if savetofile:
          msd.to_csv(f"./img/{dataset[1]}/{dataset[1]}_{n}_part_{i}_msd.csv", index=False)
          if subtract_drift:
            d.to_csv(f"./img/{dataset[1]}/{dataset[1]}_{n}_part_{i}_drift.csv", index=False)
        if graph & subtract_drift:
          d.plot()
          plt.savefig(f"./img/{dataset[1]}/{dataset[1]}_{n}_part_{i}_drift.png", dpi=300)
          plt.close()
  return emsd, drift, index

if __name__ == '__main__':
  for dataset in datasets.todo:
    msd_conj(dataset, subtract_drift=True, savetofile=True, graph=True)

# eof
