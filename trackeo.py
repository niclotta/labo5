#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:16:22 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/pinzas/trackeo.py, 2026-05-01 Friday 16:26:43 nclotta>

import numpy as np
import matplotlib.pyplot as plt
import trackpy as tp
import pims

from pathlib import Path

import datasets

# print(f"Version de trackpy: {tp.__version__}")
# v0.7

@pims.pipeline
def g(img):
    return img[:, :, 1]

def track_vid(v_in, n, data, graph=False):
  frames = pims.open(v_in)
  tp.quiet()
  q = tp.link(tp.batch(list(g(frames)), invert=True,
                         diameter=data[n][0],
                         threshold=data[n][1],
                         minmass=data[n][2]), data[n][0]*data[n][1], memory=40)
  if graph:
    plt.hist(q['particle'], bins=q['particle'].max(), ec='r', color='skyblue')
    plt.savefig(f"./img/{Path(v_in).stem}_histo_parts.png", dpi=300)
    plt.close()
    if len(data[n][3]) > 0:
      n_parts = len(data[n][3])
    else:
      n_parts = q['particle'].max()
    for i in range(n_parts):
      if len(data[n][3]) > 0:
        j = data[n][3][i]
      else:
        j = i
      fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
      fnum = q[q['particle'] == j]['frame'].min()
      tp.annotate(q[(q['particle'] == j) &
                    (q['frame'] == fnum)], frames[fnum], ax=ax1)
      tp.plot_traj(q[q['particle'] == j], ax=ax2)
      plt.savefig(f"./img/{Path(v_in).stem}_part_{j}.png", dpi=300)
      plt.close()
  return q

if __name__ == '__main__':
  for dataset in datasets.todo:
    for n in range(len(dataset[0])):
      if dataset[0][n][0] > 0:
        track_vid(f"data/{dataset[1]}_{n}.avi", n, dataset[0], graph=True)

# eof
