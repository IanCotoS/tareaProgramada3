# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 23/11/2022 10:40 am
# Última modificación: 23/11/2022 03:40 pm
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
    Entrada: pUsuarios (list)
    pDiccProductos (dict)
    pCompras (list)
    Salida: crearCompras(pUsuarios, pDiccProductos, pCompras) (act en list compras)
    """
    if len(pUsuarios) == 0:
        return messagebox.showerror("Usuarios vacíos", "No se han generado los usuarios.")
    return crearComprasAux(pUsuarios, pDiccProductos, pCompras)

# 4. Generar tracking
def bloqueoGenerarTracking(pCompras, pTracking,tipocambio):
    """
    Funcionalidad: bloqueo botón 3 si no se han importado las compras
    Entrada: pTracking (list)
    pCompras (list)
    Salida: 
    """
    if len(pCompras) == 0:
        return messagebox.showerror("Compras vacías", "No se han generado las compras.")
    messagebox.showinfo("Tracking generado", "El tracking ha sido generado.")
    return generarTracking(pCompras, pTracking,tipocambio)

# 5. Reportes
def reporteProdCasilleroVent(ventanaMain, pProductos, pCompras):
    """
    Funcionalidad: ser la ventana que permite los reportes de productos por casillero
    Entrada: ventanaMain (CTK)
    pProductos (dict)
    pCompras (compras)
    Salida: genera reporte productos por casillero / mensaje retroalimentación
    """
    reporteProdCasilleroVent = ctk.CTkToplevel(ventanaMain)
    reporteProdCasilleroVent.geometry("400x200")
    reporteProdCasilleroVent.title("Reporte productos casillero")
    titulo = ctk.CTkLabel(reporteProdCasilleroVent, text="Reporte productos casillero", 
    text_font=fuenteTitulo)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(reporteProdCasilleroVent, 
    text="Ingrese el número del casillero (mayor o igual que 10):",
    text_font=fuenteBotones)
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    cantEntry = ctk.CTkEntry(master=reporteProdCasilleroVent,
                               placeholder_text="Ej: 11",
                               width=125,
                               height=35,
                               border_width=2,
                               corner_radius=10)
    cantEntry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    botonCrear = ctk.CTkButton(master=reporteProdCasilleroVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Crear",
                                 command=lambda: reportesProductosAux(cantEntry.get(), pCompras, pProductos))
    botonCrear.place(relx=0.30, rely=0.75, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=reporteProdCasilleroVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Regresar",
                                 command=lambda: reporteProdCasilleroVent.destroy()) # Sale de la ventana
    botonSalir.place(relx=0.7, rely=0.75, anchor=tk.CENTER)

def reporteCompraVent(ventanaMain, pProductos, pTracking):
    """
    Funcionalidad: ser la ventana que permite los reportes de productos por casillero
    Entrada: ventanaMain (CTK)
    pProductos (dict)
    pCompras (compras)
    Salida: genera reporte productos por casillero / mensaje retroalimentación
    """
    reporteCompraVent = ctk.CTkToplevel(ventanaMain)
    reporteCompraVent.geometry("400x200")
    reporteCompraVent.title("Reporte por Compra")
    titulo = ctk.CTkLabel(reporteCompraVent, text="Reporte por Compra", 
    text_font=fuenteTitulo)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(reporteCompraVent, 
    text="Ingrese el número de Compra:",
    text_font=fuenteBotones)
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    cantEntry = ctk.CTkEntry(master=reporteCompraVent,
                               placeholder_text="Ej: 11",
                               width=125,
                               height=35,
                               border_width=2,
                               corner_radius=10)
    cantEntry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    botonCrear = ctk.CTkButton(master=reporteCompraVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Crear",
                                 command=lambda: reportesCompraAux(pTracking, cantEntry.get(), pProductos))
    botonCrear.place(relx=0.30, rely=0.75, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=reporteCompraVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Regresar",
                                 command=lambda: reporteCompraVent.destroy()) # Sale de la ventana
    botonSalir.place(relx=0.7, rely=0.75, anchor=tk.CENTER)

def devuelveReporte(ventanaMain, pOpcion, pProductos, pUsuarios, pCompras, pTracking, medio):
    """
    Funcionalidad: devuelve el reporte o ventana de acuerdo a opción
    Entrada: ventanaMain (CTK)
    pOpcion (int) 
    pProductos (dict) 
    pUsuarios (list) 
    pCompras (list) 
    pTracking (list)
    Salida: genera reporte o devuelve ventana para generarlo / mensaje retroalimentación
    """
    if pOpcion == 0:
        messagebox.showinfo("Reporte creado", 
        "El reporte de los casilleros ha sido creado.")
        return reporteCasilleros(pUsuarios)
    elif pOpcion == 1:
        return reporteProdCasilleroVent(ventanaMain, pProductos, pCompras)
    elif pOpcion == 2:
        return reporteCompraVent(ventanaMain, pProductos, pTracking)
    elif pOpcion == 3:
        messagebox.showinfo("Reporte creado", 
        "El reporte por tipoi de medio ha sido creado.")
        return reportesMedio(pTracking, pCompras, medio)
    elif pOpcion== 4:
        messagebox.showinfo("Reporte creado", 
        "El reporte de tracking ha sido creado.")
        return reportesEntregas(pTracking, pCompras)
    else:
        messagebox.showerror("Número de opción no válido""Digite una opción del 1 al 4")

def obtenerOpcReportes(pReportes, pOpcion):
    """
    Funcionalidad: devuelve la posición en pReportes de pOpcion
    Entrada: pReportes (list)
    pOpcion (int) 
    Salida: posición de pOpcion (int)
    """
    return pReportes.index(pOpcion)

def reportesVent(ventanaMain, pProductos, pUsuarios, pCompras, pTracking, medio):
    """
    Funcionalidad: ventana para los reportes
    Entrada: ventanaMain (CTK)
    pOpcion (int) 
    pProductos (dict) 
    pUsuarios (list) 
    pCompras (list) 
    pTracking (list)
    Salida: genera reporte o devuelve ventana para generarlo con la función 
            / mensaje retroalimentación
    """
    reportesVent = ctk.CTkToplevel(ventanaMain)
    reportesVent.geometry("400x200")
    reportesVent.title("Reportes")
    reportesTipos = ["Listar casilleros", "Productos comprados por casillero", 
    "Tracking de una compra", "Tracking por medio", "Entregas"]
    titulo = ctk.CTkLabel(reportesVent, text="Reportes HTML", text_font=fuenteTitulo)
    titulo.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subTitulo = ctk.CTkLabel(reportesVent, 
    text="Seleccione el reporte que quiere obtener",
    text_font=fuenteBotones)
    subTitulo.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    opcionReportes = ctk.StringVar(value="Entregas")
    opcionesSeleccion = ctk.CTkComboBox(master=reportesVent,
                                width=200, height=32,
                                values=reportesTipos,
                                variable=opcionReportes)
    opcionesSeleccion.place(relx=0.50, rely=0.4, anchor=tk.CENTER)
    botonReporte = ctk.CTkButton(master=reportesVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Crear / Ir",
                                 command=lambda: 
                                 devuelveReporte(ventanaMain, obtenerOpcReportes(reportesTipos, 
                                 opcionReportes.get()), pProductos, pUsuarios, pCompras, pTracking, medio))
    botonReporte.place(relx=0.30, rely=0.7, anchor=tk.CENTER)
    botonSalir = ctk.CTkButton(master=reportesVent,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotones,
                                 text="Regresar",
                                 command=reportesVent.destroy)
    botonSalir.place(relx=0.70, rely=0.7, anchor=tk.CENTER)

def bloqueoReportes(ventanaMain, pProductos, pUsuarios, pCompras, pTracking, medio):
    """
    Funcionalidad: bloqueo botón 5 si no se han generado los tracking
    Entrada: ventanaMain (CTK)
    pProductos (dict) 
    pUsuarios (list) 
    pCompras (list) 
    pTracking (list)
    Salida: reportesVent(ventanaMain, pProductos, pUsuarios, pCompras, pTracking) (TopLevel())
    """
    if len(pTracking) == 0:
        return messagebox.showerror("Tracking vacíos", "No se han generado el tracking de las compras.")
    return reportesVent(ventanaMain, pProductos, pUsuarios, pCompras, pTracking, medio)

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
    productos = {} # Debe estar vacío y usarse para la primer función
    usuarios = []
    compras = []
    tracking = []
    medio=["aéreo", "terrestre", "marítimo"]
    crearArchivoXML("Prueba",convertirDatosXML(purificarDatos(obtenerDatosCSV())))
    tipocambio=607 #cambioUSDtoCRC()
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
                                 command=lambda: leerArchivoXML("Prueba",productos))
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
                                 command=lambda: bloqueoGenerarTracking(compras, tracking, tipocambio))
    boton4.grid(row = 4, column=1, padx=5, pady=5, ipadx=15, ipady=10)
    boton5 = ctk.CTkButton(master=app,
                                 width=120,
                                 height=32,
                                 corner_radius=8,
                                 fg_color="grey",
                                 text_font=fuenteBotonesMenu,
                                 text="5. Reportes",
                                 command=lambda: bloqueoReportes(app, productos, usuarios, compras, tracking, medio))
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