from __future__ import division, unicode_literals, print_function, absolute_import
import pyvisa as visa
import numpy as np
import time
import matplotlib.pyplot as plt
import serial
import pandas as pd


class AFG3021B:
    
    def __init__(self, name='USB0::0x0699::0x0346::C034166::INSTR'):
        self._generador = visa.ResourceManager().open_resource(name)
        print(self._generador.query('*IDN?'))
        
        #Activa la salida
        self._generador.write('OUTPut1:STATe on')
        # self.setFrequency(1000)
        
    def __del__(self):
        self._generador.close()
        
    def setFrequency(self, freq):
        self._generador.write(f'FREQ {freq}')
        
    def getFrequency(self):
        return self._generador.query_ascii_values('FREQ?')
        
    def setAmplitude(self, freq):
        print('falta')
        
    def getAmplitude(self):
        print('falta')
        return 0 
    
# def de Medidor de presion       
class edwards:
    def __init__(self,port):
        if(port == None):
            print("Se necesita un puerto valido")
            return 0
        self._gauge = serial.Serial(port, baudrate=9600)     
        self._gauge.baudrate = 9600
        self._gauge.port = port
        self._gauge.bytesize = 8
        self._gauge.parity = 'N'
        self._gauge.stopbits = 1
        self._gauge.timeout = 1   
        self.open() 

    def open(self):
        if not self._gauge.is_open:
            self._gauge.open()            

    def close(self):
        self._gauge.close()	        

    def GetPressure(self):        
        pressure = ""
        while len(pressure) != 9:
            self._gauge.write(b'?GA1\r')        
            pressure = self._gauge.readline()
            if pressure[:2]=="ERR":
                print("Error message: ",pressure)
        pres = float(pressure.decode('ascii'))
        return pres
#
rm = visa.ResourceManager()
instrumentos = rm.list_resources()  
print(instrumentos)

#%% 
gen=rm.open_resource(instrumentos[-3])
print(gen.query('*IDN?'))
 
mult_1=rm.open_resource(instrumentos[-1])
print(mult_1.query('*IDN?'))

mult_2=rm.open_resource(instrumentos[-2])
print(mult_2.query('*IDN?'))
#%%

gen.query('FREQ?')
gen.query('VOLT?')

mult_1.query('MEASURE:VOLTAGE:DC?')#mult de arriba
mult_2.query('MEASURE:VOLTAGE:DC?')#mult de abajo

gen.write('VOLTage:LEVel:IMMediate:OFFS 0.1')
gen.write('VOLTage:LEVel:IMMediate:HIGH 0.1')

# #%% Conex
# controlador = edwards('COM7')
# controlador.close()

# controlador.open()
# print(controlador.GetPressure())

# #%% Error presión 
# def error_presion(p):
#   if 10**(-3)<=p<100:
#     return 0.15*p
#   elif p<10**(-3):
#     return 0.3*p

#
t = 120 #[s]
n = t/1.25 # tiempo x medición



# Esperar un tiempo antes de la siguiente medición
# time.sleep(2)  # Esperar 0.1 segundos

#%% def med

numeromed = 666

distancia = 2.0
presion_fija = 5.2

#%%

R4 = 14.8*1000

err_corrientes = []
d = [2.5, 5, 7.5]
frec = 0.5 #Hz
factor = 500

V_HV = np.arange(300, 800 + 1, 5) 

offsets = V_HV / factor 
          # volts del generador
gen.write(f'VOLTage:LEVel:IMMediate:OFFS {600/500}')
#%%

voltajes_m1 = []
voltajes_m2 = []
voltajes_a = []
corrientes = []
Dif = []

#get_ipython().run_line_magic('matplotlib', 'qt5')
gen.write('FUNC DC')

tiempo=[]
presion=[]
tiempo_inicial = time.time()
#for i in range(int(np.round(n))):

