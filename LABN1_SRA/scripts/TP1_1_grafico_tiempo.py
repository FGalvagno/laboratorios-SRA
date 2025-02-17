# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import pandas as pd
import plotly.express as px

# Colocar ruta del archivo generado en LTSpice
file_path = 'LABN1_SRA/LTSpice_data/TP1_1_Vo2_V1_V2_vs_t.txt'
data = pd.read_csv(file_path, sep='\t')

# Plotear los datos
fig = px.line(data,
              x='time', 
              y=['V(v1)', 'V(v2)', 'V(vo2)'], 
              title='Gráfico en funcion del tiempo',
                labels={
                    'time': 'Tiempo [s]',
                    'variable':'Señales',
                    'V(v1)': 'V1',
                    'V(v2)': 'V2',
                    'V(vo2)':'Vo2'
                }
              )

# Cambiar los nombres manualmente
new_legend_names = {"V(v1)": "V1", "V(v2)": "V2", "V(vo2)": "Vo2"}

for trace in fig.data:
    trace.name = new_legend_names.get(trace.name, trace.name)

# Customizar el eje Y
fig.update_yaxes(tick0=0, dtick=2, title='Tension [V]')

fig.show()