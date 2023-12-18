"""
PROGRAMA PARA CALCULAR LAS NOTAS DE N ESTUDIANTES..
"""
import os
alumnos =[]
isActive = True
menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Buscar estudiante\n4. Salir\n:)"
subMenuNotas = ["Parciales","Quices","Trabajos","Regresar al menu principal"]
opMenu=0
while (isActive) :
    os.system("cls")
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de de ingreso")
        os.system("pause")
    else:
        if (opMenu == 1):
            rta = "S"
            while (rta in ["S","s"]):
                codigo = input("Ingrese el Codigo del Estudiante : ")
                nombre = input("Ingrese el Nombre del Estudiante : ")
                edad = int(input(f"Ingrese la edad del Estudiante :  {nombre}"))
                alumno = [codigo,nombre,edad,[],[],[]]
                alumnos.append(alumno)
                os.system("pause")
                rta = input("Desea registrar otro Alumno S(si) o N(No)").upper()
        elif (opMenu == 2):
            opNotas = 0
            isActiveGrades = True
            while (isActiveGrades):
                os.system("cls")
                for i,item in enumerate(subMenuNotas):
                    print(f"{i+1}. {item}")

                try:
                    opNotas = int(input(":)"))
                except ValueError:
                    print("Error en el dato de de ingreso")
                    os.system("pause")
                else:                    
                    if (opNotas == 1):
                        rta = "S"
                        isAddGrades = True
                        codigo = input("Ingrese el codigo del Estudiante: ")
                        for item in alumnos:
                            if codigo in item:
                                indice=alumnos.index(item)
                        while isAddGrades:
                            while (rta in ["S","s"]):
                                nota=float(input("Ingrese la nota del parcial: "))
                                alumnos[indice][3].append(nota)
                                print(alumnos)
                                os.system("pause")
                                rta = input("Desea registrar otro parcial S(si) o N(No)").upper()
                            if bool(input("Desea registrar otro estudiante S(si) o Enter(No)")):
                                codigo = input("Ingrese el codigo del Estudiante: ")
                                rta = "S"
                                for item in alumnos:
                                    if codigo in item:
                                        indice=alumnos.index(item)
                                isAddGrades = bool(input("Desea iniciar con el registro S(si) o Enter(No)"))                           
                    elif (opNotas == 2):
                        rta = "S"
                        isAddGrades = True
                        codigo = input("Ingrese el codigo del Estudiante: ")
                        for item in alumnos:
                            if codigo in item:
                                indice=alumnos.index(item)
                        while isAddGrades:
                            while (rta in ["S","s"]):
                                nota=float(input("Ingrese la nota del quiz: "))
                                alumnos[indice][4].append(nota)
                                print(alumnos)
                                os.system("pause")
                                rta = input("Desea registrar otro quiz S(si) o N(No)").upper()
                            if bool(input("Desea registrar otro estudiante S(si) o Enter(No)")):
                                codigo = input("Ingrese el codigo del Estudiante: ")
                                rta = "S"
                                for item in alumnos:
                                    if codigo in item:
                                        indice=alumnos.index(item)
                                isAddGrades = bool(input("Desea iniciar con el registro S(si) o Enter(No)")) 
                    elif (opNotas == 3):
                        rta = "S"
                        isAddGrades = True
                        codigo = input("Ingrese el codigo del Estudiante: ")
                        for item in alumnos:
                            if codigo in item:
                                indice=alumnos.index(item)
                        while isAddGrades:
                            while (rta in ["S","s"]):
                                nota=float(input("Ingrese la nota del trabajo: "))
                                alumnos[indice][4].append(nota)
                                print(alumnos)
                                os.system("pause")
                                rta = input("Desea registrar otro trabajo S(si) o N(No)").upper()
                            if bool(input("Desea registrar otro estudiante S(si) o Enter(No)")):
                                codigo = input("Ingrese el codigo del Estudiante: ")
                                rta = "S"
                                for item in alumnos:
                                    if codigo in item:
                                        indice=alumnos.index(item)
                                isAddGrades = bool(input("Desea iniciar con el registro S(si) o Enter(No)")) 

                    elif (opNotas == 4):
                        isActiveGrades = False
                    else:
                        pass
        elif (opMenu == 3):
            codigo = input("Ingrese el codigo del Estudiante: ")

            for item in alumnos:
                if codigo in item:
                    print(item)
            os.system("pause")
        elif (opMenu == 4):
            os.system("cls")
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            os.system("cls")
            print("Opcion invalida")
    os.system("pause")
        