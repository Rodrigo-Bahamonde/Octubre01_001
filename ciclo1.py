#Crear ciclo for que permita ingresar 10 numeros, contar y mostrar cuantos son pares y cuantos son impares
par = 0
impar = 0
for x in range(10):
    num = int(input("Ingrese el numero "+ str(x+1) + ": "))
    if(num %2 == 0):
        par = par + 1 
    else:
        impar = impar + 1
print("Los numeros pares son: "+str(par)+"\nLos numeros impares son: "+str(impar))