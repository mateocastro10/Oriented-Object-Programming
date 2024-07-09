from manejadorInfraccion import ManejadorInfraccion
from manejadorInfractor import ManejadorInfractor
from claseMenu import menu
if __name__ == '__main__':
    manInfraccion = ManejadorInfraccion()
    manInfractor = ManejadorInfractor()
    manInfractor.testinfractores()
    manInfraccion.testinfracciones(manInfractor)
    xmenu = menu()
    b = False
    while not b:
        print('-------MENU DE OPCIONES-------')
        print('opcion 1\nopcion 2\nopcion 3:\nopcion 4:\nopcion 5:salir')
        op = int(input('seleccione opcion'))
        if op == 0 or op > 5:
            print('OPCION INCORRECTA')
        else:
            b = True
            xmenu.opcion(op, manInfractor, manInfraccion)