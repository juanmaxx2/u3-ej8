from personal import Personal
class PersonaldeApoyo(Personal):
    __Categoria=None

    def __init__(self,cuil,apellido,nombre,sueldobasico,antiguedad,categoria):
        super().__init__(cuil,apellido,nombre,sueldobasico,antiguedad)
        self.__Categoria=categoria

    def __str__(self):
        return super().__str__()+self.__Categoria
    def getCategoria(self):
        return self.__Categoria
    def getSueldo(self):
        return self.__SueldoBasico

    def getPorcentajecategoria(self,opcion,nuevoporcentaje):
        if opcion=='1':
            PersonaldeApoyo.setCategoria1(nuevoporcentaje)
        if opcion=='2':
            PersonaldeApoyo.setCategoria11(nuevoporcentaje)
        if opcion=='3':
            PersonaldeApoyo.setCategoria21(nuevoporcentaje)

    
    @classmethod
    def getCategoria1(cls):
        return cls.porcentajeCategoria1
    @classmethod
    def getCategoria11(cls):
        return cls.porcentajeCategoria11
    @classmethod
    def getCategoria21(cls):
        return cls.porcentajeCategoria21
    @classmethod
    def setCategoria1(cls,porcentaje):
        cls.porcentajeCategoria1=porcentaje
    @classmethod
    def setCategoria11(cls,porcentaje):
        cls.porcentajeCategoria11=porcentaje
    @classmethod
    def setCategoria21(cls,porcentaje):
        cls.porcentajeCategoria21=porcentaje 

    def toJSON(self):
        d=dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                categoria=self.__Categoria
            )
        )
        return d
