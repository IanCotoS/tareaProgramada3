# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 16/11/2022 08:20 pm
# Última modificación: 22/11/2022 07:48 pm
# Versión: 3.10.8

# Importar librerías
import requests

# Función

def cambioMXNtoUSD():
    """
    Funcionalidad: cambio actual del MXN a USD
    Entrada: N/A
    Salida: cambio de un peso mexicano a dólares (float)
    """
    response = requests.get(
        f"https://api.frankfurter.app/latest?amount=1&from=MXN&to=USD") # from y to para cambiar de exchange
                                                                                   # con código ISO
    return response.json()["rates"]["USD"] # Conversión

def cambioUSDtoCRC():
    """
    Funcionalidad: cambio actual del USD a CRC
    Entrada: N/A
    Salida: cambio de un dólar a colón (float)
    """
    response = requests.get("http://data.fixer.io/api/latest?access_key=7370ff2962d49abefc56c32f5bc74aa8")
    return response.json()['rates']['CRC']/response.json()['rates']['USD']

# Pruebas
"""
usdCambio = cambioMXNtoUSD()
for cant in range(1, 10000):
    print(cant, "MXN")
    print(cant*usdCambio,"USD")
print(cambioUSDtoCRC())
"""