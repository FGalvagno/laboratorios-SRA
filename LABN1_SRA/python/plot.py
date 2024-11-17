import pandas as pd
import plotly.express as px

# Load data from the file
file_path = './LABN1_SRA/LTSpice_data/TP1_Vo1_vs_V1.txt'
data = pd.read_csv(file_path, sep='\t')

# Plot the data
fig = px.line(data, x='v1', y='V(vo1)', title='Plot of V(vo1) vs v1', labels={'v1': 'v1', 'V(vo1)': 'V(vo1)'})
fig.show()