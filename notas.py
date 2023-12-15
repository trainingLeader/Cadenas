import os
alumnos =[]
isActive = True
menu = "1. Registrar Alumno\n2. Registrar Nota\n3. Salir\n:)"
subMenuNotas = ["1. Parciales","2. Quices","3. Trabajos","4. Regresar al menu principal"]
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
            pass
        elif (opMenu == 2):
            pass
        elif (opMenu == 3):
            os.system("cls")
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            os.system("cls")
            print("Opcion invalida")
    os.system("pause")
        