import AbmArticulos
import AbmVentas
import Reporte

archivoVentas = "Input\Ventas.csv"
archivoArticulos = "Input\Articulos.csv"

def Menu():
    while True:
        print("1) ABM Articulos")
        print("2) ABM Ventas")
        print("3) Listado de articulos")
        print("4) Listado de ventas")
        print("5) Reporte total")
        print("6) Salir")
        choice = input("Seleccione una opcion: ")

        choice = choice.strip()
        if(choice == "1"):
            print()
            AbmArticulos.SubMenuAbmArticulos()            
        elif(choice == "2"):
            print()
            AbmVentas.SubMenuAbmVentas()
        elif(choice == "3"):
            AbmArticulos.TraerTodos()
        elif(choice == "4"):
            AbmVentas.TraerTodos()
        elif(choice == "5"):   
            Reporte.ProcesarArchivo()            
        elif(choice == "6"):
            break
        else:
            print("Opcion invalida. Seleccione una opcion del 1 al 5")

        print("-----------------------------------------------\n")

Menu()



                

    

