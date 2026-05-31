#!/usr/bin/env python3
"""
resta la rampa a uno de los canales y devuelve los arrays corregidos
"""

import importlib.util, pathlib
import numpy as np
import matplotlib.pyplot as plt

def cargar(filepath):
    fp = pathlib.Path(filepath)
    spec = importlib.util.spec_from_file_location(fp.stem, fp)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

file= "/content/zeedat/"

d  = cargar(file)
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
plt.show()

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
plt.show()


fuera_picos = señal[mask]
print(f"Residuo en extremos — media: {fuera_picos.mean():.5f} V,  std: {fuera_picos.std():.5f} V")



#zoom

i_inicio = int(n * 0.15)
i_fin    = int(n * 0.85)

t_zoom    = t[i_inicio:i_fin]
señal_zoom = señal[i_inicio:i_fin]

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(t_zoom, señal_zoom, lw=0.8, color='seagreen')
ax.axhline(0, color='gray', lw=0.5, ls='--')
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('ΔV (V)')
ax.set_title('Zona central del barrido')
ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()

t_corr   = t
sig_corr = señal

#eof
