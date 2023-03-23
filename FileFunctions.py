
import csv

class FileFunctions:

    @staticmethod
    def LeerArchivo(archivo):
        listaDeRegistros = []
        with open(archivo, "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                listaDeRegistros.append(row)
            return listaDeRegistros

    @staticmethod
    def LeerArchivoCsv(archivo):
        with open(archivo, "r") as file:
            return csv.reader(file)

    @staticmethod
    def EscribirLineaEnArchivo(archivo,linea):
        with open(archivo, "a") as file:
            file.write(linea)

    @staticmethod
    def EscribirListaEnArchivo(archivo,lista):
        with open(archivo, "w", newline='') as file:
            csvwriter = csv.writer(file, delimiter=',')
            for lineaCsv in lista:
                if len(lineaCsv) != 0:
                    csvwriter.writerow(lineaCsv)
