# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 13/11/2022 07:45 pm
# Última modificación: 13/11/2022 09:05 pm
# Versión: 3.10.8

# Importar libreías
from names import *
import random
import re
import string
from tkinter import messagebox

# Variables globales
listaPaises = ["Belice", "Costa Rica", "El Salvador", 
"Guatemala", "Honduras", "Nicaragua", "Panama"]

# Funciones auxiliares
"""
def validarDireccion(pDireccion):
    if re.match("^[a-zA-Z0-9ÁÉÍÓÚáéíóú\s]{5,}$", pDireccion) == None:
        return False
    return True
"""
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
    
    def asignarPais(self):
        """
        Función: asigna la dirección al usuario
        Entrada: N/A
        Salida: asigna el número de país al atributo pais al usuario
        (num del 0 al 6)
        """  
        self.pais = random.randint(0,6)
        return
    
    def asignarMetodoPago(self):
        """
        Función: asignar el método de pago al usuario
        Entrada: N/A
        Salida: asigna el número de método de pago al atributo metodoPago
        al usuario
        """  
        self.metodoPago = random.randint(1,3)
        return

    def obtenerNomUsuario(self):
        """
        Función: retorna el nombre de usuario
        Entrada: N/A
        Salida: self.usuario (str)
        """  
        return self.usuario
    
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


# Función Crear usuarios
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
        usuario.asignarPais()
        usuario.asignarMetodoPago()
        pUsuarios.append(usuario)
        numCasillero += 1
    return pUsuarios

def crearUsuariosAux(pCant, pUsuarios):
    """
    Funcionalidad: valida los datos de entrada
    Entradas: pCant (str)
              pUsuarios (list): no necesita validación porque se introduce
              desde el código, no como entrada
    Salidas: resultado de crearUsuarios(pCant, pUsuarios) (list)
    """
    if not esEntero(pCant):
        return messagebox.showerror("Cantidad incorrecta", "Debe ingresar un número entero positivo.")
    elif 0 >= int(pCant) or int(pCant) > 1000:
        return messagebox.showerror("Cantidad incorrecta", "Debe ingresar un número entero mayor a 0 y menor a 1001")
    return crearUsuarios(int(pCant), pUsuarios)

# Pruebas
"""
print(crearUsuariosAux(0, []))
print(crearUsuariosAux(-1, []))
print(crearUsuariosAux(1001, []))
usuarios = crearUsuariosAux(23, [])
print(crearUsuariosAux("asdc", []))

for i in usuarios:
    print(i.obtenerInfo())
"""
