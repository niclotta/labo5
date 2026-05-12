#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:16:22 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/pinzas/trackeo.py, 2026-05-11 Monday 18:15:17 nclotta>

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import trackpy as tp
import pims
import os

from pathlib import Path

import datasets

px_per_um = 11.1943     # px/um
um_per_px = 1/px_per_um # um/px

# print(f"Version de trackpy: {tp.__version__}")
# v0.7

@pims.pipeline
def g(img):
    return img[:, :, 1]

def track_graph(q, data, frames, img_name):
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
      plt.gca().set_aspect('equal')
      tp.plot_traj(q[q['particle'] == j], ax=ax2)
      x = np.linspace(0, 1280, 8)
      y = np.linspace(0, 1024, 7)
      tx = tck.FuncFormatter(lambda x, p: f'{x*um_per_px:.1f}')
      ty = tck.FuncFormatter(lambda y, p: f'{y*um_per_px:.1f}')
      ax1.xaxis.set_major_formatter(tx)
      ax1.yaxis.set_major_formatter(ty)
      ax1.tick_params(axis='y', labelsize=18)
      ax1.tick_params(axis='x', labelsize=18)
      ax1.set_xlabel(r'$\mathrm{\mu m}$', fontsize=18)
      ax1.set_ylabel(r'$\mathrm{\mu m}$', fontsize=18)
      ax2.xaxis.set_major_formatter(tx)
      ax2.yaxis.set_major_formatter(ty)
      ax2.tick_params(axis='x', labelsize=18)
      ax2.tick_params(axis='y', labelsize=18)
      ax2.set_xlabel(r'$\mathrm{\mu m}$', fontsize=18)
      ax2.set_ylabel(r'$\mathrm{\mu m}$', fontsize=18)
      plt.tight_layout()
      plt.savefig(f"{img_name}_{j}.png", dpi=300)
      plt.close()

def track_vid(v_in, data, graph=False, imgpath="./img", csvpath="./csv",
              mem=40, sr=0, savetofile=False, read_data=True):
  frames = pims.open(v_in)
  tp.quiet()
  if sr == 0:
    search_range = data[0]*data[1]
  else:
    search_range = sr
  if read_data:
    q = pd.read_csv(f"./csv/{Path(v_in).stem}_trajs.csv")
    d = pd.read_csv(f"./csv/{Path(v_in).stem}_drift.csv")
  else:
    q = tp.link(tp.batch(list(g(frames)), invert=True,
                       diameter=data[0], threshold=data[1],
                       minmass=data[2]), search_range=search_range, memory=mem)
    d = tp.compute_drift(q)
    q = q[q['particle'].isin(data[3])]
  if savetofile:
    q.to_csv(f"{csvpath}/{Path(v_in).stem}_trajs.csv")
    d.to_csv(f"{csvpath}/{Path(v_in).stem}_drift.csv")
  if graph:
    track_graph(q, data, frames, f"{imgpath}/{Path(v_in).stem}_part_")
#    plt.hist(q['particle'], bins=q['particle'].max(), ec='r', color='skyblue')
#    plt.savefig(f"{imgpath}/{Path(v_in).stem}_histo_parts.png", dpi=300)
#    plt.close()
#    plt.hist(q['mass'], bins=q['particle'].max(), ec='r', color='skyblue')
#    plt.savefig(f"{imgpath}/{Path(v_in).stem}_histo_mass.png", dpi=300)
#    plt.close()
  return q, d

if __name__ == '__main__':
  if not os.path.exists(f"./csv"):
    os.makedirs(f"./csv")
  for dataset in datasets.todo:
    for n in range(len(dataset[0])):
      if dataset[0][n][0] > 0:
        if not os.path.exists(f"./img/{dataset[1]}"):
          os.makedirs(f"./img/{dataset[1]}")
        track_vid(f"data/{dataset[1]}_{n}.avi", dataset[0][n], graph=True, read_data=False,
                  imgpath=f"./img/{dataset[1]}", savetofile=False, mem=dataset[2], sr=dataset[3])

# eof
