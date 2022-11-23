# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 23/11/2022 10:40 am
# Última modificación: 23/11/2022 12:20 md
# Versión: 3.10.8

# Importar librerías
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from funciones import *
from validaciones import *

# Fuentes
fuenteBotones = ("Helvetica", 10)
fuenteBotonesMenu = ("Helvetica", 12)
fuenteTitulo = ("Helvetica", 20)

# Ventanas / Bloqueos botones
# 1. Importar producto
"""No se necesita"""

# 2. Crear usuarios
def generarUsuariosVent(ventanaMain, pUsuarios):
    """
    Funcionalidad: ser la ventana que permite generar usuarios
    Entrada: ventanaMain (CTK)
    pUsuarios (list)
    Salida: genera usuarios / mensaje retroalimentación
    """
    genUsuariosVent = ctk.CTkToplevel(ventanaMain)
    genUsuariosVent.geometry("400x200")
    genUsuariosVent.title("Generar usuarios")
    titulo = ctk.CTkLabel(genUsuariosVent, text="Generar usuarios", 
    text_font=fuenteTitulo)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(genUsuariosVent, 
    text="Ingrese la cantidad de usuarios a generar: ",
    text_font=fuenteBotones)
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    cantEntry = ctk.CTkEntry(master=genUsuariosVent,
                               placeholder_text="Ej: 100",
                               width=125,
                               height=35,
                               border_width=2,
                               corner_radius=10)
    cantEntry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    botonCrear = ctk.CTkButton(master=genUsuariosVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Extraer",
                                 command=lambda: crearUsuariosAux(cantEntry.get(), pUsuarios))
    botonCrear.place(relx=0.30, rely=0.75, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=genUsuariosVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Regresar",
                                 command=lambda: genUsuariosVent.destroy()) # Sale de la ventana
    botonSalir.place(relx=0.7, rely=0.75, anchor=tk.CENTER)

def bloqueoGenerarUsuarios(ventanaMain, pUsuarios, pProductos):
    """
    Funcionalidad: bloqueo botón 2 si no se han importado los productos
    Entrada: ventanaMain (CTK) 
    pUsuarios (list)
    pProductos (dict)
    Salida: generarUsuariosVent(ventanaMain, pUsuarios)
    """
    if len(pProductos) == 0:
        return messagebox.showerror("Productos vacíos", "No se han importado los productos.")
    return generarUsuariosVent(ventanaMain, pUsuarios)

# 3. Generar compras
def bloqueoGenerarCompras(pUsuarios, pDiccProductos, pCompras):
    """
    Funcionalidad: bloqueo botón 3 si no se han importado los usuarios
    Entrada: ventanaMain (CTK) 
    pUsuarios (list)
    pCompras (list)
    Salida: generarUsuariosVent(ventanaMain, pUsuarios)
    """
    if len(pUsuarios) == 0:
        return messagebox.showerror("Usuarios vacíos", "No se han generado los usuarios.")
    messagebox.showinfo("Compras generadas", "Las compras han sido generados.")
    return crearCompras(pUsuarios, pDiccProductos, pCompras)

# 4. Generar tracking

# 5. Reportes
# Hacer la misma lógica anterior

# Ventana menú
def menuVentana():
    """
    Funcionalidad: despliega la ventana con el menú principal
    Entrada: N/A
    Salida: retorna la función de acuerdo a la opción presionada
            por el botón
    """
    app = ctk.CTk()
    app.geometry(f"{515}x{400}")
    app.title("AeroTEC")
    productos = {"OF-1234":["Secadora", (1000.12, 54.32)], "OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-5321":["Bola", (153.12, 7.432)], "OF-4312":["Camisa", (573.12, 12.43)], 
"OF-5343":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)],
"OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)]} # Variables a usar
    usuarios = []
    compras = []
    tracking = []
    titulo = tk.StringVar(value="¡Bienvenido a AeroTEC!")
    tituloLabel = ctk.CTkLabel(master=app,
                               textvariable=titulo,
                               text_color="white",
                               text_font=("Helvetica",35))
    tituloLabel.grid(row = 0, column = 0, columnspan=2)
    subTitulo = tk.StringVar(value="Seleccione una de las opciones")
    subTituloLabel = ctk.CTkLabel(master=app,
                               textvariable=subTitulo,
                               text_color="white",
                               text_font=("Helvetica", 15))
    subTituloLabel.grid(row = 1, column = 0, columnspan=2)
    espacioLabel = tk.StringVar(value="------------------------------------")
    espacioLabel = ctk.CTkLabel(master=app,
                                    textvariable=espacioLabel,
                                    text_font=("Helvetica", 30))    
    espacioLabel.grid(row = 2, column = 0, columnspan=2)
    boton1 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="1. Importar producto",
                                 command=lambda: print(1))
    boton1.grid(row = 3, column = 0, padx=5, pady=5, ipadx=15, ipady=10)
    boton2 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="2. Generar usuarios",
                                 command=lambda: bloqueoGenerarUsuarios(app, usuarios, productos))
    boton2.grid(row =3, column = 1, padx=5, pady=5, ipadx=15, ipady=10)
    boton3 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="3. Generar compras",
                                 command=lambda: bloqueoGenerarCompras(usuarios, productos, compras))
    boton3.grid(row = 4, column = 0, padx=5, pady=5, ipadx=15, ipady=10)
    boton4 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="4. Tracking",
                                 command=lambda: print(4))
    boton4.grid(row = 4, column=1, padx=5, pady=5, ipadx=15, ipady=10)
    boton5 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="5. Reportes",
                                 command=lambda: print(5))
    boton5.grid(row = 5, column=0, padx=5, pady=5, ipadx=15, ipady=15)
    boton6 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="6. Salir",
                                 command=lambda: app.destroy())
    boton6.grid(row = 5, column=1, padx=5, pady=5, ipadx=15, ipady=15)
    app.mainloop()

menuVentana()