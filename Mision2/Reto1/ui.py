# ui.py
# Capa de interfaz gráfica (Tkinter)

# Usar archivos y cajas de mensajes y se le puede dar un alias 
import tkinter as tk
from tkinter import filedialog as flg, messagebox as msgb
from controller import procesar_instruccion


def iniciar_app():
    
    # Ventana principal
    root = tk.Tk()
    root.title("Procesador Excel con IA")
    root.geometry("500x300")

    # Etiqueta
    tk.Label(root, text = "Escriba una instrucción en lenguaje natural").pack(pady = 10)


    # Funcion para buscar y seleccionar el archivo de excel
    def seleccionar_excel():
        pash =  flg.askopenfilename(
        title = "Seleccionar archivo Excel",
        filetypes = [("Archivo Excel", "*.xlsx")]
        )

    # Funcion para devolvernos la ruta del archivo
    
        if pash:
            # msgb.showinfo("Resultado", pash)
            pash_Label.config(text = pash)

    boton = tk.Button(
        root,
        text = "Seleccionar Archiv de Excel",
        command = seleccionar_excel, 
        width = 30,
        height = 2
    )

    # Etiqueta
    pash_Label = tk.Label(root, text = "Sin Archivo",
                          width = 30,
                          height = 2
                          ).pack(pady = 10)
    boton.pack(pady = 15)

    # Campo de texto
    entrada = tk.Entry(root, width = 60)
    entrada.pack(pady = 5)
    
    # Campo de ruta
    ruta = tk.Entry(root, width = 60)
    ruta.pack(pady = 5)

    # Lo que el usuario va a ver

    # Funcion para
    def seleccionar_excel():
        return flg.askopenfilename(
        title = "Seleccionar archivo Excel",
        filetypes = [("Archivo Excel", "*.xlsx")]
        )                

    # Acción del botón
    def ejecutar():         
        pash = pash_Label.cget("text")
        texto = entrada.get()
        msgb.showinfo("Resultado", pash)
        exito, mensaje = procesar_instruccion(texto,pash)

        if exito:
            msgb.showinfo("Resultado", mensaje)
        else:
            msgb.showerror("Error", mensaje)
    
    def on_click():
        archivo = seleccionar_excel()
        ruta.insert(0, archivo)

    # Botón
    tk.Button(root, text="Ejecutar instrucción", command = ejecutar).pack(pady = 20)
    
    boton = tk.Button(
        root,
        text = "Seleccionar Archiv de Excel",
        command = on_click, 
        width = 30,
        height = 2
    )
    
    boton.pack(pady = 60)
    root.mainloop()