from ManejadorCama import ManCama
from ManejadorMed import ManMed
if __name__ == '__main__':
    mc = ManCama()
    mc.test()
    mm = ManMed()
    mm.test()
    no = input('Ingrese nombre del internado de alta: ')
    ap = input('Ingrese apellido del internado de alta: ')
    x = mc.listar(no, ap)
    mm.devolver(x)
    d = input('ingrese diagnostico')
    mc.diag(d)
