# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import pandas as pd
import plotly.express as px

# Colocar ruta del archivo generado en LTSpice
file_path = 'LABN2_SRA/LTSpice_data/TP2_2_slew.txt'
data = pd.read_csv(file_path, sep='\t')

# Plotear los datos
fig = px.line(data,
              x='time', 
              y=['V(vin2)', 'V(vo2)'], 
              title='Gráfico en funcion del tiempo',
                labels={
                    'time': 'Tiempo [s]',
                    'variable':'Señales',
                    'V(vin2)': 'Vin',
                    'V(vo2)': 'Vout',
                }
              )

# Cambiar los nombres manualmente
new_legend_names = {'V(vin2)': 'Vin', 'V(vo2)': 'Vout'}

for trace in fig.data:
    trace.name = new_legend_names.get(trace.name, trace.name)

# Customizar el eje Y
fig.update_yaxes(tick0=0, dtick=1, title='Tension [V]')

fig.show()