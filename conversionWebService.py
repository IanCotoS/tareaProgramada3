# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 16/11/2022 08:20 pm
# Última modificación: 16/11/2022 XX:XX pm
# Versión: 3.10.8

# Importar librerías
import requests
import json

# Funciones auxiliares
def retornarPeticion(pLink):
    """
    Funcionalidad: se obtiene el código HTML de la página
    Entradas: pLink (str)
    Salidas: codHtml (bs4.BeautifulSoup)
    """
    respuesta = requests.get(pLink).text
    jsonPeticion = json.loads(respuesta)
    return jsonPeticion

#apiFile = open("api.json")
#data = json.load(apiFile)
#apiKey = data["API_KEY"]
#key = "0WoEeaF1fvAODyVlEgZQk8nPp1AO8pc0"
#print(retornarPeticion("http://data.fixer.io/api/latest?access_key="+apiKey))

amount = float(input("Enter in the amount of money: "))

response = requests.get(
    f"https://api.frankfurter.app/latest?amount={amount}&from=MXN&to=USD")

print(f'''{amount} MXN is {response.json()["rates"]["USD"]} USD''')