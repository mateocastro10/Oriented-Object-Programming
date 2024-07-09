from ManejadorOrganismos import ManejadorOrganismo
from ManejadorPersonas import ManejadorPersona


if __name__ == '__main__':
    manO = ManejadorOrganismo()
    manP = ManejadorPersona()
    manO.cargaOrganismo()
    manP.cargarPersona()
    manO.mostrarCantidad()
    nombre = input('Ingrese nombre de una Organizacion: ')
    manO.listado(nombre)