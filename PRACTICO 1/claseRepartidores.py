class Repartidor:
    __id = ''
    __apellido = ''
    __nombre = ''
    __tel = 0
    __tmovilidad = ''
    __comision = 0

    def __init__(self, i, ap, nom, tel, t):
        self.__id = i
        self.__apellido = ap
        self.__nombre = nom
        self.__tel = tel
        self.__tmovilidad = t
        self.__comision = 0

    def __str__(self):
        return (
            'Apellido:       {}       Nombre:       {}       \nTelefono:        {}       Tipo Movilidad:        {}       \nNúmero de Pedido   Descripción   Cantidad   Precio Unitario   Total'.format(
                self.__apellido, self.__nombre, self.__tel, self.__tmovilidad))

    def getid(self):
        j = int(self.__id)
        return j

    def getNo(self):
        return self.__nombre

    def getAp(self):
        return self.__apellido

    def getTe(self):
        return self.__tel

    def getTM(self):
        return self.__tmovilidad

    def getCom(self):
        return self.__comision

    def guard(self, x):
        self.__comision = x

    def __eq__(self, other):
        b = False
        if (self.__nombre == other.__nombre) and (self.__apellido == other.__apellido) and (self.__tel == other.__tel):
            b = True
        print('VALOR DE B :::::: {}'.format(b))
        return b
