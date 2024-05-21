import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.scrolledtext import ScrolledText
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#########################################################################################
# SETTINGS #
#########################################################################################

# Crear una figura de Matplotlib
fig1, ax1 = plt.subplots()
ax1.plot([0, 1, 2, 3], [10, 20, 25, 30])  # Ejemplo de gráfico de líneas

# Crear la ventana principal de Tkinter
root = tk.Tk()
# Configurar el título de la ventana
root.title("Ventana Redimensionable")

# Definir el tamaño inicial de la ventana (ancho x alto)
root.geometry("800x600")

# Permitir que la ventana se pueda redimensionar
root.resizable(True, True)  # True para permitir redimensionar tanto en ancho como en alto

# Establecer el tamaño mínimo de la ventana
root.minsize(400, 300)

# Cambiar el color de fondo de la ventana
root.configure(bg="#f0f0f0")

# Añadir un manejador de eventos para la acción de cierre de la ventana
def on_closing():
    exit()

root.protocol("WM_DELETE_WINDOW", on_closing)

#########################################################################################

#########################################################################################
# DESIGN #
#########################################################################################

#Variables
ruta_imagen = "images/nist.png"
#Functions
def cambiar_pagina(pagina):
    notebook.select(pagina)

def abrir_archivo():
    # Abrir el navegador de archivos
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])

    #Limpiar listas
    valores_x = []
    valores_y = []
    # Verificar si se seleccionó un archivo
    if archivo:
        # Leer el contenido del archivo
        with open(archivo, "r") as file:
            # Procesar cada línea del archivo
            for linea in file:
                # Separar los datos x e y por coma
                x, y = linea.strip().split(",")
                # Agregar los datos a las listas
                valores_x.append(int(x))
                valores_y.append(int(y))

    crear_tabla(valores_x, valores_y)

def limpiar_tabla():
    # Eliminar todos los widgets dentro del frame, empezando desde la fila 1
    for widget in frame.winfo_children():
        if int(widget.grid_info()["row"]) > 0:  # Verificar si el widget está en una fila > 0
            widget.destroy()
    actualizar_graficas([], [])

def crear_tabla(valores_x, valores_y):
    # Configurar las columnas
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    # Agregar etiquetas al frame
    for number in range(len(valores_x)):
        l = tk.Label(frame, text=valores_x[number])
        l.grid(row=number+1, column=0, sticky='w')  # Alineado hacia la izquierda
        l = tk.Label(frame, text=valores_y[number])
        l.grid(row=number+1, column=1, sticky='w')  # Alineado hacia la izquierda
    
    actualizar_graficas(valores_x, valores_y)

def actualizar_graficas(valores_x, valores_y):
    # Actualizar datos de las gráficas
    ax1.clear()
    ax1.bar(valores_x, valores_y)
    ax1.set_title("Sales by Product")
    ax1.set_xlabel("Product")
    ax1.set_ylabel("Sales")

    ax2.clear()
    ax2.barh(valores_x, valores_y)
    ax2.set_title("Inventory by Product")
    ax2.set_xlabel("Inventory")
    ax2.set_ylabel("Product")

    ax3.clear()
    ax3.fill_between(valores_x, valores_y)
    ax3.set_title("Inventory by Month")
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Inventory")

    ax4.clear()
    ax4.plot(valores_x, valores_y)
    ax4.set_title("Sales by Year")
    ax4.set_xlabel("Year")
    ax4.set_ylabel("Sales")

    # Redibujar los widgets de lienzo
    canvas1.draw()
    canvas2.draw()
    canvas3.draw()
    canvas4.draw()

    print(valores_x)
    print(valores_y)


frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Configurar la primera columna para que ocupe dos tercios del espacio
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
# Configurar la segunda columna para que ocupe un tercio del espacio
frame.columnconfigure(1, weight=4)

# Crear el primer frame hijo (izquierda)
bar_frame = tk.Frame(frame, bg="red")
bar_frame.grid(row=0, column=0, sticky="nsew")

# Crear el segundo frame hijo (derecha)
frame_derecha = tk.Frame(frame, bg="blue")
frame_derecha.grid(row=0, column=1, sticky="nsew")

# Crear el botón Home
boton_Home = tk.Button(bar_frame, text="Inicio", command=lambda: cambiar_pagina(pagina1))
boton_Home.pack(fill="both", expand=True)
# Crear el botón Input
boton_Input = tk.Button(bar_frame, text="Datos Historicos", command=lambda: cambiar_pagina(pagina2))
boton_Input.pack(fill="both", expand=True)
# Crear el botón Predictions
boton_Predictions = tk.Button(bar_frame, text="Predicciones", command=lambda: cambiar_pagina(pagina3))
boton_Predictions.pack(fill="both", expand=True)
# Crear el botón Import
boton_import = tk.Button(bar_frame, text="Importar", command=lambda: cambiar_pagina(pagina4))
boton_import.pack(fill="both", expand=True)
# Crear el botón eXIT
boton_Exit = tk.Button(bar_frame, text="Salir", background="red", command=on_closing)
boton_Exit.pack(fill="both", expand=True)


