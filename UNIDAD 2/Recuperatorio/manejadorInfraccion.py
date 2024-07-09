from claseInfraccion import Infraccion
import numpy as np
import csv


class ManejadorInfraccion:
    __listaInfraccion = []
    __cantidad: 0
    __dimension: 0

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 1
        self.__listaInfraccion = np.empty(1, dtype=Infraccion)

    def agregar(self, unaInfraccion):
        if (type(unaInfraccion)) == Infraccion:
            if self.__dimension == self.__cantidad:
                self.__dimension += 1
                self.__listaInfraccion.resize(self.__dimension)
            self.__listaInfraccion[self.__cantidad] = unaInfraccion
            self.__cantidad += 1
            print('Infraccion cargada con éxito')
        else:
            print('ERROR DE DATO EN LA CREACION DE LA INFRACCION')

    def testinfracciones(self, mp):
        archivo = open('infracciones.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        lista = mp.getlista()
        j = 0
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                k = 0
                while k < len(lista):
                    if int(fila[0]) == lista[k].getdni():
                        unaInfraccion = Infraccion(int(fila[0]), fila[1], fila[2], fila[3], fila[4], fila[5], int(fila[6]), fila[7])
                        self.agregar(unaInfraccion)
                        lista[k].modificapuntaje()
                    k += 1
                j += 1

    def getdescuento(self, c, acum):
        s = 0
        if c == 1:
            s = acum / 2
        return s

    def listado(self, dni, manInfractor):
        lista = manInfractor.getlista()
        c = 0
        acum = 0
        i = 0
        j = 0
        k = 0
        band = True
        while i < (len(lista)) and band:
            if lista[i].getdni() == dni:
                print(
                    'Datos del Infractor \nApellido: {}             Nombre: {}            DNI: {}\nCarnet: {}             Direccion: {}'.format(
                        lista[i].getapellido(), lista[i].getnombre(), lista[i].getdni(), lista[i].getcarnet(),
                        lista[i].getdireccion()))
                print('Patente       Tipo de vehículo         Marca         Descripción         Importe \nInfracciones')
                band = False
                while j < self.__cantidad:
                    if self.__listaInfraccion[j].getdni() == dni and self.__listaInfraccion[j].getestado() == 'N':
                        while k < self.__cantidad:
                            if self.__listaInfraccion[j] == self.__listaInfraccion[k]:
                                c += 1
                            k += 1
                        acum += self.__listaInfraccion[j].getimporte()
                        print('{}       {}              {}           {}           {}'.format(
                            self.__listaInfraccion[j].getpatente(), self.__listaInfraccion[j].gettipo(),
                            self.__listaInfraccion[j].getmarca(), self.__listaInfraccion[j].getdescripcion(),
                            self.__listaInfraccion[j].getimporte()))
                    j += 1
            i += 1
        print('SUBTOTAL: {}'.format(acum))
        print('DESCUENTO: {}'.format(self.getdescuento(c, acum)))
        print('TOTAL: {}'.format(acum - self.getdescuento(c, acum)))

    def pagas(self, xdni, xpatente):
        i = 0
        while i < self.__cantidad:
            if self.__listaInfraccion[i].getdni() == xdni and self.__listaInfraccion[i].getpatente() == xpatente and \
                    self.__listaInfraccion[i].getestado() == 'N':
                self.__listaInfraccion[i].modificaestado()
            print(self.__listaInfraccion[i])
            i += 1

    def reincidente(self, dni):
        k, j, c = 0, 0, 0
        while j < self.__cantidad:
            if self.__listaInfraccion[j].getdni() == dni:
                while k < self.__cantidad:
                    if self.__listaInfraccion[j] == self.__listaInfraccion[k]:
                        c += 1
                    k += 1
            j += 1
        print('El infractor cometio {} veces la misma infraccion'.format(c))
        if c > 2:
            print('Es reincidente')
        else:
            print('No es reincidente')
