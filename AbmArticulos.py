from Articulo import Articulo
import ExpressionFunctions
from FileFunctions import FileFunctions
import sys
import AbmVentas

archivoArticulos = "Input\Articulos.csv"

def SubMenuAbmArticulos():
    while True:
        print("1) Alta Articulo")
        print("2) Baja Articulo")
        print("3) Modificacion Articulo")
        print("4) Salir al menu principal")
        choice = input("Seleccione una opcion: ")
        if choice == "1":
            AltaArticulo()
        elif choice == "2":
            BajaArticulo()      
        elif choice == "3":
            ModificarArticulo()
        elif choice == "4":
            return
        else:
            print("Elija una opcion entre 1 al 4!") 
            
def AltaArticulo():

    codigo = ValidarCodigo()
    descripcion = input("Ingrese la descripcion: ")
    stock = ValidarStock()
    objArticulo = Articulo(codigo,descripcion,stock) #Instanciacion de clase

    try:
        linea = "\n" + objArticulo.Codigo + "," + objArticulo.Descripcion + "," + objArticulo.Stock
        CrearCabecera()
        FileFunctions.EscribirLineaEnArchivo(archivoArticulos, linea)
        print("Articulo dado de alta exitosamente")

    except:
        print("Error al intentar escribir en el archivo el nuevo articulo")
        
def BajaArticulo():
    codigoDeArticuloAEliminar = input("Ingrese el codigo del producto a eliminar: ")
    try:
        lista = FileFunctions.LeerArchivo(archivoArticulos)

        codigoExiste = False
   
        for line in lista:
            if codigoDeArticuloAEliminar in line:
                codigoExiste = True
                lineaParaEliminar = line

        if codigoExiste and not AbmVentas.ArticuloEstaAsociadoAUnaVenta(codigoDeArticuloAEliminar):
            lista.remove(lineaParaEliminar)
            FileFunctions.EscribirListaEnArchivo(archivoArticulos,lista)
            print('-----------------------------------------------')
            print("Articulo eliminado correctamente")
            print('-----------------------------------------------')
        else:
            print("El código del artículo ingresado no existe o bien posee ventas asociadas\n")
    except:
            print("Error Detallado: ",sys.exc_info()[1])
            print("Error al intentar escribir en el archivo la venta dar de baja\n")
        
def ModificarArticulo():
    codigoDeArticuloAModificar = input("Ingrese el codigo del producto de la venta a modificar: ")
    try:
    
        lista = FileFunctions.LeerArchivo(archivoArticulos)

        codigoExiste = False
        for line in lista:
            if codigoDeArticuloAModificar in line:
                codigoExiste = True
                lineaParaModificar = line

        if codigoExiste:
            
                lista.remove(lineaParaModificar)
                descripcion = input("Ingrese la nueva descripcion: ")
                stock = ValidarStock()
                objArticulo = Articulo(codigoDeArticuloAModificar,descripcion,stock)
                lineaModificada = objArticulo.Codigo + "," + objArticulo.Descripcion + "," + objArticulo.Stock
                FileFunctions.EscribirListaEnArchivo(archivoArticulos,lista)
                FileFunctions.EscribirLineaEnArchivo(archivoArticulos, lineaModificada)
                print('-----------------------------------------------')
                print("Articulo modificado correctamente")
                print('-----------------------------------------------')
        else:
            print("El código del artículo ingresado no existe\n")
    except:
        print("Error Detallado: ",sys.exc_info()[1])
        print("Error al intentar escribir en el archivo la venta a modificar\n")
    
        

def TraerTodos():
    try:
        lista = FileFunctions.LeerArchivo(archivoArticulos)
        print(*lista, sep='\n')
    except:
        print("Ocurrio un error al intentar leer el archivo de articulos")

def CrearCabecera():
    lista = FileFunctions.LeerArchivo(archivoArticulos)
    if not lista:
        linea = "Codigo,Descripcion,Stock"
        FileFunctions.EscribirLineaEnArchivo(archivoArticulos, linea)

def ValidarCodigo():

    codigoInvalido = True

    while(codigoInvalido):
        codigoSinValidar = input("Ingrese el codigo: ")
        if ExpressionFunctions.EsCodigoDeArticuloValido(codigoSinValidar):
            if not CodigoYaExiste(codigoSinValidar):
                codigoInvalido = False
                return codigoSinValidar
            else:
                print("El codigo ingresado ya existe en el archivo")
                print("Por favor intente nuevamente\n")
        else:
            print("El codigo ingresado no posee el formato adecuado")
            print("Por favor intente nuevamente\n")

def CodigoYaExiste(codigo):

    try:
        lista = FileFunctions.LeerArchivo(archivoArticulos)
        for x in lista:
            if codigo in x:
                return True
    except:
        print("Error al intentar leer el archivo")

    return False

def ValidarStock():

    stockInvalido = True

    while(stockInvalido):
        stockSinValidar = input("Ingrese el stock: ")
        if ExpressionFunctions.EsEnteroValido(stockSinValidar):
            stockInvalido = False
            return stockSinValidar
        else:
            print("El stock ingresado no posee el formato adecuado\n")
            print("Por favor intente nuevamente\n\n")

def ObtenerDescripcionPorCodigo(codigoArticulo):
    lista = FileFunctions.LeerArchivo(archivoArticulos)

    for line in lista:
        if codigoArticulo in line:
            return line[1]
    
    return None
