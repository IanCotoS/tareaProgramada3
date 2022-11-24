#Autores: Ian Coto Soto y Fabián Araya Ortega
#Fecha de creación: 10/11/2022
#Última actualización: ##/##/2022
#Versión: 3.10.6
#Librerías importadas
from claseTrackingVer1 import *
import random

#Variables Globales
tracking=("Tienda", "Miami", "Tu país", "Entregado en domicilio", "Entregado en oficina")
medio=["aéreo", "terrestre", "marítimo"]
listatracking=[]

def  generarTracking(listaobjetos):
    global listatracking
    for objeto in listaobjetos:
        listadetalles=objeto.obtenerDetalles()
        for codigop in listadetalles:
            nTracking=random.randint(1,7500)
            nCompra=objeto.obtenerNcompra()
            codigoP=codigop[0]
            trackingnum=random.randint(0, 4)
            medionum=random.randint(0, 2)
            if medionum==0:
                costoprimer=codigop[2]*0.06
            else:
                costoprimer=codigop[2]*0.05
            costosegun=costoprimer*617 #Precio del cambio del dolar
            listacosto=[costoprimer, costosegun]
            paquete=Tracking( nTracking, nCompra, codigoP, trackingnum, 
            medionum, tuple(listacosto))
            listatracking.append(paquete)