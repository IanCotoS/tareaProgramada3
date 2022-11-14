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
        try:
            if (fila[2][0]!="E") or (fila[2][0]!="O"):
                continue
            else:
                datos.append(fila)
        except:
            continue
    archivo.close()
    return datos

datos=obtenerDatosCSV()
print(datos)