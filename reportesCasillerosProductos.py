# Creado por: Ian Steven Coto Soto, Fabián Araya
# Fecha de creación: 20/11/2022 02:30 pm
# Última modificación: 20/11/2022 XX:XX pm
# Versión: 3.10.8

# Importar librerías

# Función archivos HTML
def crearArchivoHtml(pNombre, pInfo):
    """
    Funcionalidad: crea el archivo HTML
    Entradas: pNombre (str)
              pInfo (str)
    Salidas: N/A
    """
    archivo = open(pNombre + ".html", 'w', encoding="utf-8")
    archivo.write(pInfo)
    archivo.close
    return

# Funciones reportes
# Casilleros


# Productos

