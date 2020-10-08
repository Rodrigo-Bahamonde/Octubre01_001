#Ingresar n numeros donde n sea ingresado por el usuario (ciclo while)
#Mostrar cuantos son positivos, cuantos son negativos y cuantos son iguales a 0
n = 0
pos = 0
neg = 0
cero = 0
cont = int(input("Cuantos numeros ingresara?: "))
x = 1
while(x<=cont):
    num=int(input("Ingrese el numero: "))
    if(num < 0):
        pos = pos+1
    elif(num > 0):
        neg = neg+1
    else:
        cero = cero+1
    x = x+1

print("Los numeros positivos son: "+str(pos)+"\nLos numeros negativos son: "+str(neg)+"\nLos numeros iguales a 0 son: "+str(cero))