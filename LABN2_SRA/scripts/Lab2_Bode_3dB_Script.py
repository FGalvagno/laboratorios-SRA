# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import pandas as pd
import plotly.express as px

# Colocar ruta del archivo generado en LTSpice
file_path = 'LABN2_SRA/LTSpice_data/Lab2_Bode_3dB.txt'
data = pd.read_csv(file_path, sep='\t', encoding='latin1')

# Separar magnitud (dB) 
data['Magnitude (dB)'] = data['V(vo1)/V(Vin1)'].str.extract(r'\(([-+e\d\.]+)dB')[0].astype(float)

# Plotear la amplitud
fig_mag = px.line(data,
                  x='Freq.', 
                  y='Magnitude (dB)', 
                  title='Magnitud en función de la Frecuencia',
                  labels={
                      'Freq.': 'Frecuencia [Hz]',
                      'Magnitude (dB)': 'Amplitud [dB]',
                  }
                 )

fig_mag.update_xaxes(type='log', title='Frecuencia [Hz]')
fig_mag.update_yaxes(title='Amplitud [dB]')

# Mostrar las figuras
fig_mag.show()
