class Persona:
    __apellido:str = ""
    __nombre:str = ""
    __direccion:str = ""
    __dni:str = ""
    __edad:int = ""
    __telofono:str = ""
    __factor:str = ""
    __nomOrganismo:str = ""

    def __init__(self,ape:str,nom:str,dni:str,edad:int,dir:str,tel:str,factor:str,nomO:str):
        self.__apellido = ape
        self.__nombre = nom
        self.__direccion = dir
        self.__dni = dni
        self.__edad = edad
        self.__telofono = tel
        self.__factor = factor
        self.__nomOrganismo = nomO

    def getNomO(self):
        return self.__nomOrganismo

    def getFactor(self):
        return self.__factor
    
    def getEdad(self):
        return self.__edad
    
    def getApellido(self):
        return self.__apellido
    
    def __str__(self):
        return ('A: {} N: {} DNI: {} Edad: {} '.format(self.__apellido,self.__nombre,self.__dni,self.__edad))
    
    def __lt__(self,otro):
        return self.__edad < otro