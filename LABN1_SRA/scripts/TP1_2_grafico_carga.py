# -------------------------------------------------------------
# Script para guardar datos de LTSpice en .PNG
# -------------------------------------------------------------

import matplotlib.pyplot as plt

# Variables para almacenar los datos
steps = {}
current_step = None

# Configurar que datos se quieren ver:
# 'IL': Corriente en la carga en funcion de RL
# 'Vo': Tension de salida en funcion de RL
class Config:
    Y_VAR = 'Vo'

# Leer el archivo
if Config.Y_VAR == 'IL':
    
    # Colocar ruta del archivo generado en LTSpice
    with open("LABN1_SRA/LTSpice_data/TP1_2_i_vs_Vin_RL.txt", "r") as file:
        lines = file.readlines()
        
    # Procesar las líneas del archivo
    for line in lines:
        line = line.strip()
        if line.startswith("Step Information:"):
            # Extraer la información del paso
            step_info = line.split(":")[1].strip()
            current_step = step_info
            steps[current_step] = {"vin": [], "I(Rl)": []}
        elif line and current_step:
            # Leer los valores numéricos
            try:
                vin, current = map(float, line.split())
                steps[current_step]["vin"].append(vin)
                steps[current_step]["I(Rl)"].append(current)
            except ValueError:
                pass

    # Graficar cada paso
    plt.figure(figsize=(10, 6))

    for step, data in steps.items():
        plt.plot(data["vin"], data["I(Rl)"], label=step)
        
    # Personalizar el gráfico
    plt.title("Corriente en funcion de RL y Vin")
    plt.xlabel("Vin [V]")
    plt.ylabel("IL [A]")
        
elif Config.Y_VAR == 'Vo':
    
    # Colocar ruta del archivo generado en LTSpice
    with open("LABN1_SRA/LTSpice_data/TP1_2_Vo_vs_Vin_RL.txt", "r") as file:
        lines = file.readlines()
        
    # Procesar las líneas del archivo
    for line in lines:
        line = line.strip()
        if line.startswith("Step Information:"):
            # Extraer la información del paso
            step_info = line.split(":")[1].strip()
            current_step = step_info
            steps[current_step] = {"vin": [], "V(vo)": []}
        elif line and current_step:
            # Leer los valores numéricos
            try:
                vin, current = map(float, line.split())
                steps[current_step]["vin"].append(vin)
                steps[current_step]["V(vo)"].append(current)
            except ValueError:
                pass

    # Graficar cada paso
    plt.figure(figsize=(10, 6))

    for step, data in steps.items():
        plt.plot(data["vin"], data["V(vo)"], label=step)
        
    # Personalizar el gráfico
    plt.title("Tension de salida en funcion de RL y Vin")
    plt.xlabel("Vin [V]")
    plt.ylabel("Vo [V]")

plt.legend(title="Steps")
plt.grid(True)
plt.show()
