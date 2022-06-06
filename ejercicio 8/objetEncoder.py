import json
from pathlib import Path
from manejador import Manejador
from personal import Personal 
from personaldeapoyo import PersonaldeApoyo
from docente import Docente
from investigador import Investigador
from docenteinvestigador import DocenteInvestigador
class ObjectEncoder(object):

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='Manejador':
                Personal=d['Personal']
                dPersonal=Personal[0]
                manejador=class_()
                for i in range(len(Personal)):
                    dPersonal=Personal[i]
                    class_name=dPersonal.pop('clase')
                    class_=eval(class_name)
                    atributos=dPersonal['atributos']
                    unPersonal=class_(**atributos)
                    manejador.AgregarAgente(unPersonal)
            return manejador

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)