#Ingresar dos numeros
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))

#Operaciones matematicas
suma = a+b
multi = a*b
print("La suma de " + str(a) + " con el numero " + str(b) + " es igual a: " + str(suma))
print("La multiplicacion de " + str(a) + " con el numero " + str(b) + " es igual a: " + str(multi))

#Creamos una condicion
if (a>b):
    print("El numero de "+str(a)+" es mayor que "+str(b))
elif (a<b):
    print("El numero de "+str(a)+" es menor que "+str(b))
else:
    print("Los numeros son iguales")