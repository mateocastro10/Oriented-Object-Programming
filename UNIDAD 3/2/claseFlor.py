class Flor:
    __numero = 0
    __nombre = ''
    __color = ''
    __descripcion = ''

    def __init__(self, n, c, d):
        if type(n) == str and type(c) == str and type(d) == str:
            self.__nombre = n
            self.__color = c
            self.__descripcion = d
        else:
            print('No se pudo cargar el objeto')
