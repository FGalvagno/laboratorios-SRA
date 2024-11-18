# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import pandas as pd
import plotly.express as px

# Colocar ruta del archivo generado en LTSpice
file_path = '[Ruta]/[Nombre_del_archivo].txt'
data = pd.read_csv(file_path, sep='\t')

# Plotear los datos
fig = px.line(data,
              x='vin', 
              y=['V(vo1)', 'V(vo2)'], 
              title='Gráfica de tension de salida en funcion de la entrada',
                labels={
                    'vin': 'Vi [V]',
                    'variable':'Salidas',
                    'V(vo1)': 'V2',
                    'V(vo2)':'Vo2'
                }
              )

# Cambiar los nombres manualmente
new_legend_names = {"V(vo1)": "Vo1", "V(vo2)": "Vo2"}

for trace in fig.data:
    trace.name = new_legend_names.get(trace.name, trace.name)

# Customizar el eje X e Y
fig.update_xaxes(tick0=0, dtick=1)
fig.update_yaxes(tick0=0, dtick=2, title='Tension [V]')

fig.show()
print(fig.data)