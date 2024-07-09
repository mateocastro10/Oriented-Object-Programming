from clasePedidos import Pedido
import numpy as np
import csv


class ManejadorPed:
    def __init__(self):
        self.__pedidos = np.empty(16, dtype=Pedido)

    def agregarPed(self, unPedido, i):
        if (type(unPedido)) == Pedido:
            self.__pedidos[i] = unPedido
        else:
            print('ERROR DE DATO EN LA CREACION DEL PEDIDO')

    def testped(self):
        archivo = open('pedidos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        j = 0
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                i = int(fila[0])
                n = int(fila[1])
                d = fila[2]
                c = int(fila[3])
                p = int(fila[4])
                e = fila[5]
                unPedido = Pedido(i, n, d, c, p, e)
                self.agregarPed(unPedido, j)
                j += 1
        archivo.close()

    def getarre(self):
        return self.__pedidos

    def pendiente(self, op):
        c = 0
        while c < len(self.__pedidos):
            if self.__pedidos[c].getId() == op:
                if self.__pedidos[c].getEs() == 'N':
                    print(self.__pedidos[c])
                    c = c + 1
                else:
                    c += 1
            else:
                c = c + 1

