class Organismo:
    __nombre:str = ""
    __domicilio:str = ""
    __localidad:str = ""
    __telefono:str = ""

    def __init__(self,nombre:str,domicilio:str,localidad:str,telefono:str):
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__localidad = localidad
        self.__telefono = telefono
    
    def getNombre(self):
        return self.__nombre
