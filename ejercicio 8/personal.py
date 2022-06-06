import abc
from abc import ABC
class Personal(ABC):
    __Cuil=None
    __Apellido=None
    __Nombre=None
    __SueldoBasico=None
    __Antiguedad=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,area="",tipo=""):
        self.__Cuil=cuil
        self.__Apellido=apellido
        self.__Nombre=nombre
        self.__SueldoBasico=sueldobasico
        self.__Antiguedad=antiguedad
    
    def __str__(self):
        return '/n'+self.__Cuil+self.__Apellido+self.__Nombre+str(self.__SueldoBasico)+str(self.__Antiguedad)
    def getCuil(self):
        return self.__Cuil
    def getApellido(self):
        return self.__Apellido
    def getNombre(self):
        return self.__Nombre
    def getSueldoBasico(self):
        return self.__SueldoBasico
    def getAntiguedad(self):
        return self.__Antiguedad
    
    @abc.abstractmethod
    def gettipo(self):
        pass
    @abc.abstractmethod
    def getSueldo(self):
        pass
    def setSueldoBasico(self,valor):
        self.__SueldoBasico=valor
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                cuil=self.__Cuil,
                apellido=self.__Apellido,
                nombre=self.__Nombre,
                sueldobasico=self.__SueldoBasico,
                antiguedad=self.__Antiguedad
            )
        )
        return d