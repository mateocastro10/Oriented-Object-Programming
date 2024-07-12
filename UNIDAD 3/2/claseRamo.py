class Ramo:
    __tamaño = ''
    __listaflores = []

    def __init__(self, t):
        if type(t)==str:
            self.__tamaño = t
            self.__listaflores = []
        else:
            print('Error en la creacion del objeto')