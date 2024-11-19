import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from pathlib import Path

def update_transfer_text(text):
    transfer_textbox.config(state=tk.NORMAL)
    transfer_textbox.delete("1.0", tk.END)
    transfer_textbox.insert(tk.END, text)
    transfer_textbox.config(state=tk.DISABLED)

def format_transfer_function(tf):
    num, den = tf.num, tf.den
    num_str = " + ".join(f"{coef:.3e} s^{i}" for i, coef in enumerate(num[::-1]))
    den_str = " + ".join(f"{coef:.3e} s^{i}" for i, coef in enumerate(den[::-1]))
    return f"Numerador:\n{num_str}\nDenominador:\n{den_str}\n"

def update_filter():
    try:
        FS = float(fs_entry.get()) * 10
        fp = list(map(float, fp_entry.get().split(',')))  # Banda de Paso [Hz]
        fs = list(map(float, stopband_entry.get().split(',')))  # Banda de Rechazo [Hz]

        Wp = np.array(fp) * 2 * np.pi  # Banda de Paso [Hz] [rad/s]
        Ws = np.array(fs) * 2 * np.pi  # Banda de Rechazo [rad/s]
        Ap = 0.25  # Max at. en banda de paso [dB]
        As = 30  # Min at. en banda de rechazo [dB]

        # Diseño del filtro Chebyshev
        N, Wn = signal.cheb1ord(Wp, Ws, Ap, As, analog=True)
        b, a = signal.cheby1(N, Ap, Wn, btype='bandpass', analog=True)
        w, h = signal.freqs(b, a)

        Filtro = signal.TransferFunction(b, a)  # Función de transferencia
        sos = signal.cheby1(N, Ap, Wn, btype='bandpass', output='sos', analog=True)
        PasaBajo = signal.TransferFunction(2 * sos[0, :3], sos[0, 3:])
        PasaAlto = signal.TransferFunction(1 / 2 * sos[1, :3], sos[1, 3:])

        # Actualizar Funciones de Transferencia en Tkinter
        update_transfer_text(f"Filtro:\n{format_transfer_function(Filtro)}\n\nPasaBajo:\n{format_transfer_function(PasaBajo)}\n\nPasaAlto:\n{format_transfer_function(PasaAlto)}")

        # Graficar Diagrama de Bode
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6), facecolor='white')
        
        # Magnitud
        ax1.semilogx(w, 20 * np.log10(abs(h)), color='#2F6165')
        ax1.set_title('Diagrama de Bode del Filtro Chebyshev I')
        ax1.set_ylabel('Magnitud [dB]')
        ax1.grid(which='both', axis='both')
        
        # Fase
        angles = np.unwrap(np.angle(h))
        angles_deg = np.degrees(angles)
        ax2.semilogx(w, angles_deg, color='#2F6165')
        ax2.set_xlabel('Frecuencia [rad/s]')
        ax2.set_ylabel('Fase [grados]')
        ax2.grid(which='both', axis='both')

        # Embed plot in Tkinter
        for widget in plot_frame.winfo_children():
            widget.destroy()
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()

        # Create and pack the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas, plot_frame)
        toolbar.update()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    except Exception as e:
        print(e)

# Handle window close event
def on_closing():
    plt.close('all')  # Close all matplotlib plots
    root.destroy()  # Destroy Tkinter window

# Crear ventana Tkinter
root = tk.Tk()
root.title("Filtro Pasa Banda Chebyshev")
#root.geometry("1280x720")
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

# Bind window close event to on_closing function
root.protocol("WM_DELETE_WINDOW", on_closing)

# Marco de Entrada
input_frame = ttk.Frame(root, padding="10")
input_frame.pack(side=tk.TOP, fill=tk.X)

ttk.Label(input_frame, text="Frecuencia de muestreo (FS):").grid(row=0, column=0, padx=5, pady=5)
fs_entry = ttk.Entry(input_frame, width=20)
fs_entry.insert(0, "5000")  # Valor por defecto
fs_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Banda de paso (fp, ej., 800,1250):").grid(row=1, column=0, padx=5, pady=5)
fp_entry = ttk.Entry(input_frame, width=20)
fp_entry.insert(0, "800,1250")  # Valor por defecto
fp_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(input_frame, text="Banda de detención (fs, ej., 200,5000):").grid(row=2, column=0, padx=5, pady=5)
stopband_entry = ttk.Entry(input_frame, width=20)
stopband_entry.insert(0, "200,5000")  # Valor por defecto
stopband_entry.grid(row=2, column=1, padx=5, pady=5)

update_button = ttk.Button(input_frame, text="Actualizar Filtro", command=update_filter)
update_button.grid(row=2, column=3, columnspan=2, pady=10)

# Logo
image = Image.open(Path(__file__).with_name('logo.png'))
photo = ImageTk.PhotoImage(image)

ttk.Label(input_frame, image = photo).grid(row=0, column=5, columnspan=3, rowspan=3,
           sticky='W', padx=5, pady=5)

# Marco de Gráfica
plot_frame = ttk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True)

# Marco de Función de Transferencia
transfer_frame = ttk.Frame(root, padding="10")
transfer_frame.pack(side=tk.BOTTOM, fill=tk.X)

scrollbar = tk.Scrollbar(transfer_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

transfer_textbox = tk.Text(transfer_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
transfer_textbox.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=transfer_textbox.yview)

# Inicializar Gráfica
update_filter()

root.mainloop()
