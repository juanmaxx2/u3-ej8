from manejador import Manejador
from menu import Menu
from objetEncoder import ObjectEncoder
if __name__=='__main__':
    unManejador=Manejador()
    jsonF=ObjectEncoder()
    diccionario=jsonF.leerJSONArchivo('personal.json')
    unManejador=jsonF.decodificarDiccionario(diccionario)
    unMenu=Menu()
    unMenu.Iniciar(unManejador,jsonF)