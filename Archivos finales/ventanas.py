# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 23/11/2022 10:40 am
# Última modificación: 23/11/2022 11:35 am
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

# Ventanas
# 1. Importar producto 
# 2. Crear usuarios
# 3. Generar compras
# 4. Generar tracking
# 5. Reportes

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
                                 command=lambda: print(2))
    boton2.grid(row =3, column = 1, padx=5, pady=5, ipadx=15, ipady=10)
    boton3 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="3. Generar compras",
                                 command=lambda: print(3))
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
    boton5.grid(row = 5, column=0, padx=5, pady=5, ipadx=15, ipady=15, columnspan=2)
    boton6 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="Salir",
                                 command=lambda: app.destroy())
    boton6.grid(row = 6, column=0, padx=5, pady=5, ipadx=15, ipady=15, columnspan=2)
    app.mainloop()

menuVentana()