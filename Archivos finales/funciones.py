# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/11/2022 07:45 pm
# Última modificación: 23/11/2022 09:30 pm
# Versión: 3.10.8

# Importar librerías
from datetime import datetime
from tkinter import messagebox
import requests
import random
import string
from names import *
from clases import *
import csv
import xml.etree.ElementTree as ET

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
    url = "https://api.apilayer.com/fixer/convert?to=CRC&from=USD&amount=1"
    payload = {}
    headers= {"apikey": "QsXLGNtt1JaTYyEmQZRikj8HnvAKlMlM"}
    response = requests.request("GET", url, headers=headers, data = payload)
    return response.json()['info']['rate']

# 1. Importar producto
def obtenerDatosCSV():
    """
    F:Obtiene los datos del archivo.csv y los guarda los datos por fila en una matriz.
    E:N/A
    S:La matriz con todos los datos del documento csv
    """
    archivo= open("HojaParaTP3.csv", encoding="utf8")
    csv_archivo=csv.reader(archivo)
    datos=[]
    for fila in csv_archivo:
        datos.append(fila)
    archivo.close()
    return datos

def purificarDatos(lista):
    """
    F:Funcion que se encarga de purificar los datos provenientes de la matriz creada
    E:lista (list); lista con todos los datos del archivo 
    S:listanueva (list); Lista con los valores corregidos 
    """
    listanueva=[]
    for fila in lista:
        if fila[2]!='':
            if (fila[2][0]=="E") or (fila[2][0]=="O") or (fila[2][0]=="H"):
                fila[3]=fila[3].replace("&", "y")
                fila[4]=fila[4].replace(",", "")
                listanueva.append(fila)
    return listanueva

def convertirDatosXML(lista):
    """
    F:Funcion que acomoda los datos purificados en un formato xml.
    E:lista(list)
    S:stringdatos(str)
    """
    stringdatos="""
                    <almacen>"""
    for fila in lista:
        stringdatos+="""
                        <producto>
                            <codigoProducto>%s</codigoProducto>
                            <nombreProducto>%s</nombreProducto>
                            <precio>%s</precio>
                        </producto>""" % (fila[2], fila[3], fila[4])
    stringdatos+="""
                    </almacen>"""
    return stringdatos 


def crearArchivoXML(pNombre, pInfo):
    """
    Funcionalidad: crea el archivo XML
    Entradas: pNombre (str)
              pInfo (str)
    Salidas: N/A
    """
    archivo = open(pNombre + ".xml", 'w', encoding="utf-8")
    archivo.write(pInfo)
    archivo.close
    return    

def leerArchivoXML(pnombre,diccionario,tipocambiomx):
    """
    F:Funcion que abre el archivo .xml y obtiene los datos correspondientes.
    E:pnombre(str); nombre del archivo, diccionario(dicc)
    S:diccionario (dic); el diccionario con todos los datos del documento.xml
    """
    doc = open(pnombre + ".xml", encoding="utf-8")
    almacen = ET.fromstring(doc.read())
    productos = almacen.findall('producto')
    contador=0
    for producto in productos:
        codigo=producto.find("codigoProducto").text
        nombre=producto.find("nombreProducto").text
        precio=producto.find("precio").text
        dolar=round(tipocambiomx*float(precio), 6) #funcionDolar
        diccionario[codigo]=[nombre,(float(precio),dolar)]
        contador+=1
    print(diccionario)
    print("Cantidad total: ",contador)
    return diccionario

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
            subtotal = round(((pDiccProductos[codigoAct][1][1])*cantProducto), 6) # redondea a dos decimales
            comprasRealizadas.append([codigoAct, cantProducto, subtotal])
            total += subtotal
    return comprasRealizadas, round(total, 6)

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
def generarTracking(listaobjetos, listatracking, tipocambio):
    """
    Funcionalidad: genera las lista con las instancias de la clase Tracking
    Entradas: listaobjetos (list) 
    listatracking (list) 
    tipocambio (float)
    Salidas: listatracking (list) (actualizada)
    """
    contador=0
    for objeto in listaobjetos:
        listadetalles=objeto.obtenerDetalle()
        for codigop in listadetalles:
            nTracking=random.randint(1,100000)
            nCompra=objeto.obtenerNumCompra()
            codigoP=codigop[0]
            trackingnum=random.randint(0, 4)
            medionum=random.randint(0, 2)
            if medionum==0:
                costoprimer=round(codigop[2]*0.06,6)
            else:
                costoprimer=round(codigop[2]*0.05, 6)
            costosegun=round(costoprimer*tipocambio, 6) #Precio del cambio del dolar
            listacosto=[costoprimer, costosegun]
            paquete=Tracking(nTracking, nCompra, codigoP, trackingnum, 
            medionum, tuple(listacosto))
            listatracking.append(paquete)
            print(paquete.getInfo())
            contador+=1
    print("Cantidad total: ", contador)
    return listatracking

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
    """
    Funcionalidad: retorna el país por posición en la lista
    Entradas: pNumPais (int)
    Salidas: listaPaises[pNumPais] (str)
    """
    listaPaises = ["Belice", "Costa Rica", "El Salvador", 
    "Guatemala", "Honduras", "Nicaragua", "Panama"]
    return listaPaises[pNumPais]

