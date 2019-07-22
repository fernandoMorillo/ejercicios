'''Pedir por pantalla tres números no consecutivos y mostrar en orden ascendente.'''

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))
num3 = int(input("Ingrese un tercer número: "))

if num1 > num2 and num2 > num3:
    print("Orden ascendete: ",num3,num2,num1)
elif num2 > num1 and num1 > num3:
    print("Orden ascendete: ",num3,num1,num2)
else:
    print("Orden ascendete: ",num1,num2,num3)        