# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import pandas as pd
import plotly.express as px

# Colocar ruta del archivo generado en LTSpice
file_path = 'LABN2_SRA/LTSpice_data/Lab2_1b_salida.txt'
data = pd.read_csv(file_path, sep='\t')

# Plotear los datos
fig = px.line(data,
              x='time', 
              y='V(vo8)', 
              title='Gráfico en funcion del tiempo',
                labels={
                    'time': 'Tiempo [s]',
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