def retornarMetPagoStr(pNumMet):
    """
    Funcionalidad: retorna el método de pago por posición en la lista
    Entradas: pNumMet (int)
    Salidas: listaMetPago[pNumMet-1] (str)
    """
    listaMetPago = ["Tarjeta de crédito internacional", "Tarjeta de débito internacional",
    "Pay Pal"]
    return listaMetPago[pNumMet-1]

def reporteCasilleros(pUsuarios):
    """
    Funcionalidad: crea el archivo HTML con la información de los usuarios (sus casilleros)
    Entradas: pUsuarios (list)
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

def obtenerProdCasillero(pCasillero, pCompras, pProductos, valorColon):
    """
    Funcionalidad: obtiene los datos del producto en pProdutos, según el 
                   detalle del casillero
    Entradas: pCasillero (int) 
              pCompras (list of compra)
              pProductos (dict)
              valorColon (float)
    Salidas: productos (list)
    """
    prodsCasillero = obtenerDetCasillero(pCasillero, pCompras)
    productos = []
    for compra in prodsCasillero:
        for codigo, datos in pProductos.items():
            if compra[0] == codigo:
                productos.append((datos[0], datos[1][1], round(datos[1][1]*valorColon, 6)))
                break
    return productos

def reportesProductos(pCasillero, pCompras, pProductos, tipoCambioCRC):
    """
    Funcionalidad: crea el reporte de productos según el casillero
    Entradas: pCasillero (int) 
              pCompras (list of compra)
              pProductos (dict)
    Salidas: crearArchivoHtml("Reporte productos casillero " + str(pCasillero), strTabla) (HTML file)
    """
    productos = obtenerProdCasillero(pCasillero, pCompras, pProductos, tipoCambioCRC)
    strTabla = "<html>\n<head>\n<title> \nProductos casillero "+str(pCasillero)+" \n\
                </title>\n</head><body><h1>Casillero "+str(pCasillero)+"</h1> \
                <table><tr><th>Nombre del producto</th><th>Precio dólares</th> \
                    <th>Precio colones</th></tr>"
    for producto in productos:
        strElementos = ("<tr><td>"+producto[0]+"</td><td>"+
            str(producto[1])+"</td><td>"+str(producto[2])+"<td></tr>")
        strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte productos casillero " + str(pCasillero), strTabla)
        

# Tracking de una compra
def obtenerNombre(codigo, diccionario):
    """
    Funcionalidad: Obtiene el nombre del producto
    Entradas: codigo(str), diccionario (Dicc)
    Salidas: diccionario[key][0]; el nombre del producto
    """
    for key in diccionario:
        if key==codigo:
            return diccionario[key][0]

def reportesCompra(listatracking, pCompras, diccionario):
    """
    Funcionalidad: crea el reporte de productos según el número de compra
    Entradas: pCompras (int) 
              listatracking (list)
              diccionario (dict)
    Salidas: crearArchivoHtml("Reporte Compra " + str(pCompras), strTabla) (HTML file)
    """
    strTabla = "<html>\n<head>\n<title> \nCompras\n\
                </title>\n</head><body><h1>Número de Compra "+str(pCompras)+"</h1> \
                <table><tr><th>Nombre del producto</th><th>Número de tracking</th><th>Costo en dólares</th> \
                    <th>Costo en colones</th></tr>"
    for tracking in listatracking:
        if tracking.getCompra()==pCompras:
            nombreproducto=obtenerNombre(tracking.getCodigo(), diccionario)
            costo=tracking.getCosto()
            strElementos = ("<tr><td>"+nombreproducto+"</td><td>"+
                str(tracking.getTracking())+"</td><td>"+str(costo[0])+"</td><td>"+str(costo[1])+"</td></tr>")
            strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte Compra " + str(pCompras), strTabla)

# Tracking por medio
def reportesMedio(listatracking, listacompras, medio):
    """
    Funcionalidad: crea el reporte de productos para todos los medios
    Entradas: listatracking (list) 
              listacompras (list)
              medio (list)
    Salidas: crearArchivoHtml("Reporte Medios", strTotal) (HTML file)
    """
    strTotal="<html>\n<head>\n<title> \nReporte por medios \n"
    for i in range (0,3):
        strTabla = "</title>\n</head><body><h1>Medio: "+medio[i]+"</h1> \
                    <table><tr><th>Número de tracking</th><th>Número de compra</th><th>Código de compra</th> \
                        <th>Cantidad</th><th>Costo en dólares</th><th>Costo en colones</th></tr>"
        for tracking in listatracking:
            if tracking.getMedio()==i:
                numCompra=tracking.getCompra()
                numTracking=tracking.getTracking()
                codigoCompra=tracking.getCodigo()
                for compra in listacompras:
                    if numCompra==compra.obtenerNumCompra():
                        detalle=compra.obtenerDetalle()
                        for item in detalle:
                            if codigoCompra==item[0]:
                                cantidad=item[1]
                costo=tracking.getCosto()
                strElementos = ("<tr><td>"+str(numTracking)+"</td><td>"+
                    str(numCompra)+"</td><td>"+codigoCompra+"</td><td>"+str(cantidad)+"</td><td>"
                    +str(costo[0])+"</td><td>"+str(costo[1])+"</td></tr>")
                strTabla += strElementos
        strTabla += "</table>"
        strTotal+=strTabla
    strTotal+="</html>"
    return crearArchivoHtml("Reporte Medios", strTotal)

# Reporte de entregas
def reportesEntregas(listatracking, listacompras):
    """
    Funcionalidad: crea el reporte de Tracking
    Entradas: listatracking (list) 
              listacompras (list)
    Salidas: crearArchivoHtml("Reporte Entregas", strTabla) (HTML file) 
    """
    strTabla = "<html>\n<head>\n<title> \nEntregas \n\
                </title>\n</head><body><h1>Reporte de Entregas</h1> \
                <table><tr><th>Número de tracking</th><th>Número de compra</th><th>Código de compra</th><th>Cantidad</th> \
                <th>Costo en dólares</th><th>Costo en colones</th></tr>"
    for tracking in listatracking:
        numCompra=tracking.getCompra()
        numTracking=tracking.getTracking()
        codigoCompra=tracking.getCodigo()
        for compra in listacompras:
            if numCompra==compra.obtenerNumCompra():
                detalle=compra.obtenerDetalle()
                for item in detalle:
                    if codigoCompra==item[0]:
                        cantidad=item[1]
        costo=tracking.getCosto()
        strElementos = ("<tr><td>"+str(numTracking)+"</td><td>"+
            str(numCompra)+"</td><td>"+codigoCompra+"</td><td>"+str(cantidad)+"</td><td>"+str(costo[0])+"</td><td>"+
            str(costo[1])+"<td></tr>")
        strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte Entregas", strTabla)
