from claseProyecto import Proyecto
import csv
class Manejador:

    def __init__(self):
        self.__lista = []

    def agregarProyecto(self, unProyecto):
        if(type(unProyecto)) == Proyecto:
            self.__lista.append(unProyecto)
            print('Proyecto cargado con éxito')
        else:
            print('ERROR DE DATO EN LA CREACION DEL PROYECTO')

    def test(self):
        archivo = open('proyectos.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                i = fila[0]
                t = fila[1]
                p = fila[2]
                unProyecto = Proyecto(i, t, p)
                self.agregarProyecto(unProyecto)
        archivo.close()
