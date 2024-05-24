import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Scrollable Frame con Tablas")

# Creamos un frame principal con scroll horizontal
frame = ttk.Frame(root)
frame.pack(fill='both', expand=True)

canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill='both', expand=True)

scrollbar = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar.pack(side=tk.BOTTOM, fill='x')

canvas.configure(xscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Creamos un frame interior para colocar las tablas
interior = ttk.Frame(canvas)
canvas.create_window((0, 0), window=interior, anchor='nw')

# Creamos 11 tablas y las colocamos horizontalmente en el frame interior
for i in range(11):
    table = ttk.Treeview(interior, columns=('x', 'y'), show='headings')
    table.heading('x', text='X')
    table.heading('y', text='Y')
    table.insert('', 'end', values=(f'Valor X{i}', f'Valor Y{i}'))
    table.pack(side=tk.LEFT)

# Configuramos el scroll horizontal
interior.update_idletasks()
canvas.configure(scrollregion=frame.bbox("all"))

root.mainloop()