# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import pandas as pd
import plotly.express as px

# Colocar ruta del archivo generado en LTSpice
file_path = 'LABN2_SRA/LTSpice_data/Lab2_Bode1.txt'
data = pd.read_csv(file_path, sep='\t', encoding='latin1')

# Separar magnitud (dB) y fase (°) de la columna 'V(vo1)'
data['Magnitude (dB)'] = data['V(vo1)'].str.extract(r'\(([-+e\d\.]+)dB')[0].astype(float)
data['Phase (deg)'] = data['V(vo1)'].str.extract(r',([-+e\d\.]+)°\)')[0].astype(float)

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

# Plotear la fase
fig_phase = px.line(data,
                    x='Freq.', 
                    y='Phase (deg)', 
                    title='Fase en función de la Frecuencia',
                    labels={
                        'Freq.': 'Frecuencia [Hz]',
                        'Phase (deg)': 'Fase [°]',
                    }
                   )
fig_phase.update_xaxes(type='log', title='Frecuencia [Hz]')
fig_phase.update_yaxes(title='Fase [°]')

# Mostrar las figuras
fig_mag.show()
fig_phase.show()
