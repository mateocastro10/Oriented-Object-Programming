class Infraccion:
    __dni: 0
    __patente: ''
    __tipo: ''
    __marca: ''
    __fecha: ''
    __desc: ''
    __importe: 0
    __estado: ''

    def __init__(self, d, p, t, m, f, desc, i, e):
        self.__dni = d
        self.__patente = p
        self.__tipo = t
        self.__marca = m
        self.__fecha = f
        self.__desc = desc
        self.__importe = i
        self.__estado = e

    def __str__(self):
        return 'Patente:{}       Marca:{}         Dni:{}\nEstado:{}       Descripcion:{}'.format(self.__patente, self.__marca, self.__dni, self.__estado, self.__desc)

    def getdni(self):
        return self.__dni

    def getpatente(self):
        return self.__patente

    def getmarca(self):
        return self.__marca

    def getdescripcion(self):
        return self.__desc

    def gettipo(self):
        return self.__tipo

    def getimporte(self):
        return self.__importe

    def getdesc(self):
        return self.__desc

    def getestado(self):
        return self.__estado

    def modificaestado(self):
        self.__estado = 'P'

    def __eq__(self, other):
        if type(other) == Infraccion:
            b = False
            if self.__dni == other.getdni() and self.__patente == other.getpatente() and self.__desc == other.getdesc():
                b = True
            return b