# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/11/2022 07:45 pm
# Última modificación: 23/11/2022 11:10 am
# Versión: 3.10.8

# Clase Usuario
class Usuario:

    def __init__(self):
        """
        Método constructor = Crea la estructura de la clase Usuario
        Método que se llama al instanciar
        """
        self.numCuenta = 0
        self.nombreDuenno = ()
        self.usuario = ""
        self.contrasenna = ""
        self.direccion = ""
        self.pais = 0
        self.metodoPago = 0
        return

    def asignarNumCuenta(self, pNumCuenta):
        """
        Función: asigna el número de cuenta al usuario
        Entrada: pNumCuenta (int)
        Salida: asigna la cédula al atributo numCuenta al usuario
        """   
        self.numCuenta = pNumCuenta
        return 
    
    def asignarNombre(self, pNom, pApe1, pApe2):
        """
        Función: asigna el nombre al usuario
        Entrada: pNom, pApe1, pApe2 (string): nombre y dos apellidos
        Salida: asigna un nombre al atributo nombreDuenno del miembro 
                (tupla con 3 items)
        """   
        nombreCompl = (pNom, pApe1, pApe2)
        self.nombreDuenno = nombreCompl
        return
    
    def asignarUsuario(self):
        """
        Función: asigna el nombre de usuario tomando los datos 
        del nombre 
        Entrada: N/A
        Salida: asigna la nombre de usuario al atributo usuario a la instancia
        """
        self.usuario = self.nombreDuenno[0][0:2].lower() + self.nombreDuenno[1][0:2].lower()  + self.nombreDuenno[2][0:2].lower() 
        return
    
    def asignarContrasenna(self, pContra):
        """
        Función: asigna la contraseña al usuario
        Entrada: pContra (str)
        Salida: asigna la contraseña al atributo contrasenna al usuario
        """  
        self.contrasenna = pContra
        return
    
    def asignarDireccion(self, pDirec):
        """
        Función: asigna la dirección al usuario
        Entrada: pDirec (str)
        Salida: asigna la dirección al atributo direccion al usuario
        """  
        self.direccion = pDirec
        return
    
    def asignarPais(self, numPais):
        """
        Función: asigna la dirección al usuario
        Entrada: numPais (int): 0 la 6
        Salida: asigna el número de país al atributo pais al usuario
        (num del 0 al 6)
        """  
        self.pais = numPais
        return
    
    def asignarMetodoPago(self, numMetPago):
        """
        Función: asignar el método de pago al usuario
        Entrada: numMetPago (int): 1 al 3
        Salida: asigna el número de método de pago al atributo metodoPago
        al usuario
        """  
        self.metodoPago = numMetPago
        return

    def obtenerNumCuenta(self):
        """
        Función: retorna el número de cuenta del usuario
        Entrada: N/A
        Salida: self.numCuenta (int)
        """  
        return self.numCuenta

    def obtenerNomDuenno(self):
        """
        Función: retorna el nombre de usuario de la persona
        Entrada: N/A
        Salida: self.nombreDuenno (tuple)
        """  
        return self.nombreDuenno

    def obtenerNomUsuario(self):
        """
        Función: retorna el nombre de usuario
        Entrada: N/A
        Salida: self.usuario (str)
        """  
        return self.usuario

    def obtenerContrasenna(self):
        """
        Función: retorna la contraseña del usuario
        Entrada: N/A
        Salida: self.contrasenna (str)
        """  
        return self.contrasenna

    def obtenerDireccion(self):
        """
        Función: retorna la dirección del usuario
        Entrada: N/A
        Salida: self.direccion (str)
        """  
        return self.direccion

    def obtenerPais(self):
        """
        Función: retorna el número del país del usuario
        Entrada: N/A
        Salida: self.pais (int)
        """  
        return self.pais

    def obtenerMetPago(self):
        """
        Función: retorna el número del método de pago del usuario
        Entrada: N/A
        Salida: self.metodoPago (int)
        """  
        return self.metodoPago
    
    def obtenerInfo(self):
        """
        Función: retorna una tupla con al información de la instancia
        Entrada: N/A
        Salida: self.numCuenta (int)
        self.nombreDuenno (tuple)
        self.usuario (str)
        self.contrasenna (str)
        self.direccion (str)
        self.pais (int)
        self.metodoPago (int)
        """  
        return (self.numCuenta, self.nombreDuenno, self.usuario,
        self.contrasenna, self.direccion, self.pais, self.metodoPago)


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
        return

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
    
    def asignarTienda(self, pNumTienda):
        """
        Función: asigna la tienda a la compra
        Entrada: pNumTienda (int): 0 al 3
        Salida: asigna la tienda al atributo tienda de la compra
        (num aleatorio del 0 al 3)
        """  
        self.tienda = pNumTienda
        return

    def obtenerNumCompra(self):
        """
        Función: retorna el número de la compra
        Entrada: N/A
        Salida: self.numCompra (int)
        """  
        return self.numCompra

    def obtenerFecha(self):
        """
        Función: retorna la fecha de la compra
        Entrada: N/A
        Salida: self.fecha (str)
        """  
        return self.fecha
    
    def obtenerNumCuenta(self):
        """
        Función: retorna el número de cuenta de la compra
        Entrada: N/A
        Salida: self.numCuenta (int)
        """  
        return self.numCuenta

    def obtenerDetalle(self):
        """
        Función: retorna el detalle de la compra
        Entrada: N/A
        Salida: self.detalle (list)
        """  
        return self.detalle

    def obtenerTotal(self):
        """
        Función: retorna el total a pagar de la compra
        Entrada: N/A
        Salida: self.total (float)
        """  
        return self.total
    
    def obtenerTienda(self):
        """
        Función: retorna el número de tienda de la compra
        Entrada: N/A
        Salida: self.tienda (int)
        """  
        return self.tienda
    
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


# Clase Tracking
class Tracking:
    def __init__(self, nTracking, nCompra, nFactura, nEstado, nMedio, nCosto ):
        """
        Método constructor = Crea la estructura de la clase Tracking
        Método que se llama al instanciar
        """
        self.tracking=nTracking
        self.compra=nCompra
        self.codigo=nFactura
        self.estado=nEstado
        self.medio=nMedio
        self.costo=nCosto
    
    def getTracking(self):
        """
        Función: retorna el número de tracking
        Entrada: N/A
        Salida: self.tracking (int)
        """  
        return self.tracking

    def getCompra(self):
        """
        Función: retorna el número de compra
        Entrada: N/A
        Salida: self.compra (int)
        """  
        return self.compra

    def getCodigo(self):
        """
        Función: retorna el número de código
        Entrada: N/A
        Salida: self.codigo (str)
        """  
        return self.codigo
    
    def getEstado(self):
        """
        Función: retorna el número del estado del tracking
        Entrada: N/A
        Salida: self.estado (int)
        """  
        return self.estado

    def getMedio(self):
        """
        Función: retorna el número del medio que se utiliza
        Entrada: N/A
        Salida: self.medio (int)
        """  
        return self.medio

    def getCosto(self):
        """
        Función: retorna el costo del medio
        Entrada: N/A
        Salida: self.costo (tuple)
        """  
        return self.costo

    def getInfo(self):

        return (self.tracking, self.compra, self.codigo, self.estado, self.medio, self.costo)
