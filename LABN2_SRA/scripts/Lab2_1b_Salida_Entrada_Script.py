# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import pandas as pd
import plotly.express as px

# Colocar ruta del archivo generado en LTSpice
file_path = 'C:/Users/Usuario/GASTON/Z Sintesis de Redes Activas/Ejercicios (Vs Code)/.venv(enviroment)/Lab2_1b_Salida_Entrada.txt'
data = pd.read_csv(file_path, sep='\t')

# Plotear los datos
fig = px.line(data,
              x='v9', 
              y='V(vo8)', 
              title='Gráfico en funcion de la tensión de entrada',
                labels={
                    'v9': 'Tensión [V]',
                    'variable':'Señales',
                    'V(vo8)': 'vout',
                }
              )

# Cambiar los nombres manualmente
new_legend_names = {"V(vo8)": "Vout"}

for trace in fig.data:
    trace.name = new_legend_names.get(trace.name, trace.name)

# Customizar el eje Y
fig.update_yaxes(tick0=0, dtick=2, title='Tension [V]')

fig.show()