# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 20/11/2022 02:30 pm
# Última modificación: 20/11/2022 XX:XX pm
# Versión: 3.10.8

# Importar librerías
from claseUsuario import *

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

usuarios = crearUsuariosAux(10, [])

for i in usuarios:
    print(i.obtenerInfo())

reporteCasilleros(usuarios)
# Productos

