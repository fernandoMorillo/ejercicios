''' Desarrollar un algoritmo que solicite por teclado el peso de un niño y determine 
si está obeso o no. (Con 40 Kg o más ya se le considera obeso '''

peso = int(input("Ingrese el peso del niño: "))
if peso >= 40:
    print("¡El niño está en estado de OBESIDAD!")
else:
    print("El niño está bien de peso.")