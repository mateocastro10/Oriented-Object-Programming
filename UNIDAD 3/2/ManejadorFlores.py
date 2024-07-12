from claseFlor import Flor
import numpy as np

class ManejadorF:

    def __init__(self):
    __arregloflores = np.empty(12, dtype=Cama)

    def test(self):
        archivo = open('flores.csv')
        reader = csv.reader(archivo, delimiter=';')
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
