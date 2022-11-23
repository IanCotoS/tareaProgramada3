# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/11/2022 07:45 pm
# Última modificación: 23/11/2022 11:30 am
# Versión: 3.10.8

# Importar librerías
from datetime import datetime
import requests
import random
import string
from names import *
from clases import *

# Funciones
# Extras
def esEntero(pNum):
    """
    Funcionalidad: comprueba que sea un número entero
    Entradas: pNum (int)
    Salidas: True/False (bool)
    """
    try:
        pNum = int(pNum)
        return True
    except:
        return False

def obtenerListasLlaves(pDicc):
    """
    Funcionalidad: obtener llaves de un diccionario como listas
    Entradas: pDicc (dict)
    Salidas: listaLlaves (list)
    """
    listaLlaves = []
    for llave in pDicc.keys():
        listaLlaves.append(llave) 
    return listaLlaves

# Web service (cambio monedas)
def cambioMXNtoUSD():
    """
    Funcionalidad: cambio actual del MXN a USD
    Entrada: N/A
    Salida: cambio de un peso mexicano a dólares (float)
    """
    response = requests.get(
        f"https://api.frankfurter.app/latest?amount=1&from=MXN&to=USD") # from y to para cambiar de exchange
                                                                                   # con código ISO
    return response.json()["rates"]["USD"] # Conversión

def cambioUSDtoCRC():
    """
    Funcionalidad: cambio actual del USD a CRC
    Entrada: N/A
    Salida: cambio de un dólar a colón (float)
    """
    response = requests.get("http://data.fixer.io/api/latest?access_key=7370ff2962d49abefc56c32f5bc74aa8")
    return response.json()['rates']['CRC']/response.json()['rates']['USD']

# 1. Importar producto
"""Agregarla"""

# 2. Crear usuarios
def crearContrasenna():
    """
    Función: crea una contraseña de 8 caracteres, en el orden: letra mayúscula,
    letra minúscula, dígito, letra, letra, dígito y dos carácteres especiales.
    Siempre se mantiene el orden de grupos pero los caracteres no son iguales
    Entrada: N/A
    Salida: contraseña con el orden anteriormente mencionado (str)
    """   
    return (random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) +
    random.choice(string.digits) + random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + 
    random.choice(string.digits) + random.choice(string.punctuation) + random.choice(string.punctuation))

def crearDireccion():
    """
    Función: crea una dirección ficticia para los usuarios
    Entrada: N/A
    Salida: dirección según calle de referencia o recidencia específica (str)
    """   
    direcciones = ["Avenida", "Calle", "Autopista"]
    lugares = ["Condominio", "Edificio", "Urbanización"]
    nombresLugares = ["Antares", "Arrabrá", "El Olivo", "Vitonuova", "La Arboleda"]
    if random.randint(0,1) == 0:
        return (random.choice(lugares) + " " + random.choice(nombresLugares))
    return (random.choice(direcciones) + " " + str(random.randint(1, 99)))

def usuarioRepetido(pNomUsuario, pUsuarios):
    """
    Función: retorna True si el nombre de usuario se encuentra
             en el sistema
    Entrada: pNomUsuario (str)
             pUsuarios (list)
    Salida: True/False (bool)
    """  
    for usuario in pUsuarios:
        if usuario.obtenerNomUsuario() == pNomUsuario:
            return True
    return False

def crearUsuarios(pCant, pUsuarios):
    """
    Función: crea la cantidad de usuarios ingresada y lo retorna en una lista
             de instancias de la clase Usuarios, considerando que no se deben
             repetir nombres de usuarios
    Entrada: pCant (int)
             pUsuarios (list)
    Salida: pUsuarios (list)
    """  
    numCasillero = 1
    while numCasillero <= pCant:
        usuario = Usuario()
        usuario.asignarNombre(get_first_name(), get_last_name(), get_last_name())
        usuario.asignarUsuario() # Comprobar usuario repetido
        if usuarioRepetido(usuario.obtenerNomUsuario(), pUsuarios):
            continue
        usuario.asignarNumCuenta(numCasillero)
        usuario.asignarContrasenna(crearContrasenna())
        usuario.asignarDireccion(crearDireccion())
        usuario.asignarPais(random.randint(0,6))
        usuario.asignarMetodoPago(random.randint(1,3))
        pUsuarios.append(usuario)
        print(usuario.obtenerInfo())
        numCasillero += 1
    print("Cantidad total:", len(pUsuarios))
    return pUsuarios

# 3. Generar compras
def crearDetalle(pDiccProductos):
    """
    Función: crea el detalle de los productos por compra, con
             una cantidad aleatoria de entre 1 y 5
    Entrada: pDiccProductos (dict)
    Salida: comprasRealizadas (list) 
            total (float con dos decimales)
    """ 
    cantCompras = random.randint(1, 5)
    codigos = obtenerListasLlaves(pDiccProductos)
    codigosUsados = []
    comprasRealizadas = []
    total = 0.0
    while len(codigosUsados) < cantCompras:
        posCod = random.randint(0, len(codigos)-1)
        codigoAct = codigos[posCod]
        if codigoAct not in codigosUsados:
            codigosUsados.append(codigoAct)
            cantProducto = random.randint(1,3)
            subtotal = round(((pDiccProductos[codigoAct][1][1])*cantProducto), 2) # redondea a dos decimales
            comprasRealizadas.append([codigoAct, cantProducto, subtotal])
            total += subtotal
    return comprasRealizadas, round(total, 2)

def crearCompras(pUsuarios, pDiccProductos, pCompras):
    """
    Función: crea la lista de compras con las instancias de
             Compra
    Entrada: pUsuarios (list of Usuarios)
             pDiccProductos (dict)
             pCompras (list)
    Salida: pCompras (list) (actualizado)
    """  
    for numCompra, usuario in enumerate(pUsuarios):
        compra = Compra()
        compra.asignarNumCompra(numCompra+1*10)
        fechaHoy = datetime.now().date()
        compra.asignarFecha(str(fechaHoy.day) + "/" + str(fechaHoy.month) + "/" + str(fechaHoy.year)) # Fecha de hoy en SO
        compra.asignarNumCuenta(usuario.obtenerNumCuenta())
        comprasLista, total = crearDetalle(pDiccProductos) # Matriz de compras y total
        compra.asignarDetalle(comprasLista)
        compra.asignarTotal(total)
        compra.asignarTienda(random.randint(0,3))
        pCompras.append(compra)
        print(compra.obtenerInfo())
    print("Cantidad total:", len(pCompras))
    return pCompras

# 4. Generar tracking
"""Agregarla"""

# 5. Reportes HTML
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

# Casilleros
def retornarPaisStr(pNumPais):
    listaPaises = ["Belice", "Costa Rica", "El Salvador", 
    "Guatemala", "Honduras", "Nicaragua", "Panama"]
    return listaPaises[pNumPais]

def retornarMetPagoStr(pNumMet):
    listaMetPago = ["Tarjeta de crédito internacional", "Tarjeta de débito internacional",
    "Pay Pal"]
    return listaMetPago[pNumMet-1]

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

# Productos casillero
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
                productos.append((datos[0], datos[1][1], round(datos[1][1]*valorColon, 2)))
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
        

# Tracking de una compra
"""Agregarla"""

# Tracking por medio
"""Agregarla"""

# Reporte de entregas
"""Agregarla"""
