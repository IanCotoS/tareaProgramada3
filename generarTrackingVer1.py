#Autores: Ian Coto Soto y Fabián Araya Ortega
#Fecha de creación: 10/11/2022
#Última actualización: ##/##/2022
#Versión: 3.10.6
#Librerías importadas
from claseTrackingVer1 import *
import random

#Variables Globales
numerosCompra=[1,2,3,4,5,6,7,8,9,0]


def  generarTracking(cant):
    global numerosCompra
    while cant!=0:
        paquete=Tracking(random.randint(1,7500), 
        numerosCompra[random.randint(0,9)], )