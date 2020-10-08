import os

def Temperatura():
    print("---Opcion de temperaturas---")
    veces = int(input("Cuantas temperaturas ingresa?: "))
    suma = 0
    for x in range(veces):
        tempe = float(input("Ingrese temperatura: "))
        suma = tempe + suma
    print("El promedio de las temperaturas es: ", round((suma/veces),2))
    input("Presione enter para continuar")

def Personas():
    print("---Opcion datos de personas---")
    #Ingresar para n personas el nombre y la edad. N debe ser ingresado por teclado
    #Mostrar: cuantas personas son mayores de edad y cuantas son menores de edad.
    #Subir un tercer commit a git con el mensaje "Se agregó la opción 2 al menu"
    cant = int(input("Ingrese cantidad de personas: "))
    mayor = 0
    menor = 0
    for x in range(cant):
        input("Nombre de la persona: ")
        edad = int(input("Edad de la persona: "))
        print("")
        if(edad >= 18):
            mayor = mayor + 1
        else:
            menor = menor + 1
    print("Las personas mayores de edad son:", mayor)
    print("Las personas menores de edad son:", menor)
    input("Presione enter para continuar")

seguir = True

while(seguir):
    os.system('cls')
    print("1. Temperaturas")
    print("2. Datos de Personas")
    print("3. Salir")
    print("")
    op = int(input("Seleccione una opcion: "))

    if(op == 1):
        Temperatura()
    if(op == 2):
        Personas()
    if(op == 3):
        print("Programa finalizado")
        break

