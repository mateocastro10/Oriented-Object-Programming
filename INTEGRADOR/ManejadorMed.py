import csv
from claseMed import Medicamento
class ManMed:
    def __init__(self):
        self.__listaMed = []

    def __str__(self):
        s = ''
        for Medicamento in self.__listaMed:
            s += str(Medicamento) + '\n'
        return s

    def agregarMed(self, unMed):
        if type(unMed==Medicamento):
            self.__listaMed.append(unMed)
            print('Medicamento cargado con éxito')
        else:
            print('PARAMETRO INCORRECTO')

    def test(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for fila in reader:
            if bandera:
                '''saltear cabecera '''
                bandera = not bandera
            else:
                idc = int(fila[0])
                idm = int(fila[1])
                n = fila[2]
                m = fila[3]
                p = fila[4]
                c = int(fila[5])
                precio = float(fila[6])
                unMed = Medicamento(idc, idm, n, m, p, c, precio)
                self.agregarMed(unMed)
        archivo.close()

    def devolver(self, x):
        preci = 0.0
        print('Medicamento/monodroga      Presentacion      Cantidad      Precio')
        for i in range(len(self.__listaMed)):
            self.__listaMed[i].buscaid(x)
            preci += self.__listaMed[i].total(x)
        print('Total adeudado: {}'.format(preci))
