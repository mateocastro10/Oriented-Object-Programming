class Pedido:
    __id = 0
    __nro = 0
    __desc = ''
    __cantidad = 0
    __precio = 0
    __estado = ''
    def __init__(self, i, n, d, c, p, e):
        self.__id = i
        self.__nro = n
        self.__desc = d
        self.__cantidad = c
        self.__precio = p
        self.__estado = e

    def getId(self):
        return self.__id

    def getEs(self):
        return self.__estado

    def gettotal(self):
        return int(self.__cantidad * self.__precio)

    def __str__(self):
        return ('{}    {}        {}     {}                    {}'.format(self.__nro, self.__desc, self.__cantidad, self.__precio, (self.__cantidad * self.__precio)))
