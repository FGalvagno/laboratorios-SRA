import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from scipy import signal

# Variables
Ado = 100  # dB
f1 = 10  # Hz
f2 = 5.06e6  # Hz

w1 = 2 * np.pi * f1
w2 = 2 * np.pi * f2

num = 10 ** (Ado / 20)
den = [1 / (w1*w2), 1/w1 + 1/w2, 1]

# Crear sistema
Av = signal.TransferFunction(num, den)
print(Av)

# Bode
w = np.logspace(-1, 10, 1000)
w_v, mag_v, phase_v = signal.bode(Av, w)
f_v = w_v / (2 * np.pi)

# Crear gráfico
fig = go.Figure()
# Magnitud
fig.add_trace(go.Scatter(
    x=f_v,
    y=mag_v,
    mode='lines',
    name='Magnitud [dB]',
    line=dict(color='blue')
))
# Fase
fig.add_trace(go.Scatter(
    x=f_v,
    y=phase_v,
    mode='lines',
    name='Fase [°]',
    yaxis='y2',
    line=dict(color='red')
))
# Configurar los ejes
fig.update_layout(
    title="Bode Plot",
    xaxis=dict(
        title="Frecuencia [Hz]",
        type="log",
    ),
    yaxis=dict(
        title="Magnitud [dB]",
        side="left"
    ),
    yaxis2=dict(
        title="Fase [°]",
        overlaying="y",
        side="right"
    ),
    legend=dict(x=0.75, y=0.95),
    template="plotly_white"
)
fig.show()


# # Plot Magnitude
# fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
# ax1.semilogx(w_v/(2*np.pi), mag_v)
# ax1.set_ylabel("Magnitud [dB]")
# ax1.grid(which="both", linestyle="--", linewidth=0.5)

# ax2.semilogx(w_v/(2*np.pi), phase_v)
# ax2.set_xlabel("Frecuencia [Hz]")
# ax2.set_ylabel("Fase [°]")
# ax2.grid(which="both", linestyle="--", linewidth=0.5)

# plt.show()