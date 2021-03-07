import os
from lstCircular import *
def MenuPrincipal():
    print("Bienvenido")

    try:

        a=0
        while a<=6:
            a=0
            borrar()
            menu = Lista()
            menu.agregar("           ╔══════════════════════════════════╗")
            menu.agregar("           ║          Menu Principal          ║  ")
            menu.agregar("           ╠══════════════════════════════════╣")
            menu.agregar("           ║  1. Cargar Archivo               ║")
            menu.agregar("           ║  2. Procesar Archivo             ║")
            menu.agregar("           ║  3. Escribir Salida              ║")
            menu.agregar("           ║  4. Mostrar Datos Del Estudiante ║")
            menu.agregar("           ║  5. Generar Grafica              ║")
            menu.agregar("           ║  6. Salir                        ║")
            menu.agregar("           ╚══════════════════════════════════╝")
            menu.desplegar()
            a=int(input( "              Ingrese una opcion "))

            if a==1:
                borrar()
                print("         Ingresar nombre del archivo: \n")
                nombre=input("          ")
                b=input("       \nPresione una tecla para continuar...")
            else:
                if a==2:
                    borrar()
                    print("             Procesar Archivos")

                    b=input("       \nPresione una tecla para continuar...")
                else:
                    if(a==3):
                        borrar()
                        print("     Escribir la ruta para el archivo de salida:")
                        print("     Ejemplo: C:/Escritorio/salida.xml")
                        b=input("       ")
                        input("     \nPresione enter para continuar...")
                    else:
                        if(a==4):
                            borrar()
                            print("                                               ")
                            print("           ╔═════════════════════════════════════╗")
                            print("           ║        Datos del estudiante         ║ ")
                            print("           ╠═════════════════════════════════════╣")
                            print("           ║  Adolfo Francisco Lopez Cuzco       ║")
                            print("           ║  200011006                          ║")
                            print("           ║  Introduccion A La Programacion     ║")
                            print("           ║  y Computacion 2                    ║")
                            print("           ║  Ingenieria En Ciencias y Sistemas  ║")
                            print("           ║  4to Semestre                       ║")
                            print("           ╚═════════════════════════════════════╝")
                            input("           \nPresione enter para continuar...")
                        else:
                            if(a==5):
                                borrar()
                                print("     Generando Grafica De La Matriz")
                                b=input("   Presione enter para continuar...")
                            else:
                                if(a==6):
                                    borrar()
                                    print("\n     Esta seguro de salir S/N")
                                    res=input("      ")

                                    if(res=="s" or res=="S"):
                                        break
                                    else:
                                        if(res=="n" or res=="N"):
                                            continue
                                else:
                                    print("\n         Opcion incorrecta")
                                    b=input("Presione enter para continuar...")
                                    continue
    except Exception as e:
            print("Error al elegir error",e)

def borrar():
    os.system("cls")
