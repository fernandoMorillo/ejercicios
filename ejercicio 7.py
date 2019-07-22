''' Crear un programa que le permita al usuario ingresar valores a una lista,
 y al imprimir muestre cuantos valores hay.  '''

lista = []
for x in range(4):
    n = int(input("Ingrese valor a incluir en la lista: "))
    lista.append(n)
print("Los valores de la lista son: ",lista )        