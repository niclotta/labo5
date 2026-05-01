#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:19:25 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/pinzas/datasets.py, 2026-05-01 Friday 16:27:33 nclotta>

# sinlaser_{i}.avi,
# (41 * 1.2) px de desplazamiento posible,
# memoria = 40 frames.
sinlaser = [
      # d, thr, minmss, p
      [41, 1.2, 1.85e4, [0, 1]],
      [41, 1.2, 1.95e4, [0, 1, 3, 6, 9, 10]],
      [41, 1.2, 1.95e4, [0, 1, 2, 3, 6, 8]],
      [41, 1.2, 1.85e4, [2, 3, 5, 13, 15]],
      [0,  0,        0, []], # el 4 se skippea
      [41, 1.2, 1.75e4, [0,1, 2, 3, 5, 11]],
      [41, 1.2, 1.85e4, [0, 1, 2, 6]],
      [41, 1.2, 1.85e4, [0, 2, 3, 4, 5, 12]],
      [41, 1.2, 1.85e4, [0, 1, 2, 5]],
      [41, 1.2, 1.85e4, [1, 3, 4, 5, 6, 7, 9, 10]],
      [41, 1.2, 1.85e4, [1, 2, 3, 7]]
    ]

# particulaatrapada_{i}.avi
# 
# 
partatrapada = [
    ]

atrapada = [
    ]




todo = [[sinlaser, "sinlaser"],
        [partatrapada, "particulaatrapada"],
        [atrapada, "atrapada"],
    ]









# eof
