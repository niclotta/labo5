#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:16:22 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/pinzas/trackeo.py, 2026-05-02 Saturday 17:59:36 nclotta>

import numpy as np
import matplotlib.pyplot as plt
import trackpy as tp
import pims
import os

from pathlib import Path

import datasets

# print(f"Version de trackpy: {tp.__version__}")
# v0.7

@pims.pipeline
def g(img):
    return img[:, :, 1]

def track_vid(v_in, data, graph=False, imgpath="./img", mem=40, sr=0):
  frames = pims.open(v_in)
  tp.quiet()
  if sr == 0:
    search_range = data[0]*data[1]
  else:
    search_range = sr
  q = tp.link(tp.batch(list(g(frames)), invert=True,
                       diameter=data[0], threshold=data[1],
                       minmass=data[2]), search_range=search_range, memory=mem)
  if graph:
#    plt.hist(q['particle'], bins=q['particle'].max(), ec='r', color='skyblue')
#    plt.savefig(f"{imgpath}/{Path(v_in).stem}_histo_parts.png", dpi=300)
#    plt.close()
#    plt.hist(q['mass'], bins=q['particle'].max(), ec='r', color='skyblue')
#    plt.savefig(f"{imgpath}/{Path(v_in).stem}_histo_mass.png", dpi=300)
#    plt.close()
    if len(data[3]) > 0:
      n_parts = len(data[3])
    else:
      n_parts = q['particle'].max()
    for i in range(n_parts):
      if len(data[3]) > 0:
        j = data[3][i]
      else:
        j = i
      fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
      fnum = q[q['particle'] == j]['frame'].min()
      tp.annotate(q[(q['particle'] == j) &
                    (q['frame'] == fnum)], frames[fnum], ax=ax1)
      tp.plot_traj(q[q['particle'] == j], ax=ax2)
      plt.savefig(f"{imgpath}/{Path(v_in).stem}_part_{j}.png", dpi=300)
      plt.close()
  return q

if __name__ == '__main__':
  for dataset in datasets.todo:
    for n in range(len(dataset[0])):
      if dataset[0][n][0] > 0:
        if not os.path.exists(f"./img/{dataset[1]}"):
          os.makedirs(f"./img/{dataset[1]}")
        track_vid(f"data/{dataset[1]}_{n}.avi", dataset[0][n], graph=True,
                  imgpath=f"./img/{dataset[1]}", mem=dataset[2], sr=dataset[3])

# eof
