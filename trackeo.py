#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:16:22 2026

@author: nclotta
"""

import numpy as np
import matplotlib.pyplot as plt
import trackpy as tp
import pims

# print(f"Version de trackpy: {tp.__version__}")
# v0.7

@pims.pipeline
def g(img):
    return img[:, :, 1]

def track_vid(v_in):
  frames = pims.open(v_in)
  tp.quiet()
  q = tp.link(tp.batch(list(g(frames)), invert=True, diameter=41, threshold=1.2, minmass=1.85e4), 30, memory=2)
  print(q)
  tp.annotate(q[(q['particle'] == 0) & (q['frame'] == 0)], frames[0])
#  plt.imshow(frames[0])
#  tp.plot_traj(q[q['particle'] == 0])
  plt.show()
  for i in range(2):
    tp.plot_traj(q[q['particle'] == i])
    plt.show()



  #plt.hist(part['mass'], bins=20)
  #plt.imshow(frames[0], cmap = "gray")

if __name__ == '__main__':
  track_vid("data/sinlaser_0.avi")

# eof
