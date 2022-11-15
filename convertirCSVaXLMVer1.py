#Autores: Ian Coto Soto y Fabián Araya Ortega
#Fecha de creación: 10/11/2022
#Última actualización: ##/##/2022
#Versión: 3.10.6
#Librería Importadas
import csv
def obtenerDatosCSV():
    archivo= open("HojaParaTP3.csv", encoding="utf8")
    csv_archivo=csv.reader(archivo)
    datos=[]
    for fila in csv_archivo:
        datos.append(fila)
    archivo.close()
    return datos

def purificarDatos(lista):
    listanueva=[]
    for fila in lista:
        if fila[2]!='':
            if (fila[2][0]=="E") or (fila[2][0]=="O"):
                listanueva.append(fila)
    return listanueva
"""
def crearListaObjetos(lista):
    listaobjetos=[]
    for objeto in lista:
        diccionario={}
        dolar=0 #funcionDolar(objeto[4])
        diccionario[objeto[2]]=[objeto[3],(objeto[4],dolar)]
        listaobjetos.append(diccionario)
    return listaobjetos
"""  

datos=obtenerDatosCSV()
#print(datos[0:20])
print(crearListaObjetos(purificarDatos(datos)))