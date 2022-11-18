#Autores: Ian Coto Soto y Fabián Araya Ortega
#Fecha de creación: 10/11/2022
#Última actualización: ##/##/2022
#Versión: 3.10.6
#Librería Importadas
import csv
import xml.etree.ElementTree as ET
def obtenerDatosCSV():
    """
    F:
    E:
    S:
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
    F:
    E:
    S:
    """
    listanueva=[]
    for fila in lista:
        if fila[2]!='':
            if (fila[2][0]=="E") or (fila[2][0]=="O"):
                fila[3]=fila[3].replace("&", "y")
                fila[4]=fila[4].replace(",", "")
                listanueva.append(fila)
    return listanueva

def convertirDatosXML(lista):
    """
    F:
    E:
    S:
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

def leerArchivoXML(pnombre):
    """
    F:
    E:
    S:
    """
    doc = open(pnombre + ".xml", encoding="utf-8")
    almacen = ET.fromstring(doc.read())
    productos = almacen.findall('producto')
    diccionario={}
    for producto in productos:
        codigo=producto.find("codigoProducto").text
        nombre=producto.find("nombreProducto").text
        precio=producto.find("precio").text
        dolar=0 #funcionDolar
        diccionario[codigo]=[nombre,(float(precio),dolar)]
    return diccionario 

datos=obtenerDatosCSV()
#print(datos[0:20])
crearArchivoXML("Prueba",convertirDatosXML(purificarDatos(datos)))
print(leerArchivoXML("Prueba"))