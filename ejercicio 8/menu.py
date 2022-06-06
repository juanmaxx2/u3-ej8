class Menu:
    __opcion=None

    def __init__(self):
        pass
        self.__opcion=None

    def Iniciar(self,unManejador,encoder):
        print('Iniciar sesion:')
        usuario=input('Ingrese usuario:')
        contrasenia=input('Ingrese contrasenia:')
        if usuario=='uDirector' and contrasenia=='ufC77#!1':
            while  bandera:
                print('1.Modificar el sueldo basico de un empleado')
                print('2.Modificar el importe extra de un Docente Investigador')
                print('3.Modificar el porcentaje por cargo')
                print('4.Modificar el porcentaje por categoria')
                print('5.Salir')
                opcion = int(input('Ingrese una opcion:'))
                if opcion == 1:
                    cuil=input('Ingrese el cuil:')
                    basico=input('Ingrese el nuevo sueldo basico:')
                    unManejador.ActualizarSueldoBasico(cuil,basico)
                elif opcion == 2:
                    cuil=input('Ingrese el cuil de un docente investigador:')
                    ImporteExtra=input('Ingrese el nuevo importe extra:')
                    unManejador.ActualizarImporteExtra(cuil,ImporteExtra)
                elif opcion == 3:
                    porcentajecargo=input('Ingrese el nuevo porcentaje:')
                    unManejador.ActualizarPorcentajeporcargo(porcentajecargo)
                elif opcion == 4:
                    porcentajecate=input('Ingrese el nuevo porcentaje:')
                    unManejador.ActualizarPorcentajeporcategoría(porcentajecate)
                elif opcion == 5:
                    bandera = False
                else:
                    print('ERROR: Opcion ingresda incorrecta!')
        elif usuario=='uTesoreso' and contrasenia=='ag@74ck':
            cuil=0
            while cuil!='-1':
                cuil=input('Ingrese el cuil(-1 para salir):')
                unManejador.GastosSueldosxEmpleados(cuil)
        while self.__opcion!='9':
            print('\n1.Insertar Agente.')
            print('2.Agregar Agente.')
            print('3.Mostrar tipo de agente en una posicion.')
            print('4.Mostrar Nombre de Docentes Investigadores que trabajan en una carrera.')
            print('5.Buscar docentes investigadores y investigadores pertenecientes a un area. ')
            print('6.Mostrar datos de los agentes.')
            print('7.Mostrar docentes investigadores por categoria.')
            print('8.Guardar los datos de los agentes.')
            print('9.Salir')
            self.__opcion=input('\nIngrese la opcion a realizar:')
            
            if int(self.__opcion)>=1 and int(self.__opcion)<=9:

                if self.__opcion=='1':
                    pos=input('\nIngrese la posicion en la que quiere ingresar el agente')
                    agente=unManejador.Iniciar()
                    unManejador.InsertarAgente(agente,pos)
                elif self.__opcion=='2':
                    agente=unManejador.Iniciar()
                    unManejador.AgregarAgente(agente)
                elif self.__opcion=='3':
                    pos=input('\nIngrese el posicion a mostrar el tipo de agente:')
                    print(type(unManejador))
                    unManejador.MostrarTipo(pos)
                elif self.__opcion=='4':
                    carrera=input('\nIngrese el nombre de una carrera:')
                    unManejador.DICarrera(carrera)
                elif self.__opcion=='5':
                    area=input('\nIngrese el area a buscar:')
                    unManejador.ContarxArea(area)
                elif self.__opcion=='6':
                    unManejador.Mostrar()
                elif self.__opcion=='7':
                    categoria=input('\nIngrese la categoria:')
                    unManejador.MostrarCategoria(categoria)
                elif self.__opcion=='8':
                    d=unManejador.toJSON()
                    encoder.guardarJSONArchivo(d,'personal.json')
                    print('Archivo guardado')
            else:print('Opcion incorrecta')
