#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:17:30 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/pinzas/calcmsd.py, 2026-05-10 Sunday 23:36:30 nclotta>

import matplotlib.pyplot as plt
import trackpy as tp
import pandas as pd
import numpy as np
import os

from pathlib import Path

import datasets
from trackeo import track_vid

# para 0.01 mm tenemos 111.9431 px,
# sale de ImageJ, no se cual es el error asociado.
px_per_um = 11.1943     # px/um
um_per_px = 1/px_per_um # um/px

def load_track_data(fn):
  q = pd.read_csv(f"{fn}_trajs.csv")
  d = pd.read_csv(f"{fn}_drift.csv")
  return q

def msd_conj(dataset, subtract_drift=True, savetofile=False, graph=False):
  for n in range(len(dataset[0])):
    if dataset[0][n][0] > 0:
      if not os.path.exists(f"./img/{dataset[1]}"):
        os.makedirs(f"./img/{dataset[1]}")
      # q, d = track_vid(f"data/{dataset[1]}_{n}.avi", dataset[0][n], mem=dataset[2], sr=dataset[3])
      q, d = load_track_data(f"{Path(dataset[1]).stem}_{n}")
      if subtract_drift:
        q = tp.subtract_drift(q, d)
      for i in dataset[0][n][3]:
        msd = tp.msd(q[q['particle'] == i], mpp=um_per_px, fps=15, max_lagtime=q['frame'].max())
        if savetofile:
          msd.to_csv(f"./csv/{dataset[1]}_{n}_part_{i}_msd.csv", index=False)
#        if graph & subtract_drift:
#          d.plot()
#          plt.savefig(f"./img/{dataset[1]}_{n}_part_{i}_drift.png", dpi=300)
#          plt.close()

if __name__ == '__main__':
  for dataset in datasets.todo:
    msd_conj(dataset, savetofile=True)

# eof
