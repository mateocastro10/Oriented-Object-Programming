import csv
from ClaseOrganismo import Organismo
from ClasePersona import Persona
from ManejadorPersonas import ManejadorPersona


class ManejadorOrganismo:

    def __init__(self):
        self.__listaOrganismos = []

    def cargaOrganismo(self):
        archivo = open('Organismos-del-Estado.csv')
        reader = csv.reader(archivo,delimiter=';')
        next(reader,None)
        for linea in reader:
            objeto = Organismo(linea[0],linea[1],linea[2],linea[3])
            self.__listaOrganismos.append(objeto)

    def mostrarCantidad(self):
        listaPersona = ManejadorPersona()
        lista = listaPersona.getLista()
        for organizacion in self.__listaOrganismos:
            contador1 = 0
            contador2 = 0
            for persona in lista:
                if organizacion.getNombre()==persona.getNomO():
                    if persona.getFactor()=='Edad':
                        contador1+=1
                    else:
                        contador2+=1
            print('Organizacion: -{}- tiene -{}- personas exeptuadas por edad y -{}- personas exceptuadas por enfermedad'.format(organizacion.getNombre(),contador1,contador2))

    def listado(self,nombre):
        i:int = 0
        bandera = False
        listaOrdenada = []
        listaPersona = ManejadorPersona()
        lista = listaPersona.getLista()
        while i < len(self.__listaOrganismos) and bandera == False:
            if self.__listaOrganismos[i].getNombre()==nombre:
                print('El nombre coindice'.center(30,'-'))
                for objeto in lista:
                    if self.__listaOrganismos[i].getNombre()==objeto.getNomO():
                        if objeto.getEdad() < 60:
                            listaOrdenada.append(objeto)
                bandera = True
            i+=1
        listaOrdenada.sort(key=lambda x:x.getApellido())
        for objeto in listaOrdenada:
            print(objeto)
