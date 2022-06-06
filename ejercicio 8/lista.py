from personal import Personal
from docente import Docente
from investigador import Investigador
from personaldeapoyo import PersonaldeApoyo
from docenteinvestigador import DocenteInvestigador
from nodo import Nodo
class Lista:
    __Comienzo=None
    __Actual=None
    __Indice=0
    __Tope=0

    def __init__(self):
        self.__Comienzo=None
        self.__Actual=None
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__Indice==self.__Tope:
            self.__Actual=self.__Comienzo
            self.__Indice=0
            raise StopIteration
        else:
            self.__Indice+=1
            dato = self.__Actual.getDato()
            self.__Actual=self.__Actual.getSiguiente()
            return dato
    
    def getComienzo(self):
        return self.__Comienzo

    def AgregarPersonal(self,personal):
        nodo=Nodo(personal)
        nodo.setSiguiente(self.__Comienzo)
        self.__Comienzo=nodo
        self.__Actual=nodo
        self.__Tope+=1
        print('\nEl personal se agrego')

    def Insertar(self,personal,pos):
        if isinstance(personal,Personal):
            aux=self.__Comienzo
            i=0
            encontrar=False
            ant=aux
            if pos>0 and pos<=self.__tope:
                if i==pos-1:
                    if aux==None:
                        self.AgregarPersonal(personal)
                    else:
                        nodo=Nodo(personal)
                        nodo.setSiguiente(aux)
                        aux.setSiguiente(aux.getSiguiente())
                        self.__Comienzo=nodo
                        self.__Actual=nodo
                        self.__tope+=1
                else:
                    while aux!=None and not encontrar:
                        if i==pos-1:
                            encontrar=True
                            nodo=nodo(personal)
                            ant.setSiguiente(nodo)
                            nodo.setSiguiente(aux)
                            self.__tope+=1
                            print('\nEl personal se agrego a la posicion: {}'.format(pos))
                        else:
                            ant=aux
                            aux=aux.getSiguiente()
                            i+=1
            else: print('La posicion ingresada es invalida')

    def MostrarTipo(self,pos):
        aux=self.__Comienzo
        i=0 
        encontrar=False
        while int(pos)>0 and i<=self.__Tope and encontrar==False:
            if i==int(pos)-1:
                dato=aux.getDato()
                encontrar=True
            else:
                aux.getSiguiente()
                i+=1
        if encontrar==True:
            if isinstance(dato,Docente):
                print('Es un Docente')
            elif isinstance(dato,Investigador):
                print('Es una Investigador')
            elif isinstance(dato,PersonaldeApoyo):
                print('Es un PersonaldeApoyo')
            elif isinstance(dato,DocenteInvestigador):
                print('Es un Docente Investigador')
        else:print('No se encontro la posicion')
