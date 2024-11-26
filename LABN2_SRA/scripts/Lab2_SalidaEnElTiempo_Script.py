# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import pandas as pd
import plotly.express as px

# Colocar ruta del archivo generado en LTSpice
file_path = 'C:/Users/Usuario/GASTON/Z Sintesis de Redes Activas/Ejercicios (Vs Code)/.venv(enviroment)/Lab2_SalidaEnElTiempo.txt'
data = pd.read_csv(file_path, sep='\t')

# Plotear los datos
fig = px.line(data,
              x='time', 
              y='V(vout)', 
              title='Gráfico en funcion del tiempo',
                labels={
                    'time': 'Tiempo [s]',
                    'variable':'Señales',
                    'V(vout)': 'vout',
                }
              )

# Cambiar los nombres manualmente
new_legend_names = {"V(vout)": "Vout"}

for trace in fig.data:
    trace.name = new_legend_names.get(trace.name, trace.name)

# Customizar el eje Y
fig.update_yaxes(tick0=0, dtick=2, title='Tension [V]')

fig.show()