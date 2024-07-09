class claseMenu:
    __op = 0

    def __init__(self):
        self.__op = None

    def opcion(self, op, mr=None, mp=None):
        if op == 1:
            self.opcion1(mp)
        elif op == 2:
            self.opcion2(mr, mp)
        elif op == 3:
            self.opcion3(mr, mp)
        elif op == 4:
            self.opcion4(mp)
        elif op == 5:
            self.salir()

    def salir(self):
        print('Usted salio del programa')

    def opcion1(self, mp):
        dato = int(input('Ingrese identificador de Repartidor'))
        mp.pendiente(dato)
    def opcion2(self, mr, mp):
        mr.listado(mp)
    def opcion3(self, mr, mp):
        id = int(input('Ingrese identificador de Repartidor'))
        mr.rep(id, mp)
