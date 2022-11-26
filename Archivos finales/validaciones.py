# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/11/2022 07:45 pm
# Última modificación: 25/11/2022 09:10 pm
# Versión: 3.10.8

# Importar librerías
from tkinter import messagebox
from funciones import *
from clases import *

# Funciones validaciones
# 1. Importar producto
def leerArchivoXMLAux(pnombre,diccionario,tipocambiomx):
    """
    Funcionalidad: valida los datos de entrada
    Entradas: pnombre (str)
    diccionario (dict)
    tipocambiomx (float)
    Salidas: resultado de crearUsuarios(pCant, pUsuarios) (list)
    """
    if len(diccionario) != 0:
        return messagebox.showwarning("Productos ya existen", "Los productos ya han sido creados antes.")
    messagebox.showinfo("Productos importados", "Los productos han sido importados.")
    return leerArchivoXML(pnombre,diccionario,tipocambiomx)

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
    elif 0 >= int(pCant):
        return messagebox.showerror("Cantidad incorrecta", "Debe ingresar un número entero mayor a 0.")
    messagebox.showinfo("Usuarios generados", f"Los {pCant} usuarios han sido generados.")
    return crearUsuarios(int(pCant), pUsuarios)

# 3. Generar compras
def crearComprasAux(pUsuarios, pDiccProductos, pCompras):
    """
    Funcionalidad: valida los datos de entrada
    Entradas: pCompras (list)
              pDiccProductos (list)
              pUsuarios (list): no necesita validación porque se introduce
              desde el código, no como entrada
    Salidas: resultado de crearUsuarios(pCant, pUsuarios) (list)
    """
    if len(pCompras) != 0:
        return messagebox.showwarning("Compras ya existen", "Las compras ya habían sido generadas anteriormente.")
    messagebox.showinfo("Compras generadas", "Las compras se han generado.")
    return crearCompras(pUsuarios, pDiccProductos, pCompras)

# 4. Generar tracking
def generarTrackingAux(listaobjetos, listatracking, tipocambio):
    """
    Funcionalidad: valida los datos de entrada
    Entradas: listaobjetos (list)
    listatracking (list)
    tipocambio (float)
    Salidas: resultado de crearUsuarios(pCant, pUsuarios) (list)
    """
    if len(listatracking) != 0:
        return messagebox.showwarning("Tracking ya existe", "El tracking ya ha sido creado antes.")
    messagebox.showinfo("Tracking generado", "El tracking ha sido generado.")
    return generarTracking(listaobjetos, listatracking, tipocambio)

# 5. Reportes
# Casilleros
"""No necesita validación"""

# Productos casillero
def reportesProductosAux(pCasillero, pCompras, pProductos, tipoCambioCRC):
    """
    Funcionalidad: valida los datos de entrada
    Entradas: pCasillero(str), pCompras(str), pProductos(list)
    Salidas:Un mensaje de error o el resultado de reportesProductos(int(pCasillero), pCompras, pProductos)
    """
    if not esEntero(pCasillero):
        return messagebox.showerror("Formato casillero incorrecto", "Debe ingresar un número entero positivo "+
            "de acuerdo a la cantidad de casilleros disponibles.")
    elif 0 >= int(pCasillero) or int(pCasillero) > len(pCompras):
        return messagebox.showerror("Casillero no encontrado", "Ingrese un casillero existente.")
    messagebox.showinfo("Reporte creado", "El reporte de los productos en el casillero " + 
    pCasillero + " ha sido creado.")
    return reportesProductos(int(pCasillero), pCompras, pProductos, tipoCambioCRC)

# Tracking de una compra
def reportesCompraAux(listatracking, pCompras, diccionario):
    """
    Funcionalidad: valida los datos de entrada
    Entradas: listatracking (list), pCompras(str), diccionario(dicc)
    Salidas:Un mensaje de error o el resultado de reportesCompra(listatracking, int(pCompras), diccionario)
    """
    if not esEntero(pCompras):
        return messagebox.showerror("Formato de número de compra incorrecto", "Debe ingresar un número entero positivo")
    elif int(pCompras)<=0:
        return messagebox.showerror("El número de compra es inválido", "Debe ingresar un número de compra mayor que 0")
    else:
        for tracking in listatracking:
            if tracking.getCompra()==int(pCompras):
                messagebox.showinfo("Reporte creado", "El reporte del número de compra: "+pCompras+" ha sido creado.")
                return reportesCompra(listatracking, int(pCompras), diccionario)
        return messagebox.showerror("El número de compra no existe", "Digite otro número de compra")

# Tracking por medio
"""No necesita"""

# Reporte de entregas
"""No necesita"""
