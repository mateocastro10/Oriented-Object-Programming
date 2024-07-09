class Medicamento:
    __idcama = 0
    __idmed = 0
    __nom = ''
    __monodroga = ''
    __presentacion = ''
    __cant = 0
    __precio = 0.0

    def __init__(self, idc, idm, n, m, p, c, precio):
        self.__idcama = idc
        self.__idmed = idm
        self.__nom = n
        self.__monodroga = m
        self.__presentacion = p
        self.__cant = c
        self.__precio = precio

    def __str__(self):
        s = str(self.__id) + ' ' + str( self.__nombre) +' ' + str(self.__apellido) + ' ' + str(self.__hab) + ' ' + str(self.__diagnostico) + '\n'
        return s

    def total(self, x):
        if x==self.__idcama:
            return self.__precio
        else:
            return 0

    def buscaid(self, x):
        if x == self.__idcama:
            print('{}'.format(self.__nom) + '/' + '{}'.format(self.__monodroga) + '           {}'.format(self.__presentacion) + '        {}'.format(self.__cant) + '       {}'.format(self.__precio))
