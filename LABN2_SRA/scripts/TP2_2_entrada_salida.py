# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import pandas as pd
import plotly.express as px

# Colocar ruta del archivo generado en LTSpice
file_path = 'LABN2_SRA/LTSpice_data/TP2_2_entrada_salida.txt'
data = pd.read_csv(file_path, sep='\t')

# Plotear los datos
fig = px.line(data,
              x='v9', 
              y=['V(n022)'], 
              title='Gráfica de tension de salida en funcion de la entrada',
                labels={
                    'v9': 'Vi [V]',
                    'V(n022)': 'V2'
                }
              )

# Cambiar los nombres manualmente
new_legend_names = {"V(n022)": "Vout"}

for trace in fig.data:
    trace.name = new_legend_names.get(trace.name, trace.name)

# Customizar el eje X e Y
fig.update_xaxes(tick0=0, dtick=0.5)
fig.update_yaxes(tick0=0, dtick=2, title='Tension [V]')

fig.show()
print(fig.data)