# Crear un notebook para contener los 4 paneles
paneles_frame = tk.Frame(frame_derecha)
paneles_frame.pack(fill="both", expand=True)
# Crear control de pestañas (notebook)
notebook = ttk.Notebook(paneles_frame)

# Crear las páginas del dashboard
pagina1 = tk.Frame(notebook, bg="white")
pagina2 = tk.Frame(notebook, bg="white")
pagina3 = tk.Frame(notebook, bg="white")
pagina4 = tk.Frame(notebook, bg="white")

# Añadir las páginas al notebook
notebook.add(pagina1)
notebook.add(pagina2)
notebook.add(pagina3)
notebook.add(pagina4)

notebook.pack(fill="both", expand=True)

# HOME DESIGN ############################################################################
# INPUT DESIGN ###########################################################################

# Crear el frame padre
frame_padre = tk.Frame(pagina2)
frame_padre.pack(fill="both", expand=True)

# Configurar la primera fila y columna para que se expandan en igual proporción
frame_padre.columnconfigure(0, weight=1)
frame_padre.rowconfigure(0, weight=5)
frame_padre.rowconfigure(1, weight=1)


# Crear el primer frame hijo (izquierda)

frame_izquierda = tk.Frame(frame_padre)
frame_izquierda.grid(row=0, column=0, sticky="nsew")  # Se expande en todas las direcciones
text = ScrolledText(frame_izquierda, state='disable', width=0)  # Ancho ajustado
text.pack(padx=20, pady=20, fill="both", expand=True, anchor="w")  # Alineado hacia la izquierda

frame = tk.Frame(text) # Crear un frame dentro de la ScrolledText
text.window_create('1.0', window=frame)
# Títulos de las columnas
titulo_columna_1 = tk.Label(frame, text="Año", highlightthickness=2, highlightbackground="black")
titulo_columna_1.grid(row=0, column=0, sticky='w')
titulo_columna_2 = tk.Label(frame, text="Valor", highlightthickness=2, highlightbackground="black")
titulo_columna_2.grid(row=0, column=1, sticky='w')
#
# Crear el segundo frame hijo (derecha)

frame_derecha = tk.Frame(frame_padre, bg="blue")
frame_derecha.grid(row=1, column=0, sticky="nsew")  # Se expande en todas las direcciones

# Crear un botón para abrir el navegador de archivos
boton_abrir = tk.Button(frame_derecha, text="Abrir Archivo", command=abrir_archivo)
boton_abrir.pack(fill="both", expand=True)

button2 = tk.Button(frame_derecha, text="Reiniciar", command=limpiar_tabla)
button2.pack(fill="both", expand=True)

# PREDICTIONS DESIGN ########################################################################
# Crear notebook
notebookGraphs = ttk.Notebook(pagina3)
# Crear las páginas del dashboard
pagina1G = tk.Frame(notebookGraphs, bg="white")
pagina2G = tk.Frame(notebookGraphs, bg="white")
pagina3G = tk.Frame(notebookGraphs, bg="white")
pagina4G = tk.Frame(notebookGraphs, bg="white")

notebookGraphs.add(pagina1G, text="G1")
notebookGraphs.add(pagina2G, text="G2")
notebookGraphs.add(pagina3G, text="G3")
notebookGraphs.add(pagina4G, text="G4")

notebookGraphs.pack(fill="both", expand=True)

# Crear los subplots
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()
# Crear los widgets de lienzo
canvas1 = FigureCanvasTkAgg(fig1, master=pagina1G)
canvas1.get_tk_widget().pack(side="left", fill="both", expand=True)
canvas2 = FigureCanvasTkAgg(fig2, master=pagina2G)
canvas2.get_tk_widget().pack(side="left", fill="both", expand=True)
canvas3 = FigureCanvasTkAgg(fig3, master=pagina3G)
canvas3.get_tk_widget().pack(side="left", fill="both", expand=True)
canvas4 = FigureCanvasTkAgg(fig4, master=pagina4G)
canvas4.get_tk_widget().pack(side="left", fill="both", expand=True)

# IMPORT DESIGN ##############################################################################


# PROGRAM BUCLE ##############################################################################
# Iniciar el bucle principal de Tkinter
root.mainloop()
