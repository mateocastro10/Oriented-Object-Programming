from ManejadorRepartidores import ManejadorRep
from ManejadorPedidos import ManejadorPed
from Menu import claseMenu
if __name__ == '__main__':
    mr = ManejadorRep()
    mr.test()
    mp = ManejadorPed()
    mp.testped()
    xmenu = claseMenu()
    b = False
    while not b:
        print('-------MENU DE OPCIONES-------')
        print(
            'opcion 1: Dado el identificador de un repartidor, obtener los pedidos pendientes de entrega \nopcion 2: Para cada repartidor, imprimir un listado con los pedidos entregados\nopcion 3:  \n.\nopcion 5:salir')
        op = int(input('seleccione opcion'))
        if op == 0 or op>5:
            print('OPCION INCORRECTA')
        else:
            b = True
            xmenu.opcion(op, mr, mp)
