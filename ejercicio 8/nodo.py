class Nodo:
    __Personal=None
    __Siguiente=None

    def __init__(self, personal):
        self.__Personal=personal
        self.__Siguiente=None

    def getSiguiente(self):
        return self.__Siguiente
        
    def getDato(self):
        return self.__Personal

    def setSiguiente(self, Siguiente):
        self.__Siguiente=Siguiente
    
    def setelemento(self, personal):
        self.__Personal = personal