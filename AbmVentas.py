from Venta import Venta
import ExpressionFunctions
import AbmArticulos
from FileFunctions import FileFunctions
import sys

archivoVentas = "Input\Ventas.csv"

def SubMenuAbmVentas():
    while True:
        print("1) Alta Venta")
        print("2) Baja Venta")
        print("3) Modificacion Venta")
        print("4) Volver al menu principal")
        choice = input("Seleccione una opcion: ")
        if choice == "1":
            AltaVenta()
        elif choice == "2":
            BajaVenta()
        elif choice == "3":
            ModificarVenta()
        elif choice =="4":
            return
        else:
            print("Opcion invalida. Seleccione una opcion del 1 al 4")

def AltaVenta():

    sucursal = ValidarSucursal()
    codigoArticulo = ValidarCodigo()
    vendedor = input("Ingrese el nombre del vendedor: ")
    importe = ValidarImporte()
    objVenta = Venta(codigoArticulo,vendedor,sucursal,importe)

    try:
        linea = "\n" + objVenta.sucursal + "," + objVenta.codigoArticulo + "," + objVenta.vendedor + "," + objVenta.importe + "," + objVenta.fecha
        CrearCabecera()
        FileFunctions.EscribirLineaEnArchivo(archivoVentas, linea)
        print("Venta dada de alta exitosamente")

    except:
        print("Error Detallado: ",sys.exc_info()[1])
        print("Error al intentar escribir en el archivo la nueva venta\n")
        

def BajaVenta():
    codigoDeArticuloAEliminar = input("Ingrese el codigo del producto de la venta a eliminar: ")
    try:
        lista = FileFunctions.LeerArchivo(archivoVentas)

        codigoExiste = False
        for line in lista:
            if codigoDeArticuloAEliminar in line:
                codigoExiste = True
                lineaParaEliminar = line

        if codigoExiste:
        
                lista.remove(lineaParaEliminar)
                FileFunctions.EscribirListaEnArchivo(archivoVentas,lista)
                print('-----------------------------------------------')
                print("Venta eliminado correctamente")
                print('-----------------------------------------------')
        else:
            print("El código del producto ingresado no existe\n")
    except:
        print("Error Detallado: ",sys.exc_info()[1])
        print("Error al intentar escribir en el archivo la venta a dar de baja\n")
    
        
def ModificarVenta():
    codigoDeArticuloAModificar = input("Ingrese el codigo del producto de la venta a modificar: ")
    try:
        lista = FileFunctions.LeerArchivo(archivoVentas)
        codigoExiste = False
        for line in lista:
            if codigoDeArticuloAModificar in line:
                codigoExiste = True
                lineaParaEliminar = line

        if codigoExiste:
            
                lista.remove(lineaParaEliminar)
                vendedor = input("Ingrese el nombre del vendedor: ")
                importe = ValidarImporte()
                sucursal = ValidarSucursal()
                objVenta = Venta(codigoDeArticuloAModificar,vendedor,sucursal,importe)
                lineaModificada = "\n" + objVenta.sucursal + "," + objVenta.codigoArticulo + "," + objVenta.vendedor + "," + objVenta.importe + "," + objVenta.fecha
                FileFunctions.EscribirListaEnArchivo(archivoVentas,lista)
                FileFunctions.EscribirLineaEnArchivo(archivoVentas,lineaModificada)
                print('-----------------------------------------------')
                print("Venta modificada correctamente")
                print('-----------------------------------------------')
        else:
            print("El código del artículo ingresado no existe en el archivo de ventas\n")
    except:
            print("Error Detallado: ",sys.exc_info()[1])
            print("Error al intentar escribir en el archivo la venta a modificar\n")

def CrearCabecera():
    lista = FileFunctions.LeerArchivo(archivoVentas)
    if not lista:
        linea = "Sucursal,CodigoArticulo,NombreVendedor,Importe,Fech"
        FileFunctions.EscribirLineaEnArchivo(archivoVentas, linea)

def TraerTodos():
    try:
        lista = FileFunctions.LeerArchivo(archivoVentas)
        print(*lista, sep='\n')
    except:
        print("Ocurrio un error al intentar leer el archivo de ventas")

def ValidarCodigo():

    codigoInvalido = True

    while(codigoInvalido):
        codigoSinValidar = input("Ingrese el codigo: ")
        if ExpressionFunctions.EsCodigoDeArticuloValido(codigoSinValidar):
            if AbmArticulos.CodigoYaExiste(codigoSinValidar):
                codigoInvalido = False
                return codigoSinValidar
            else:
                print("El codigo de articulo ingresado no ha sido dado de alta en el archivo de Articulos")
                print("Por favor intente nuevamente\n")
        else:
            print("El codigo ingresado no posee el formato adecuado")
            print("Por favor intente nuevamente\n")

def ValidarSucursal():
    sucursalInvalida = True

    while(sucursalInvalida):
        sucursalSinValidar = input("Ingrese la sucursal: ")
        if ExpressionFunctions.EsSucursalValida(sucursalSinValidar):
            sucursalInvalida = False
            return sucursalSinValidar
        else:
            print("La sucursal ingresada no posee el formato adecuado")
            print("Por favor intente nuevamente\n")

def ValidarImporte():

    importeInvalido = True

    while(importeInvalido):
        importeSinValidar = input("Ingrese el importe: ")
        if ExpressionFunctions.EsEnteroValido(importeSinValidar):
            importeInvalido = False
            return importeSinValidar
        else:
            print("El importe ingresado no posee el formato adecuado\n")
            print("Por favor intente nuevamente\n\n")
            
def ArticuloEstaAsociadoAUnaVenta(pCodigo):
    lista = FileFunctions.LeerArchivo(archivoVentas)
    
    for line in lista:
        if pCodigo in line:
            return True
        
    return False
    

        