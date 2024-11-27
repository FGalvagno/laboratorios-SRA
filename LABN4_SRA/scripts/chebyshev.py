from scipy import signal
import numpy as np #Importa libreria numerica
import matplotlib.pyplot as plt #importa matplotlib solo pyplot
import plotly.express as px

# sym.init_printing() #activa a jupyter para mostrar simbolicamente el output

# Parametros de Entrada
fp=[800, 1250] #Banda de Paso [Hz]
fs=[200, 5000];#Banda de Rechazo [Hz]

# dot(a,b): Producto punto entre a y b.
Wp=np.dot(2*np.pi,fp); #Banda de Paso [rad/s]
Ws=np.dot(2*np.pi,fs); #Banda de Rechazo [rad/s]

Ap=0.25; #Atenuacion maxima en Banda de Paso [dB]
As=30; #Atenuacion minima en Banda de Rechazo [dB]

# cheb1ord(): Seleccion del orden del filtro Chebyshev tipo I
# 
# Devuelve el menor orden que puede tener el filtro para que cumpla la
# especificacion de la Atenuacion maxima en Banda de Paso en dB y de la
# Atenuacion minima en Banda de Rechazo en dB.
# 
# Return: 
# N (int): el orden mas bajo que puede tener el filtro
# Wn (ndarray o float): la frecuencia de corte (-3dB) para usar en cheby1().
N, Wn = signal.cheb1ord(Wp, Ws, Ap, As, analog=True)

# cheby1(): Diseño del filtro de Chebyshev tipo I
# 
# Devuelve los coeficientes del filtro
# 
# Return:
# N (int): el orden del filtro
# rp (float): la maxima atenuacion que puede tener en la banda de paso
# Wn (array): la frecuencia de corte (-3dB)
# btype: el tipo de filtro
# output: puede ser 'ba' (num/den), 'zpk' (polo-cero) o 'sos' (second-order
#         sections)
# analog (bool): si esta en True, devuelve un filtro analogico, sino
#                uno digital
b, a = signal.cheby1(N, Ap, Wn, btype="bandpass", output="ba", analog=True)

# freqs(b,a): Respuesta en frecuencia segun el numerador 'b' y el
#             denominador 'a'
# Return:
# w (ndarray): frecuencias en las que la respuesta fue calculada
# h (ndarray): la respuesta en frecuencia
w, h = signal.freqs(b, a, worN = 20000)

# Funcion de transferencia calculada
Filtro=signal.TransferFunction(b,a)

# Implementacion como PasaAlto/PasaBajo
sos = signal.cheby1(N, Ap, Wn, btype="bandpass", output="sos", analog=True)
PasaBajo=signal.TransferFunction(2*sos[0,:3],sos[0,3:])
PasaAlto=signal.TransferFunction(1/2*sos[1,:3],sos[1,3:])

# Crear un rango de frecuencias (logarítmico)
f_v = np.logspace(np.log10(100), np.log10(10000), 10000)  # 5000 puntos entre 200 y 5000 rad/s

# Calcular la respuesta en frecuencia
w_F, h_F = signal.freqresp(Filtro, w=2 * np.pi * f_v)
w_PB, h_PB = signal.freqresp(PasaBajo, w=2 * np.pi * f_v)
w_PA, h_PA = signal.freqresp(PasaAlto, w=2 * np.pi * f_v)

# Graficar
plt.figure()
plt.semilogx(w_F/(2*np.pi), 20*np.log10(abs(h_F)), label = "Filtro", color = 'b', linewidth = 1.4)
plt.semilogx(w_PB/(2*np.pi), 20*np.log10(abs(h_PB)), label = "Pasa Bajo", color = 'red', linewidth = 0.5)
plt.semilogx(w_PA/(2*np.pi), 20*np.log10(abs(h_PA)), label = "Pasa Alto", color = 'orange', linewidth = 0.5)
plt.title("Chebyshev I" )
plt.xlabel("Frecuencia [Hz]")
plt.ylabel('Amplitud [dB]')
plt.grid(which="both", axis="both")
plt.show()