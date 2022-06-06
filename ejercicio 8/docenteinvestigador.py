from docente import Docente
from investigador import Investigador
class DocenteInvestigador(Docente,Investigador):
    __CategoriaProgramaInvestigacion=None
    __ImporteExtra=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo,categoriaprogramainvestigacion,importeextra):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad,carrera,cargo,catedra,area,tipo)
        self.__CategoriaProgramaInvestigacion=categoriaprogramainvestigacion
        self.__ImporteExtra=importeextra

    def __str__(self):
        return super().__str__()+self.__CategoriaProgramaInvestigacion+self.__ImporteExtra
    def getCategoria(self):
        return self.__CategoriaProgramaInvestigacion
    def getImporte(self):
        return self.__ImporteExtra
    def getSueldo(self):
        if self.__getCargo=='Simple':
            Sueldo1=(self.__SueldoBasico*10)/100
        elif self.__getCargo=='Semiexclusivo':
            Sueldo1=(self.__SueldoBasico*20)/100
        elif self.__getCargo=='Exclusivo':
            Sueldo1=(self.__SueldoBasico*50)/100
        if int(self.__getCategoria)>=1 and int(self.__get)<=10:
            Sueldo2=(self.__SueldoBasico*10)/100
        elif int(self.__getCategoria)>=11 and int(self.__get)<=20:
            Sueldo2=(self.__SueldoBasico*20)/100
        elif int(self.__getCategoria)>=21 and int(self.__get)<=22:
            Sueldo2=(self.__SueldoBasico*30)/100
        Sueldo=Sueldo1+Sueldo2+self.__SueldoBasico
        return Sueldo 
    def setExtra(self,valor):
        self.__ImporteExtra=valor
    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                categoriaprogramainvestigacion=self.__CategoriaProgramaInvestigacion,
                importeextra=self.__ImporteExtra
            )
        )
        return d