import numpy as np
from claseCama import Cama
import csv


class ManCama:
    def __init__(self):
        self.__arregloCama = np.empty(30, dtype=Cama)

    def agregarCama(self, unaCama, i):
        if (type(unaCama)) == Cama:
            self.__arregloCama[i] = unaCama
            print('Cama cargada con éxito')
            print(self.__arregloCama[i])
        else:
            print('ERROR DE DATO EN LA CREACION DE LA CAMA')

    def __str__(self):
        s = ''
        for Cama in self.__arregloCama:
            s += str(Cama) + '\n'
        return s

    def test(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                i = int(fila[0])
                h = int(fila[1])
                e = (fila[2])
                x = fila[3].split(',')
                n = x[1]
                a = x[0]
                d = fila[4]
                fi = fila[5]
                fa = fila[6]
                unaCama = Cama(i, h, e, n, a, d, fi, fa)
                self.agregarCama(unaCama, i - 1)
        archivo.close()

    def listar(self, no, ap):
        if type(no) and type(ap) == str:
            b = False
            for i in range(len(self.__arregloCama)):
                if self.__arregloCama[i] is not None and b != True:
                    b = self.__arregloCama[i].getCama(no, ap)
                elif b == True and self.__arregloCama[i] is not None:
                    return int(i)
                elif self.__arregloCama[i] is None and b==True:
                    return int(i)
                elif self.__arregloCama[i] is None:
                    print('No se encontró')
                    break

    def diag(self, d):
        for i in range(len(self.__arregloCama)):
            if self.__arregloCama[i] is not None:
                self.__arregloCama[i].listado(d)
            else:
                break
