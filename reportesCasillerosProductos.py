# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 20/11/2022 02:30 pm
# Última modificación: 22/11/2022 11:45 pm
# Versión: 3.10.8

# Importar librerías
from claseUsuario import *
from claseCompra import *
from conversionWebService import *
from tkinter import messagebox

# Función archivos HTML
def crearArchivoHtml(pNombre, pInfo):
    """
    Funcionalidad: crea el archivo HTML
    Entradas: pNombre (str)
              pInfo (str)
    Salidas: N/A
    """
    archivo = open(pNombre + ".html", 'w', encoding="utf-8")
    archivo.write(pInfo)
    archivo.close
    return

# Funciones reportes
# Casilleros
def reporteCasilleros(pUsuarios):
    """
    Funcionalidad: crea el archivo HTML con la información de los usuarios (sus casilleros)
    Entradas: pUsuarios
    Salidas: resultado crearArchivoHtml("Reporte casilleros AeroTEC", strTabla) (HTML file)
    """
    strTabla = "<html>\n<head>\n<title> \nCasilleros AeroTEC \n\
                </title>\n</head><body><h1>Casilleros AeroTEC</h1> \
                <table><tr><th>Número de casillero</th><th>Nombre completo</th> \
                    <th>País</th><th>Método de pago</th></tr>"
    for usuario in pUsuarios:
        nombreTupla = usuario.obtenerNomDuenno()
        strElementos = ("<tr><td>"+str(usuario.obtenerNumCuenta())+"</td><td>"+
            nombreTupla[0]+" "+nombreTupla[1]+" "+nombreTupla[2]+"</td> \
                <td>"+retornarPaisStr(usuario.obtenerPais())+"</td>\
                    <td>"+retornarMetPagoStr(usuario.obtenerMetPago())+"</td></tr>")
        strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte casilleros AeroTEC", strTabla)

# Productos por casillero
def existeCasillero(pCasillero, pCompras):
    """
    Funcionalidad: comprueba que el casillero exista
    Entradas: pCasillero (int) 
              pCompras (list of compra)
    Salidas: True/False (bool)
    """
    for compra in pCompras:
        if pCasillero == compra.obtenerNumCuenta():
            return True
    return False

def obtenerDetCasillero(pCasillero, pCompras):
    """
    Funcionalidad: obtiene el atributo del detalle según su num de cuenta
    Entradas: pCasillero (int) 
              pCompras (list of compra)
    Salidas: detalle de la compra (list of lists)
    """
    for compras in pCompras:
        if pCasillero == compras.obtenerNumCuenta():
            return compras.obtenerDetalle()
    return []

def obtenerProdCasillero(pCasillero, pCompras, pProductos):
    """
    Funcionalidad: obtiene los datos del producto en pProdutos, según el 
                   detalle del casillero
    Entradas: pCasillero (int) 
              pCompras (list of compra)
              pProductos (dict)
    Salidas:
    """
    prodsCasillero = obtenerDetCasillero(pCasillero, pCompras)
    productos = []
    valorColon = cambioUSDtoCRC()
    for compra in prodsCasillero:
        for codigo, datos in pProductos.items():
            if compra[0] == codigo:
                productos.append((datos[0], datos[1][0], round(datos[1][0]*valorColon, 2)))
                break
    return productos

def reportesProductos(pCasillero, pCompras, pProductos):
    """
    Funcionalidad: crea el reporte de productos según el casillero
    Entradas: pCasillero (int) 
              pCompras (list of compra)
              pProductos (dict)
    Salidas: crearArchivoHtml("Reporte productos casillero " + str(pCasillero), strTabla) (HTML file)
    """
    productos = obtenerProdCasillero(pCasillero, pCompras, pProductos)
    strTabla = "<html>\n<head>\n<title> \nProductos casillero "+str(pCasillero)+" \n\
                </title>\n</head><body><h1>Casillero "+str(pCasillero)+"</h1> \
                <table><tr><th>Nombre del producto</th><th>Precio dólares</th> \
                    <th>Precio colones</th></tr>"
    for producto in productos:
        print(producto)
        strElementos = ("<tr><td>"+producto[0]+"</td><td>"+
            str(producto[1])+"</td><td>"+str(producto[2])+"<td></tr>")
        strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte productos casillero " + str(pCasillero), strTabla)
        
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
    return reportesProductos(int(pCasillero), pCompras, pProductos)

# Pruebas
"""
usuarios = crearUsuariosAux(10, [])
print("\nPruebas:\nUsuarios\n", usuarios, "\nCantidad:", len(usuarios))
for i in usuarios:
    print(i.obtenerInfo())
productos = {"OF-1234":["Secadora", (1000.12, 54.32)], "OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-5321":["Bola", (153.12, 7.432)], "OF-4312":["Camisa", (573.12, 12.43)], 
"OF-5343":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)],
"OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)]}
compras = crearCompras(usuarios, productos, [])
print("\nCompras\n", compras, "\nCantidad:", len(compras))
for i in compras:
    print(i.obtenerInfo())

reportesProductosAux(10, compras, productos)
"""
