#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:19:25 2026

@author: nclotta
"""

# Time-stamp: </Users/nclotta/Documents/__UBA/__LABO_5_CINCO/pinzas/datasets.py, 2026-05-01 Friday 18:22:48 nclotta>

# todas las particulas estan seleccionadas
# considerando (41 * 1.2) px de desplazamiento
# posible y memoria=40 frames

# sinlaser_{i}.avi
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
# SOLAMENTE la particula atrapada
partatrapada = [
      # d, thr, minmss, p
      [41, 1.2, 1.85e4, [2]],
      [41, 1.2, 1.85e4, [1]],
      [41, 1.2, 1.85e4, [4]],
      [41, 1.2, 1.85e4, [3]],
      [41, 1.2, 1.85e4, [3, 10]],

      [41, 1.2, 1.85e4, [3]],
      [41, 1.2, 1.85e4, [1]],
      [41, 1.2, 1.85e4, [5]],
      [41, 1.2, 1.85e4, [1]],
      [41, 1.2, 1.85e4, [3, 10]],

      [41, 1.2, 1.85e4, [1]],
      [41, 1.2, 1.85e4, [1]],
      [41, 1.2, 1.85e4, [1, 44]]
    ]

# atrapada_{i}.avi
atrapada = [
      # d, thr, minmss, p
      [41, 1.2, 1.85e4, [3]],
      [41, 1.2, 1.85e4, [3]],
      [0,  0,   0,      []], # por alguna razon no la agarra
      [41, 1.2, 1.85e4, [1]]
#      [0,  0,   0,      []] # esta muy fuera de foco, trackpy no agarra nada
    ]

# 10_25/latex25_agua10_{i}.avi
# 
# 
latex25 = [
      # d, thr, minmss, p
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],

      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],

      [41, 1.2, 5e3, []]
    ]

# 66_33/latex33_{i}.avi
# 
# 
latex33 = [
      # d, thr, minmss, p
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],

      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],

      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],

      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []]
    ]

# latex_100/latex100_{i}.avi
# 
#
latex100 = [
      # d, thr, minmss, p
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],

      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],

      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []],
      [41, 1.2, 5e3, []]
    ]

# particulaatrapada_{i}.avi
# particulas en browniano al mover la plataforma, NO es deriva normal
derivafzda = [
      # d, thr, minmss, p
      [41, 1.2, 1.85e4, []],
      [41, 1.2, 1.85e4, []],
      [41, 1.2, 1.85e4, []],
      [41, 1.2, 1.85e4, []],
      [41, 1.2, 1.85e4, []],

      [41, 1.2, 1.85e4, []],
      [41, 1.2, 1.85e4, []],
      [41, 1.2, 1.85e4, []],
      [41, 1.2, 1.85e4, []],
      [41, 1.2, 1.85e4, []],

      [41, 1.2, 1.85e4, []],
      [41, 1.2, 1.85e4, []],
      [41, 1.2, 1.85e4, []]
    ]

# array con todos los datasets y sus paths asociados
todo = [#[sinlaser, "sinlaser", 40, 0],
#        [partatrapada, "particulaatrapada", 40, 0],
#        [atrapada, "atrapada", 40, 0],
#        [derivafzda, "particulaatrapada", 40, 0],
        [latex25, "10_25/latex25_agua10", 20, 30],
        [latex33, "66_33/latex33", 20, 30],
#        [latex100, "latex_100/latex100", 20, 30]
    ]

# eof
