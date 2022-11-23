# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/11/2022 07:45 pm
# Última modificación: 23/11/2022 11:30 am
# Versión: 3.10.8

# Importar librerías
from tkinter import messagebox
from funciones import *
from clases import *

# Funciones validaciones
# 1. Importar producto
"""Agregarla en caso de necesitar"""

# 2. Crear usuarios
def crearUsuariosAux(pCant, pUsuarios):
    """
    Funcionalidad: valida los datos de entrada
    Entradas: pCant (str)
              pUsuarios (list): no necesita validación porque se introduce
              desde el código, no como entrada
    Salidas: resultado de crearUsuarios(pCant, pUsuarios) (list)
    """
    if len(pUsuarios) != 0:
        return messagebox.showwarning("Usuarios ya existen", "Los usuarios ya han sido creados antes.")
    elif not esEntero(pCant):
        return messagebox.showerror("Cantidad incorrecta", "Debe ingresar un número entero positivo.")
    elif 0 >= int(pCant) or int(pCant) > 1000:
        return messagebox.showerror("Cantidad incorrecta", "Debe ingresar un número entero mayor a 0 y menor a 1001.")
    messagebox.showinfo("Usuarios generadas", f"Los {pCant} usuarios han sido generados.")
    return crearUsuarios(int(pCant), pUsuarios)

# 3. Generar compras

# 4. Generar tracking
"""Agregarla en caso de necesitar"""

# 5. Reportes
# Casilleros
"""No necesita validación"""

# Productos casillero
def reportesProductosAux(pCasillero, pCompras, pProductos):
    """
    Funcionalidad: valida los datos de entrada
    Entradas: 
    Salidas:
    """
    if not esEntero(pCasillero):
        return messagebox.showerror("Formato casillero incorrecto", "Debe ingresar un número entero positivo "+
            "de acuerdo a la cantidad de casilleros disponibles.")
    elif 0 >= int(pCasillero) or int(pCasillero) > len(pCompras):
        return messagebox.showerror("Casillero no encontrado", "Ingrese un casillero existente.")
    messagebox.showinfo("Reporte creado", "El reporte de los productos en el casillero " + 
    pCasillero + " ha sido creado.")
    return reportesProductos(int(pCasillero), pCompras, pProductos)

# Tracking de una compra
"""Agregarla en caso de necesitar"""

# Tracking por medio
"""Agregarla en caso de necesitar"""

# Reporte de entregas
"""Agregarla en caso de necesitar"""
