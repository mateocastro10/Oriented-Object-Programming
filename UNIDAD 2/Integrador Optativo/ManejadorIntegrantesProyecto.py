from claseIntegrante import Integrante
import numpy as np
import csv

class ManejadorInt:
    def __init__(self):
        self.__integrantes = np.empty(11, dtype=Integrante)

    def agregarInt(self, unIntegrante, i):
        if(type(unIntegrante)) == Integrante:
            self.__integrantes[i] = unIntegrante
            print('Integrante cargado con éxito')
        else:
            print('ERROR DE DATO EN LA CREACION DEL INTEGRANTE')

    def testint(self):
        archivo = open('integrantesProyecto.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        j = 0
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                i = fila[0]
                an = fila[1]
                d = int(fila[2])
                c = fila[3]
                r = fila[4]
                unIntegrante = Integrante(i, an, d, c, r)
                self.agregarInt(unIntegrante, j)
                j += 1
        archivo.close()

    def
