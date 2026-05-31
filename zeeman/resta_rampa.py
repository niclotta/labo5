#!/usr/bin/env python3
"""
resta la rampa a uno de los canales y devuelve los arrays corregidos
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import numpy as np
import os

from scipy.signal import find_peaks, savgol_filter
from scipy.interpolate import make_interp_spline

import datasets

#carpeta = 'sin avg con B monitores ds2 26 del 5'
carpeta = 'sin avg sin B DAVS monitor menos ds1 26 del 5'

if not os.path.exists("./img/" + carpeta):
    os.makedirs("./img/" + carpeta)

#for i in range(0,len(datasets.select[carpeta])):
for i in [5]:
    d  = datasets.select[carpeta][i][0]
    if carpeta == 'sin avg sin B DAVS monitor menos ds1 26 del 5':
        ch = np.asarray(d.ch2)
        t  = np.asarray(d.t2)
    else:
        t  = np.asarray(d.t1)
        ch = np.asarray(d.ch1)

    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(t, ch, lw=0.7, color='steelblue', label='Señal cruda')
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Voltaje (V)')
    ax.set_title('señal cruda')
    ax.legend()
    ax.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig("./img/" + carpeta + "/" + datasets.select[carpeta][i][2] + "_0.png", dpi=252)
    plt.close()

    print(f"Duración:   {t[-1]-t[0]:.2f} s")
    print(f"N puntos:   {len(t)}")
    print(f"Rango ch:   {ch.min():.4f} V  a  {ch.max():.4f} V")

    #restar rampa


    pctg_extremos = 0.15   # usamos el 15% inicial y 15% final

    n     = len(t)
    n_ext = int(n * pctg_extremos)

    #mascara
    mask = np.zeros(n, dtype=bool)
    mask[:n_ext]  = True
    mask[-n_ext:] = True

    # ajuste lineal en los extremos
    coef  = np.polyfit(t[mask], ch[mask], deg=1)
    rampa = np.polyval(coef, t)

    #señal corregida
    señal = ch - rampa

    #plot

    fig, axes = plt.subplots(2, 1, figsize=(12, 7), sharex=True)


    axes[0].plot(t, ch,    lw=0.7, color='steelblue', label='Señal cruda')
    axes[0].plot(t, rampa, lw=1.2, color='tomato',    label=f'Rampa ajustada  (pendiente = {coef[0]:.4f} V/s)')
    axes[0].axvspan(t[0], t[n_ext], alpha=0.12, color='gray', label='Zona de ajuste')
    axes[0].axvspan(t[-n_ext], t[-1], alpha=0.12, color='gray')
    axes[0].set_ylabel('Voltaje (V)')
    axes[0].legend(fontsize=8)
    axes[0].grid(alpha=0.3)
    axes[0].set_title('Rampa ajustada sobre los extremos')

    #señal corregida
    axes[1].plot(t, señal, lw=0.7, color='seagreen', label='Señal − rampa')
    axes[1].axhline(0, color='gray', lw=0.5, ls='--')
    axes[1].set_xlabel('Tiempo (s)')
    axes[1].set_ylabel('ΔV (V)')
    axes[1].legend(fontsize=8)
    axes[1].grid(alpha=0.3)
    axes[1].set_title('Señal corregida')

    plt.tight_layout()
    plt.savefig("./img/" + carpeta + "/" + datasets.select[carpeta][i][2] + "_1.png", dpi=252)
    plt.close()


    fuera_picos = señal[mask]
    print(f"Residuo en extremos — media: {fuera_picos.mean():.5f} V,  std: {fuera_picos.std():.5f} V")



    #zoom

    i_inicio = int(n * pctg_extremos)
    i_fin    = int(n * (1 - pctg_extremos))

    t_zoom    = t[i_inicio:i_fin]
    señal_zoom = señal[i_inicio:i_fin]
#savgol_filter(señal_zoom, window_length=51, polyorder=3)
    pmask, prop = find_peaks(np.abs(señal_zoom), height=0.005, distance=40)
    si = np.argsort(prop['peak_heights'])[::-1]
    top4 = pmask[si[:4]]
    t_del = (np.sort(t_zoom[top4]))
    tt1 = (t_del[1] - t_del[0]) # 814,5(15) MHz
    tt2 = (t_del[3] - t_del[2]) # 6,834 682 GHz
    # en Hz
    #814500000
    #6834682000000
    # e0 -> 1e-12
    # Hz -> THz
    #omega = np.interp(tt, [0.7659999999999998, 0.41600000000000015], [814500000, 6834682000000])
    #calibrador = make_interp_spline([0.41600000000000015, 0.7659999999999998], [6834682000000 * 1e-12, 814500000 * 1e-12], k=1)
    #[377.112040486, 377.111226006, 377.105205804, 377.104391324]
    coefs_freq = [377.112040486, 377.111226006, 377.105205804, 377.104391324]
    calibrador = make_interp_spline(t_del, coefs_freq, k=1)
#    fmtr = tck.FuncFormatter(lambda x, p: f"${calibrador(x):.2f}")
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(t_zoom, señal_zoom, lw=0.8, color='seagreen')
    ax.axhline(0, color='gray', lw=0.5, ls='--')
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('ΔV (V)')
    ax.set_title('Zona central del barrido')
    ax.grid(alpha=0.3)
#    ax.xaxis.set_major_formatter(fmtr)
    print(calibrador(tt1))
    print(calibrador(tt2))
    
    plt.scatter(t_zoom[top4], señal_zoom[top4], color='red')
    plt.tight_layout()
    plt.savefig("./img/" + carpeta + "/" + datasets.select[carpeta][i][2] + "_2.png", dpi=252)
    plt.close()

    t_corr   = t
    sig_corr = señal

    #eof
