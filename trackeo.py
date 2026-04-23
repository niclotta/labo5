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

print(f"Version de trackpy: {tp.__version__}")

def g(img):
    return img[:, :, 1]

def track_vid(v_in):
  frames = pims.open(v_in)
  ppf_x = []
  ppf_y = []
  part = tp.locate(g(frames[0]), invert=True, diameter=41, minmass=2.1e4)
  for i in range(11):
    p = tp.locate(g(frames[i]), invert=True, diameter=41, minmass=2.1e4)
    print(p)
    #ppf_x.append(p['x'])
    #ppf_y.append(p['y'])
#  plt.plot(ppf_x, ppf_y)
#  plt.show()
  #plt.hist(part['mass'], bins=20)
  #plt.show()
  print(part.head())
  tp.annotate(part, frames[0])
  #plt.imshow(frames[0], cmap = "gray")
  plt.show()

track_vid("data/sinlaser_0.avi")

# eof
