from funciones import *
from clases import *
import random

#Variables Globales
tracking=("Tienda", "Miami", "Tu país", "Entregado en domicilio", "Entregado en oficina")
medio=["aéreo", "terrestre", "marítimo"]
listatracking=[]
tipocambio=607#cambioUSDtoCRC()
print(tipocambio)

def  generarTracking(listaobjetos):
    global listatracking, tipocambio
    for objeto in listaobjetos:
        listadetalles=objeto.obtenerDetalle()
        for codigop in listadetalles:
            nTracking=random.randint(1,7500)
            nCompra=objeto.obtenerNumCompra()
            codigoP=codigop[0]
            trackingnum=random.randint(0, 4)
            medionum=random.randint(0, 2)
            if medionum==0:
                costoprimer=codigop[2]*0.06
            else:
                costoprimer=codigop[2]*0.05
            costosegun=costoprimer*tipocambio #Precio del cambio del dolar
            listacosto=[costoprimer, costosegun]
            paquete=Tracking( nTracking, nCompra, codigoP, trackingnum, 
            medionum, tuple(listacosto))
            listatracking.append(paquete)
            print(paquete.getInfo())
    return listatracking


def reportesCompra(listatracking, pCompras, diccionario):
    """
    Funcionalidad: 
    Entradas: 
    Salidas: 
    """
    strTabla = "<html>\n<head>\n<title> \nCompras\n\
                </title>\n</head><body><h1>Número de Compra "+str(pCompras)+"</h1> \
                <table><tr><th>Nombre del producto</th><th>Número de tracking</th><th>Costo en dólares</th> \
                    <th>Costo en colones</th></tr>"
    for tracking in listatracking:
        if tracking.getCompra()==pCompras:
            nombreproducto=obtenerNombre(tracking.getCodigo(), diccionario)
            costo=tracking.getCosto()
            strElementos = ("<tr><td>"+nombreproducto+"</td><td>"+
                str(tracking.getTracking())+"</td><td>"+str(costo[0])+"</td><td>"+str(costo[1])+"</td></tr>")
            strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte Compra " + str(pCompras), strTabla)

def reportesMedio(listatracking, listacompras, medio):
    """
    Funcionalidad: 
    Entradas: 
    Salidas: 
    """
    strTotal="<html>\n<head>\n<title> \nReporte por medios \n"
    for i in range (0,3):
        strTabla = "</title>\n</head><body><h1>Medio: "+medio[i]+"</h1> \
                    <table><tr><th>Número de tracking</th><th>Número de compra</th><th>Código de compra</th> \
                        <th>Cantidad</th><th>Costo en dólares</th><th>Costo en colones</th></tr>"
        for tracking in listatracking:
            if tracking.getMedio()==i:
                numCompra=tracking.getCompra()
                numTracking=tracking.getTracking()
                codigoCompra=tracking.getCodigo()
                for compra in listacompras:
                    if numCompra==compra.obtenerNumCompra():
                        detalle=compra.obtenerDetalle()
                        for item in detalle:
                            if codigoCompra==item[0]:
                                cantidad=item[1]
                costo=tracking.getCosto()
                strElementos = ("<tr><td>"+str(numTracking)+"</td><td>"+
                    str(numCompra)+"</td><td>"+codigoCompra+"</td><td>"+str(cantidad)+"</td><td>"
                    +str(costo[0])+"</td><td>"+str(costo[1])+"</td></tr>")
                strTabla += strElementos
        strTabla += "</table>"
        strTotal+=strTabla
    strTotal+="</html>"
    return crearArchivoHtml("Reporte Medios", strTotal)

def reportesEntregas(listatracking, listacompras):
    """
    Funcionalidad: 
    Entradas: 
    Salidas: 
    """
    strTabla = "<html>\n<head>\n<title> \nEntregas \n\
                </title>\n</head><body><h1>Reporte de Entregas</h1> \
                <table><tr><th>Número de tracking</th><th>Número de compra</th><th>Código de compra</th><th>Cantidad</th> \
                <th>Costo en dólares</th><th>Costo en colones</th></tr>"
    for tracking in listatracking:
        print(tracking)
        numCompra=tracking.getCompra()
        numTracking=tracking.getTracking()
        codigoCompra=tracking.getCodigo()
        for compra in listacompras:
            if numCompra==compra.obtenerNumCompra():
                detalle=compra.obtenerDetalle()
                for item in detalle:
                    if codigoCompra==item[0]:
                        cantidad=item[1]
        costo=tracking.getCosto()
        strElementos = ("<tr><td>"+str(numTracking)+"</td><td>"+
            str(numCompra)+"</td><td>"+codigoCompra+"</td><td>"+str(cantidad)+"</td><td>"+str(costo[0])+"</td><td>"+
            str(costo[1])+"<td></tr>")
        strTabla += strElementos
    strTabla += "</table></html>"
    return crearArchivoHtml("Reporte Entregas", strTabla)
#PP

listausuario=crearUsuarios(10, [])
crearArchivoXML("Prueba",convertirDatosXML(purificarDatos(obtenerDatosCSV())))
diccionario=leerArchivoXML("Prueba")
#generarTracking(listacompras)

#reportesCompra(listatracking, listatracking[5].getCompra(), diccionario)

#reportesMedio(listatracking, listacompras, medio)

#reportesEntregas(listatracking, listacompras)