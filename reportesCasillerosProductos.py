# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 20/11/2022 02:30 pm
# Última modificación: 22/11/2022 09:30 pm
# Versión: 3.10.8

# Importar librerías
from claseUsuario import *
from claseCompra import *
from conversionWebService import *

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
    Salidas: resultado crearArchivoHtml("", strTabla)
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
def obtenerDetCasillero(pCasillero, pCompras):
    for compras in pCompras:
        if pCasillero == compras.obtenerNumCuenta():
            return compras.obtenerDetalle()
    return []

def obtenerProdCasillero(pCasillero, pCompras, pProductos):
    prodsCasillero = obtenerProdCasillero(pCasillero, pCompras)
    productos = []
    valorColon = cambioUSDtoCRC()
    for compra in prodsCasillero:
        for codigo, datos in pProductos.items():
            if compra[0] == codigo:
                productos.append((datos[0], datos[1][0], datos[1][0]*valorColon))
                break
    return productos

def reportesProductos(pCasillero, pCompras, pProductos):
    productos = obtenerProdCasillero(pCasillero, pCompras, pProductos)
    strTabla = "<html>\n<head>\n<title> \nProductos casillero "+str(pCasillero)+" \n\
                </title>\n</head><body><h1>Casillero "+str(pCasillero)+"</h1> \
                <table><tr><th>Nombre del producto</th><th>Precio dólares</th> \
                    <th>País</th><th>Precio colones</th></tr>"
    for producto in productos:
        strElementos = ("<tr><td>"+producto[0]+"</td><td>"+
            producto[1]+"</td><td>"+producto[2]+"td></tr>")
        strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte productos casillero " + str(pCasillero), strTabla)
        
def reportesProductosAux(pCasillero, pCompras, pProductos):
    """
    Funcionalidad: valida los datos de entrada
    Entradas: 
    Salidas: resultado de crearUsuarios(pCant, pUsuarios) (list)
    """
    if not esEntero(pCasillero):
        return messagebox.showerror("Formato casillero incorrecto", "Debe ingresar un número entero positivo\
            de acuerdo a la cantidad de casilleros disponibles.")
    elif 0 >= int(pCasillero) or int(pCasillero) > len(pCompras):
        return messagebox.showerror("Casillero no encontrado", "Debe ingresar un número entero positivo\
            de acuerdo a la cantidad de casilleros disponibles.")
    return reportesProductos(int(pCasillero), pCompras, pProductos)

# Pruebas
"""
usuarios = crearUsuariosAux(10, [])
for i in usuarios:
    print(i.obtenerInfo())
reporteCasilleros(usuarios)
"""
