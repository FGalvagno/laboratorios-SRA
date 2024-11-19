from scipy import signal
from scipy.signal import freqs
import numpy as np #Importa libreria numerica
import sympy as sym #simbolica
import matplotlib.pyplot as plt #importa matplotlib solo pyplot
sym.init_printing() #activa a jupyter para mostrar simbolicamente el output
# Parametros de Entrada
FS=5000*10
fp=[800, 1250] #Banda de Paso [Hz]
fs=[200, 5000];#Banda de Rechazo [Hz]
Wp=np.dot(2*np.pi,fp); #Banda de Paso [rad/s]
Ws=np.dot(2*np.pi,fs); #Banda de Rechazo [rad/s]
Ap=0.25; #Atenuacion maxima en Banda de Paso [dB]
As=30; #Atenuacion minima en Banda de Rechazo [dB]
N, Wn = signal.cheb1ord(Wp, Ws, Ap, As, analog=True)
b, a = signal.cheby1(N, Ap, Wn, btype="bandpass", analog=True)
w, h = signal.freqs(b, a)
Filtro=signal.TransferFunction(b,a) #Funcion de transferencia calculada
#Implementacion como PasaAlto/PasaBajo
sos = signal.cheby1(N, Ap, Wn, btype="bandpass", output="sos", analog=True)
PasaBajo=signal.TransferFunction(2*sos[0,:3],sos[0,3:])
PasaAlto=signal.TransferFunction(1/2*sos[1,:3],sos[1,3:])
plt.figure()
plt.semilogx(w, 20 * np.log10(abs(h)))
plt.title("Chebyshev I" )
plt.xlabel("Frecuencia [rad/seg]")
plt.ylabel('Amplitud [dB]')
plt.grid(which="both", axis="both")
plt.show()