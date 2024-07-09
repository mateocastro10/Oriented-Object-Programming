from claseRepartidores import Repartidor
import csv
from operator import attrgetter

class ManejadorRep:
    def __init__(self):
        self.__listaRep = []

    def agregarPlan(self, unRep):
        if (type(unRep)) == Repartidor:
            self.__listaRep.append(unRep)
            print('Repartidor cargado con éxito')
        else:
            print('ERROR DE DATO EN LA CREACION DEL REPARTIDOR')

    def test(self):
        archivo = open('repartidores.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                i = fila[0]
                ap = fila[1]
                nom = fila[2]
                tel = int(fila[3])
                t = fila[4]
                unRep = Repartidor(i, ap, nom, tel, t)
                self.agregarPlan(unRep)
        archivo.close()

    def listado(self, mp):
        lista = mp.getarre()
        i = 0
        while i < len(self.__listaRep):
            print(self.__listaRep[i])
            j = 0
            acum = 0
            while j < len(lista):
                if self.__listaRep[i].getid() == lista[j].getId():
                    if lista[j].getEs() == 'E':
                        print(lista[j])
                        acum += lista[j].gettotal()
                        j += 1
                    else:
                        j += 1
                else:
                    j += 1
            print('                                                                           TOTAL: {}'.format(acum))
            x = (5*acum)/100
            self.__listaRep[i].guard(x)
            print('Comision : {}'.format(self.__listaRep[i].getCom()))
            i += 1

    def rep(self, x, mp):
        i = 0
        lista = mp.getarre()
        j=0
        c=False
        while i < len(self.__listaRep):
            if self.__listaRep[x-1].__eq__(self.__listaRep[i]):
                while j < len(lista):
                    if (lista[j].getEs() == 'E') and ((lista[j].getId == x) or lista[j].getId == (j+1)):
                        c = True
                    else:
                        c = False
                    j += 1
            i += 1
        print(c)
        if c:
            self.__listaRep[x].pop()
            print ('Borrado con éxito')
