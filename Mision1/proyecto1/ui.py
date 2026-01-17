# Lo que el usuario va a ver

# https://docs.python.org/es/3/library/tkinter.html

import tkinter as tk
# Usar archivos y cajas de mensajes y se le puede dar un alias 
from tkinter import filedialog as flg, messagebox as msgb
from proccessor import process_excel_safe

# Funcion para
def seleccionar_excel():
    return flg.askopenfilename(
    title= "Seleccionar archivo Excel",
    filetypes = [("Archivo Excel", "*.xlsx")]
    )

# Funcion para devolvernos la ruta del archivo
def on_clic_procesar():
    archivo = seleccionar_excel()
    exito,mensaje = process_excel_safe(archivo)
    if exito:
        msgb.showwinfo("Proceso Completado", mensaje)
    else:
        msgb.showerror("Error ", mensaje)

# Construcción de la Ventana Principal
def iniciar_app():
    root = tk.Tk()
    root.title("Procesador de Archivos Excel")
    root.geometry("400x400")
    root.resizable(False, False)
    
    boton = tk.Button(
        root,
        text = "Seleccionar Archiv de Excel",
        command = on_clic_procesar, 
        width = 30,
        height = 2
    )

    boton.pack(pady = 60)
    root.mainloop()