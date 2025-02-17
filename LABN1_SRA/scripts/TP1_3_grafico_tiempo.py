# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import pandas as pd
import plotly.express as px

# Colocar ruta del archivo generado en LTSpice
file_path = 'LABN1_SRA/LTSpice_data/TP1_3_Vo1_Vo2_Vin_vs_t.txt'
data = pd.read_csv(file_path, sep='\t')

# Plotear los datos
fig = px.line(data,
              x='time', 
              y=['V(vin)', 'V(vo1)', 'V(vo2)'], 
              title='Gráfico en funcion del tiempo',
                labels={
                    'time': 'Tiempo [s]',
                    'variable':'Señales',
                    'V(vin)': 'V1',
                    'V(vo1)': 'V2',
                    'V(vo2)':'Vo2'
                }
              )

# Cambiar los nombres manualmente
new_legend_names = {"V(vin)": "Vin", "V(vo1)": "Vo1", "V(vo2)": "Vo2"}

for trace in fig.data:
    trace.name = new_legend_names.get(trace.name, trace.name)
    
# Personalizar el color y grosor de la línea para el trazo de 'Vin'
fig.update_traces(selector=dict(name='Vin'), line=dict(color='black', width=0.7, dash='dash'))

# Customizar el eje X e Y
# fig.update_xaxes(tick0=0, dtick=1)
fig.update_yaxes(tick0=0, dtick=2, title='Tension [V]')

fig.show()
print(fig.data)