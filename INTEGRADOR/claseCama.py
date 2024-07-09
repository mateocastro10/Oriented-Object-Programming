
class Cama:
    __id = 0
    __hab = 0
    __estado = False
    __nombre = ''
    __apellido = ''
    __diagnostico = ''
    __fechai = ''
    __fechaalta = ''

    def __init__(self, i, h, e, n, a, d, fi, fa):
        self.__id = i
        self.__hab = h
        self.__estado = e
        self.__nombre = n
        self.__apellido = a
        self.__diagnostico = d
        self.__fechai = fi
        self.__fechaalta = fa

    def __str__(self):
        s = str(self.__id) + ' ' + str( self.__nombre) +' ' + str(self.__apellido) + ' ' + str(self.__hab) + ' ' + str(self.__diagnostico) + '\n'
        return s

    def getCama(self, no, ap):
        if (no != self.__nombre) and (ap != self.__apellido):
            return False
        else:
            print('Paciente: {} {}'.format(self.__nombre, self.__apellido) + '  Cama: {}     Habitacion: {}'. format(self.__id, self.__hab))
            print('Diagnostico: {}           Fecha internacion: {}'.format(self.__diagnostico, self.__fechai)   + '\n' + 'Fecha de Alta: 9/5/2022')
            return True
    def listado(self, dia):
        if self.__diagnostico == dia:
            print(self.__nombre)
