class menu:
    __op = 0

    def __init__(self):
        self.__op = None

    def opcion(self, op, manInfractor=None, manInfraccion=None):
        if op == 1:
            self.opcion1(manInfractor, manInfraccion)
        elif op == 2:
            self.opcion2(manInfraccion)
        elif op == 3:
            self.opcion3(manInfraccion)
        elif op == 4:
            self.opcion4(manInfractor)
        elif op == 5:
            self.salir()

    def salir(self):
        print('Usted salio del programa')

    def opcion1(self, manInfractor, manInfraccion):
        dato = int(input('Ingrese dni de Infractor'))
        manInfraccion.listado(dato, manInfractor)

    def opcion2(self, manInfraccion):
        xdni = int(input('Ingrese dni'))
        xpatente = (input('Ingrese patente'))
        manInfraccion.pagas(xdni, xpatente)

    def opcion3(self, manInfraccion):
        dni = int(input('Ingrese dni de Infractor'))
        manInfraccion.reincidente(dni)

    def opcion4(self, manInfractor):
        manInfractor.puntaje()
