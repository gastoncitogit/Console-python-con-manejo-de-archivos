from FileFunctions import FileFunctions
import AbmArticulos 

def OrdenarArchivoVentas(lista):
    for idx in range(1,len(lista)):
        evaluado = idx
        for x in range(idx + 1, len(lista)):
            if lista[evaluado] > lista[x]:
                evaluado = x
        lista[idx], lista[evaluado] = lista[evaluado], lista[idx]

def ObtenerSiguienteRegistro(lista):
    # Devuelve el siguiente registro o None si no hay más
    try:
        return next(lista)
    except:
        return None

def AparearArchivos(archivoVentas):

    # Inicialización
    listaDeRegistrosDeVentas = FileFunctions.LeerArchivo(archivoVentas)
    listaDeRegistrosDeVentas = iter(listaDeRegistrosDeVentas)

    ObtenerSiguienteRegistro(listaDeRegistrosDeVentas)
    registroDeVenta = ObtenerSiguienteRegistro(listaDeRegistrosDeVentas)
    total_general = 0

    while registroDeVenta:
        #Inicialización para el bucle de sucursal
        sucursal = registroDeVenta[0]
        total_sucursal = 0
        print ("Sucursal: ",sucursal)

        while registroDeVenta and registroDeVenta[0] == sucursal:
            # Inicialización para el bucle de articulo
            articulo = registroDeVenta[1]
            total_articulo = 0
            print("\tArticulo: ", AbmArticulos.ObtenerDescripcionPorCodigo(articulo))

            while registroDeVenta and registroDeVenta[0] == sucursal and registroDeVenta[1] == articulo:
                vendedor, importe = registroDeVenta[2], registroDeVenta[3]
                print("\t\tVendedor: ", vendedor, "- Subtotal Vendedor: ", str(importe))
                total_articulo += float(importe)
                # Siguiente registro
                registroDeVenta = ObtenerSiguienteRegistro(listaDeRegistrosDeVentas)

            # Final del bucle por Vendedor
            print("\t\t\tTotal Articulo: ", total_articulo)
            total_sucursal += total_articulo

        # Final del bucle de Sucursal
        print ("\t\t\t\tTotal Sucursal: ", total_sucursal)
        total_general += total_sucursal

    # Final del bucle principal
    print("\t\t\t\t\tTotal General: ", total_general)
    

def ProcesarArchivo():

    archivoVentas = "Input\Ventas.csv" 
    try:

        lista = FileFunctions.LeerArchivo(archivoVentas)
        OrdenarArchivoVentas(lista)
        FileFunctions.EscribirListaEnArchivo(archivoVentas, lista)
        AparearArchivos(archivoVentas)
    except:
        print("Ocurrio un error al intentar generar el reporte")