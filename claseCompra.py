# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 16/11/2022 09:35 pm
# Última modificación: 17/11/2022 01:30 pm
# Versión: 3.10.8

# Importar librerías
import random
from datetime import datetime # Para obtener la fecha del día
from claseUsuario import *

# Variables globales
tienda = ("Amazon", "Ebay", "Rakuten", "ToysRus")

# Funciones auxiliares
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
            subtotal = round((pDiccProductos[codigoAct][1][1])*cantProducto, 2) # redondea a dos decimales
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
        compra.asignarNumCuenta(usuario.obtenerInfo()[0])
        comprasLista, total = crearDetalle(pDiccProductos) # Matriz de compras y total
        compra.asignarDetalle(comprasLista)
        compra.asignarTotal(total)
        compra.asignarTienda()
        pCompras.append(compra)
    return pCompras

# Pruebas de funciones
usuarios = crearUsuariosAux(5, [])
print("\nPruebas:\nUsuarios\n", usuarios, "\nCantidad:", len(usuarios))
for i in usuarios:
    print(i.obtenerInfo())
diccProductos = {"OF-1234":["Secadora", (1000.12, 54.32)], "OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-5321":["Bola", (153.12, 7.432)], "OF-4312":["Camisa", (573.12, 12.43)], 
"OF-5343":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)],
"OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)], 
"OF-9310":["Lavadora", (100.12, 5.432)]}
compras = crearCompras(usuarios, diccProductos, [])
print("\nCompras\n", compras, "\nCantidad:", len(compras))
for i in compras:
    print(i.obtenerInfo())

# Prueba de fechas:
fechaHoy = datetime.now()
print("\nFecha SO\n", fechaHoy)

