class Infractor:
    __dni: 0
    __nombre: ''
    __apellido: ''
    __direccion: ''
    __nrocarnet: 0
    __puntaje: 0

    def __init__(self, d, n, a, di, nro, p):
        self.__dni = d
        self.__nombre = n
        self.__apellido = a
        self.__direccion = di
        self.__nrocarnet = nro
        self.__puntaje = p

    def __str__(self):
        return (
            'Apellido:       {}       Nombre:       {}         Dni:      {}\nCarnet:        {}       Direccion:        {}       \nInfracciones\n   Patente            Tipo de Vehiculo       Marca      Importe'.format(
                self.__apellido, self.__nombre, self.__dni, self.__nrocarnet, self.__direccion))

    def modificapuntaje(self):
        self.__puntaje -= 10

    def getdni(self):
        return self.__dni

    def getapellido(self):
        return self.__apellido

    def getnombre(self):
        return self.__nombre

    def getdireccion(self):
        return self.__direccion

    def getcarnet(self):
        return self.__nrocarnet

    def getpuntaje(self):
        return self.__puntaje

    def __lt__(self, other):
        b = False
        if self.__apellido < other.getapellido():
            b = True
        return b