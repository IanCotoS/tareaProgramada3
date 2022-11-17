# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 16/11/2022 08:20 pm
# Última modificación: 16/11/2022 09:00 pm
# Versión: 3.10.8

# Importar librerías
import requests

# Funciones auxiliares

def conversionMXNtoUSD(pDineroMXN): # Por ahora es una prueba
    """
    Funcionalidad: convierte de pesos mexicanos a dólares
    Entrada: pDineroMXN (float): dinero en pesos mexicanos
    Salida: dinero en dólares (float)
    """
    response = requests.get(
        f"https://api.frankfurter.app/latest?amount={pDineroMXN}&from=MXN&to=USD") # from y to para cambiar de exchange
                                                                                   # con código ISO
    #print(f'''{pDineroMXN} MXN es {response.json()["rates"]["USD"]} USD''') # Se debe eliminar, solo es
                                                                            # para mostrar resultados
    return response.json()["rates"]["USD"] # Conversión

# Pruebas
print(1000,"MXN")
print(conversionMXNtoUSD(1000),"USD")