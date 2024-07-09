import csv
from ClasePersona import Persona


class ManejadorPersona:
    __listaPersona = []
    
    def cargarPersona(self):
        archivo = open('Personal-exceptuado.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader,None)
        for linea in reader:
            objeto = Persona(linea[0],linea[1],linea[2],int(linea[3]),linea[4],linea[5],linea[6],linea[7])
            self.__listaPersona.append(objeto)

    def getLista(self):
        return self.__listaPersona
