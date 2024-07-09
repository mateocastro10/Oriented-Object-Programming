import csv
from claseInfractor import Infractor


class ManejadorInfractor:
    __listainfractores = []

    def __init__(self):
        self.__listainfractores = []

    def agregarInfractor(self, unInfractor):
        if type(unInfractor) == Infractor:
            self.__listainfractores.append(unInfractor)
            print('Infractor cargado con exito')
        else:
            print('Error en la creacion')

    def testinfractores(self):
        archivo = open('infractores.csv')
        reader = csv.reader(archivo, delimiter=';')
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                unInfractor = Infractor(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                self.agregarInfractor(unInfractor)
        archivo.close()

    def getlista(self):
        return self.__listainfractores

    def puntaje(self):
        i = 0
        lista = sorted(self.__listainfractores)
        while i < len(lista):
            if lista[i].getpuntaje() < 1:
                print(lista[i].getpuntaje())
                print('Apellido: {}    Nombre: {}'.format(lista[i].getapellido(), lista[i].getnombre()))
            i += 1