for v in offsets:   # <-- se corta solo al terminar la lista
    # gen.write(f'VOLTage:LEVel:IMMediate:HIGH {v}')
    gen.write(f'VOLTage:LEVel:IMMediate:OFFS {v}')

    tiempo_actual = time.time() - tiempo_inicial
    tiempo.append(tiempo_actual)

    #gen.write(f'VOLTage:LEVel:IMMediate:HIGH {v}') Quiza sea importante despues
    time.sleep(1)

    mult_1.open()
    mult_2.open()
    v_1 = float(mult_1.query('MEASURE:VOLTAGE:DC?')) # mult arriba
    v_2 = float(mult_2.query('MEASURE:VOLTAGE:DC?')) # mult abajo
    mult_1.close()
    mult_2.close()
    
    volt_B = v_1       #lo que medimos con el "amperimetro" -- catodo
    volt_C = v_2       #lo que medimos con el voltimetro -- anodo
    
    voltajes_m1.append(volt_C)
    voltajes_m2.append(volt_B)
    
    
    I = volt_B / R4
    corrientes.append(I)

#%%
plt.figure(figsize=(10, 6))
plt.plot(np.array(corrientes), np.array(offsets), '.-', color='r', label='Subida')
plt.plot(corrientes, voltajes_m1, 'o')
plt.xscale('log')   # eje x logarítmico

plt.xlabel('Corriente [A]')
plt.ylabel('Voltaje [V]')
plt.grid()

#%%
# ==========================================================
# GUARDAR DATOS EN CSV
# ==========================================================

df = pd.DataFrame({
    'Tiempo_s': tiempo,
    'Voltaje_plasma_V': voltajes_m1,   # volt_C
    'Voltaje_R_V': voltajes_m2,        # volt_B
    'Corriente_A': corrientes,
    'Voltaje_HV_estimado_V': offsets * factor  # opcional (HV real)
})

df.to_csv(f"datos/d{numeromed}_{distancia:.1f}_cm_aire_{presion_fija:.1f}e-1mbar_subida.csv", index=False)


voltajes_m1 = []
voltajes_m2 = []
voltajes_a = []
corrientes = []
Dif = []

#get_ipython().run_line_magic('matplotlib', 'qt5')
gen.write('FUNC DC')

tiempo=[]
presion=[]
tiempo_inicial = time.time()
#for i in range(int(np.round(n))):

#for v in offsets:   # <-- se corta solo al terminar la lista
for v in offsets[::-1]:   # <-- se corta solo al terminar la lista
    # gen.write(f'VOLTage:LEVel:IMMediate:HIGH {v}')
    gen.write(f'VOLTage:LEVel:IMMediate:OFFS {v}')

    tiempo_actual = time.time() - tiempo_inicial
    tiempo.append(tiempo_actual)

    #gen.write(f'VOLTage:LEVel:IMMediate:HIGH {v}') Quiza sea importante despues
    time.sleep(1)

    mult_1.open()
    mult_2.open()
    v_1 = float(mult_1.query('MEASURE:VOLTAGE:DC?')) # mult arriba
    v_2 = float(mult_2.query('MEASURE:VOLTAGE:DC?')) # mult abajo
    mult_1.close()
    mult_2.close()
    
    volt_B = v_1       #lo que medimos con el "amperimetro" -- catodo
    volt_C = v_2       #lo que medimos con el voltimetro -- anodo
    
    voltajes_m1.append(volt_C)
    voltajes_m2.append(volt_B)
    
    
    I = volt_B / R4
    corrientes.append(I)

#%%

plt.plot(np.array(corrientes), np.array(offsets), '.-', color='b', label='Bajada')
plt.plot(corrientes, voltajes_m1, 'o')
plt.legend()
plt.grid()
plt.savefig(f"plots/d{numeromed}_{distancia:.1f}_cm_aire_{presion_fija:.1f}e-1mbar.png")
plt.close()

#%%
# ==========================================================
# GUARDAR DATOS EN CSV
# ==========================================================

df = pd.DataFrame({
    'Tiempo_s': tiempo,
    'Voltaje_plasma_V': voltajes_m1,   # volt_C
    'Voltaje_R_V': voltajes_m2,        # volt_B
    'Corriente_A': corrientes,
    'Voltaje_HV_estimado_V': offsets * factor  # opcional (HV real)
})

df.to_csv(f"datos/d{numeromed}_{distancia:.1f}_cm_aire_{presion_fija:.1f}e-1mbar_bajada.csv", index=False)

