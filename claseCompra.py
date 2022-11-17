# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 16/11/2022 09:35 pm
# Última modificación: 16/11/2022 09:56 pm
# Versión: 3.10.8

# Importar librerías
import random
from datetime import datetime # Para obtener la fecha del día

# Variables globales
tienda = ("Amazon", "Ebay", "Rakuten", "ToysRus")

# Funciones auxiliares

# Clase Compra
class Compra:

    def __init__(self):
        """
        Método constructor = Crea la estructura de la clase Compra
        Método que se llama al instanciar
        """
        self.numCompra = 0
        self.fecha = ""
        self.numCuenta = 0
        self.detalle = []
        self.total = 0.0
        self.tienda = 0

    def asignarNumCompra(self, pNumCompra):
        """
        Función: asigna el número de compra a la compra
        Entrada: pNumCompra (int)
        Salida: asigna el número de compra al atributo numCompra a la compra
        """   
        self.numCompra = pNumCompra
        return 
    
    def asignarFecha(self, pFecha):
        """
        Función: asigna la fecha a la compra
        Entrada: pFecha (str)
        Salida: asigna la fecha al atributo fecha de la compra
        """   
        self.fecha = pFecha
        return
    
    def asignarNumCuenta(self, pNumCuenta):
        """
        Función: asigna el número de cuenta a la compra
        Entrada: pNumCuenta (int)
        Salida: asigna el número de cuenta al atributo numCuenta de la compra
        """
        self.numCuenta = pNumCuenta
        return
    
    def asignarDetalle(self, pDetalle):
        """
        Función: asigna el detalle a la compra
        Entrada: pDetalle (list)
        Salida: asigna el detalle al atributo detalle de la compra
        """  
        self.detalle = pDetalle
        return
    
    def asignarTotal(self, pTotal):
        """
        Función: asigna el precio total a la compra
        Entrada: pTotal (float)
        Salida: asigna el total al atributo total de la compra
        """  
        self.total = pTotal
        return
    
    def asignarTienda(self):
        """
        Función: asigna la tienda a la compra
        Entrada: N/A
        Salida: asigna la tienda al atributo tienda de la compra
        (num aleatorio del 0 al 3)
        """  
        self.tienda = random.randint(0,3)
        return
    
    def obtenerInfo(self):
        """
        Función: retorna una tupla con al información de la instancia de compra
        Entrada: N/A
        Salida: self.numCompra (int)
        self.fecha (str) 
        self.numCuenta (int) 
        self.detalle (list)
        self.total (float) 
        self.tienda (int) 
        """  
        return (self.numCompra, self.fecha, self.numCuenta, 
        self.detalle, self.total, self.tienda) 

# Prueba
print("Prueba instancia compra")
compra1 = Compra()
compra1.asignarNumCompra(1)
fechaHoy = datetime.now().date()
compra1.asignarFecha(str(fechaHoy.day) + "/" + str(fechaHoy.month) + "/" + str(fechaHoy.year)) # Fecha de hoy en SO
compra1.asignarNumCuenta(100)
compra1.asignarDetalle([["OF-1234", random.randint(1,3), 30.21], ["OF-9310", random.randint(1,3), 5.14]])
compra1.asignarTotal(35.35)
compra1.asignarTienda()
print(compra1.obtenerInfo())