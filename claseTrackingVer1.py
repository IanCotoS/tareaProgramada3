#Autores: Ian Coto Soto y Fabián Araya Ortega
#Fecha de creación: 10/11/2022
#Última actualización: ##/##/2022
#Versión: 3.10.6


#Clase
class Tracking:
    def __init__(self, nTracking, nCompra, nFactura, nEstado, nMedio, nCosto ):
        self.tracking=nTracking
        self.compra=nCompra
        self.codigo=nFactura
        self.estado=nEstado
        self.medio=nMedio
        self.costo=nCosto
    
    def getTracking(self):
        return self.tracking

    def getCompra(self):
        return self.compra

    def getCodigo(self):
        return self.codigo
    
    def getEstado(self):
        return self.estado

    def getMedio(self):
        return self.medio

    def getCosto(self):
        return self.costo